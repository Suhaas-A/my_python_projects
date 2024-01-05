from flask import Flask, render_template, request, redirect, url_for
import datetime
import mysql.connector as connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
app = Flask(__name__)

global value
value = None

global authorisation
authorisation = False

global connection
connection = connector.connect(
    host="localhost",
    user="root",
    password="ssuhaass",
    database="secret_santa"
)

global cursor
cursor = connection.cursor(buffered=True)

global show
show = False


def forget_password():
    try:
        global show
        show = True
        global json_data
        json_data = request.get_json()['value']
        global user_info
        user_info = json_data
        cursor.execute('''
            SELECT email FROM authorisation
            WHERE username = %s
        ''', (json_data, ))

        html_content = '''
            <p>Click the button below to confirm your new password:</p>
            <table border="0" cellspacing="0" cellpadding="0">
                <tr>
                    <td style="border-radius: 3px; background-color: #3498db;">
                        <a href="http://127.0.0.1:5000/reset_password" target="_blank" style="padding: 15px 25px; color: #ffffff; text-decoration: none; display: inline-block;">Click me</a>
                    </td>
                </tr>
            </table>
        '''

        to_email = cursor.fetchone()[0]
        message = MIMEMultipart()
        message["From"] = "suhaas062010@gmail.com"
        message["To"] = str(to_email)
        message["Subject"] = 'Change password for secret santa'
        message.attach(MIMEText(html_content, "html"))

    # Connect to the SMTP server and send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("suhaas062010@gmail.com", "srdi kczm dpuq vthf")
            server.sendmail("suhaas062010@gmail.com", str(to_email), message.as_string())
        connection.commit()
    except:
        None


@app.route('/authorisation', methods=['GET', 'POST'])
def login():
    if 'login' in request.form:
        cursor.execute('''
            SELECT username, password FROM authorisation
        ''')
        credentials = cursor.fetchall()
        username = request.form['username']
        password = request.form['password']
        connection.commit()
        if (username, password) in credentials:
            global authorisation
            authorisation = True
            global user_info
            user_info = username
            return redirect(url_for('home'))
        else:
            return render_template('authorisation.html', alert='Invalid username or password', forget_password=forget_password)
    return render_template('authorisation.html', alert=None, forget_password=forget_password)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if 'register' in request.form:
        try:
            global authorisation
            authorisation = True

            username = request.form['username']
            password = request.form['password']
            email = request.form['email']

            global user_info
            user_info = username

            cursor.execute('''
                INSERT INTO authorisation(email, username, password) VALUES(%s, %s, %s)
            ''', (email, username, password))

            cursor.execute('''
                SELECT id FROM authorisation WHERE username = %s
            ''', (username,))
            auth_id = cursor.fetchone()[0]

            name = request.form['name']
            gender = request.form['gender']
            year = str(request.form['dob_year'])
            month = str(request.form['dob_month'])
            day = str(request.form['dob_day'])
            str_dob = year + month + day
            dob = datetime.datetime.strptime(str_dob, '%Y%m%d').date()

            cursor.execute('''
                INSERT INTO profile(gender, name, dob, auth_id) VALUES(%s, %s, %s, %s)
            ''', (gender, name, dob, auth_id))
            connection.commit()
            return redirect(url_for('home'))
        except:
            return render_template('registration.html', alert="Username or email already exists", date=datetime.datetime.now(), years=reversed(range(datetime.datetime.now().year - 150, datetime.datetime.now().year + 1)), months=range(1, 13), days=range(1, 31))
    return render_template('registration.html', alert=None, date=datetime.datetime.now(), years=reversed(range(datetime.datetime.now().year - 150, datetime.datetime.now().year + 1)), months=range(1, 13), days=range(1, 31))


@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if show == True:
        if 'reset_password' in request.form:
            password = request.form['password']
            re_password = request.form['re_password']
            cursor.execute('''
                SELECT password FROM authorisation
                WHERE username = %s
            ''', (user_info,))
            if cursor.fetchone()[0] == password:
                return render_template('new_password.html', alert='Please don`t enter your old password')
            else:
                if password == re_password:
                    cursor.execute('''
                        UPDATE authorisation
                        SET password = %s
                        WHERE username = %s
                    ''', (password, json_data))
                    connection.commit()
                    return redirect(url_for('login'))
                else:
                    return render_template('new_password.html', alert='Please give the correct confirmation password')
        return render_template('new_password.html', alert=None)
    else:
        return redirect(url_for('home'))


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    request.form.to_dict().clear()
    if authorisation == False:
        return redirect(url_for('login'))
    cursor.execute('''
        SELECT name, gender, DOB
        FROM profile
        JOIN authorisation
        ON profile.auth_id = authorisation.id
        WHERE username = %s
    ''', (user_info, ))
    profile_info = cursor.fetchone()
    cursor.execute('''
        SELECT blogs.post_date , blogs.post_subject , blogs.post_content , profile.name , authorisation.username
        FROM blogs
        JOIN authorisation
        ON blogs.auth_id = authorisation.id
        JOIN profile
        ON profile.auth_id = authorisation.id
        ORDER BY blogs.post_date DESC
    ''')
    all_blogs = cursor.fetchall()
    if 'create' in request.form:
        cursor.execute('''
            SELECT id FROM authorisation
            WHERE username = %s
        ''', (user_info,))
        post_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        post_subject = str(request.form['subject'])
        post_content = str(request.form['content'])
        auth_id = cursor.fetchone()[0]
        cursor.execute('''
            INSERT INTO blogs (post_date, post_subject, post_content, auth_id) VALUES (%s, %s, %s, %s)
        ''', (post_date, post_subject, post_content, auth_id))
        connection.commit()
        request.form.to_dict().pop('create')
        return redirect(url_for('home'))
    if 'del' in request.form:
        param = datetime.datetime.strptime(request.form['invis_param'], "%Y-%m-%d %H:%M:%S")
        request.form.to_dict().pop('del')
        cursor.execute('''
            DELETE FROM blogs
            WHERE post_date = %s
        ''', (param, ))
        connection.commit()
        return redirect(url_for('home'))
    if 'edit' in request.form:
        request.form.to_dict().pop('edit')
        subject = request.form['subject']
        content = request.form['content']
        date = request.form['date']
        cursor.execute('''
            UPDATE blogs
            SET post_subject = %s, post_content = %s, post_date = %s
            WHERE post_date = %s
        ''', (subject, content, datetime.datetime.now(), date))
        connection.commit()
        return redirect(url_for('home'))
    return render_template('home.html', information=profile_info, username=user_info, blogs=all_blogs)


@app.route('/join_group', methods=['GET', 'POST'])
def join_group():
    request.form.to_dict().clear()
    if authorisation == False:
        return redirect(url_for('login'))
    if 'join' in request.form:
        request.form.to_dict().pop('join')
        key = request.form['key']
        password = request.form['password']
        try:
            cursor.execute('''
                SELECT id FROM all_groups
                WHERE special_key = %s AND password = %s
            ''', (key, password))
            group_id = cursor.fetchone()[0]
            cursor.execute('''
                SELECT id FROM authorisation
                WHERE username = %s        
            ''', (user_info,))
            my_id = cursor.fetchone()[0]
            cursor.execute('''
                INSERT INTO group_members (group_id,auth_id) VALUES (%s,%s)
            ''', (group_id, my_id))
            connection.commit()
            return redirect(url_for('my_groups'))
        except:
            alert = 'There is an error in request'
            return render_template('join_group.html')
    return render_template('join_group.html')


@app.route('/create_group', methods=['GET', 'POST'])
def create_group():
    request.form.to_dict().clear()
    if authorisation == False:
        return redirect(url_for('login'))
    cursor.execute('''
        SELECT group_name,min_price,dead_line,date_time,all_groups.password
        FROM ALL_GROUPS
        JOIN AUTHORISATION
        ON ALL_GROUPS.AUTH_ID = AUTHORISATION.ID
        WHERE USERNAME = %s
    ''', (user_info,))
    group_info = cursor.fetchall()
    print(group_info)
    cursor.execute('''
        SELECT profile.name
        FROM AUTHORISATION
        JOIN PROFILE
        ON AUTHORISATION.ID = PROFILE.AUTH_ID
        WHERE USERNAME = %s
    ''', (user_info,))
    name = cursor.fetchone()[0]
    if 'create' in request.form:
        request.form.to_dict().pop('create')
        group_name = request.form['group_name']
        min_price = request.form['min_price']
        dead_line = int(request.form['deadline'])
        dead_line = datetime.datetime.now().date() + datetime.timedelta(days=dead_line)
        password = request.form['password']
        cursor.execute('''
            SELECT id FROM authorisation
            WHERE username = %s
        ''', (user_info,))
        auth_id = cursor.fetchone()[0]
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('''
            SELECT special_key FROM all_groups
        ''')
        special_keys = cursor.fetchall()
        while True:
            import random
            choice1 = ['a', 'b', 'c', 'd', 'e']
            choice2 = ['a', 'b', 'c', 'd', 'e']
            choice3 = ['a', 'b', 'c', 'd', 'e']
            choice4 = ['a', 'b', 'c', 'd', 'e']
            choice5 = ['a', 'b', 'c', 'd', 'e']
            choice6 = ['a', 'b', 'c', 'd', 'e']
            choice7 = ['a', 'b', 'c', 'd', 'e']
            choice8 = ['a', 'b', 'c', 'd', 'e']
            choice9 = ['a', 'b', 'c', 'd', 'e']
            choice10 = ['a', 'b', 'c', 'd', 'e']
            choice11 = ['a', 'b', 'c', 'd', 'e']
            choice12 = ['a', 'b', 'c', 'd', 'e']
            choice13 = ['a', 'b', 'c', 'd', 'e']
            choice14 = ['a', 'b', 'c', 'd', 'e']
            choice15 = ['a', 'b', 'c', 'd', 'e']
            choice16 = ['1', '2', '3', '4', '5']
            choice17 = ['1', '2', '3', '4', '5']
            choice18 = ['1', '2', '3', '4', '5']
            choice19 = ['1', '2', '3', '4', '5']
            choice20 = ['1', '2', '3', '4', '5']
            sys_choice = [random.choice(choice1), random.choice(choice2), random.choice(choice3), random.choice(choice4), random.choice(choice5), random.choice(choice6), random.choice(choice7), random.choice(choice8), random.choice(choice9), random.choice(choice10), random.choice(choice11), random.choice(choice12), random.choice(choice13), random.choice(choice14), random.choice(choice15), random.choice(choice16), random.choice(choice17), random.choice(choice18), random.choice(choice19), random.choice(choice20)]
            random.shuffle(sys_choice)
            cus_choice = ''
            for digit in range(len(sys_choice)):
                cus_choice += sys_choice[digit]
            if (cus_choice,) in special_keys:
                cus_choice = ''
                continue
            else:
                break
        cursor.execute('''
            INSERT INTO ALL_GROUPS (date_time,min_price,group_name,dead_line,auth_id,special_key,password) VALUES (%s,%s,%s,%s,%s,%s,%s)
        ''', (date, min_price, group_name, dead_line, auth_id, cus_choice, password))
        cursor.execute('''
            SELECT id FROM ALL_GROUPS
            WHERE date_time = %s
        ''', (date,))
        group_id = cursor.fetchone()[0]
        cursor.execute('''
            INSERT INTO group_members (auth_id,group_id) VALUES (%s,%s)
        ''', (auth_id, group_id))
        return redirect(url_for('create_group'))
    if 'del_2' in request.form:
        param = datetime.datetime.strptime(request.form['invis_param'], "%Y-%m-%d %H:%M:%S")
        request.form.to_dict().pop('del_2')
        cursor.execute('''
            DELETE FROM ALL_GROUPS
            WHERE date_time = %s
        ''', (param,))
        return redirect(url_for('create_group'))
    if 'edit' in request.form:
        request.form.to_dict().pop('edit')
        new_group_name = request.form['group_name']
        new_min_price = request.form['min_price']
        new_dead_line = int(request.form['deadline'])
        new_dead_line = datetime.datetime.now().date() + datetime.timedelta(days=new_dead_line)
        date_param = datetime.datetime.strptime(request.form['date_param'], "%Y-%m-%d %H:%M:%S")
        new_password = request.form['password']
        cursor.execute('''
            UPDATE all_groups
            SET group_name = %s, min_price = %s, dead_line = %s, date_time = %s, password = %s
            WHERE date_time = %s
        ''', (new_group_name, new_min_price, new_dead_line, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), new_password, date_param))
        connection.commit()
        return redirect(url_for('create_group'))
    return render_template('create_group.html', groups=group_info, name=name)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    global user_info
    global authorisation
    request.form.to_dict().clear()
    if authorisation == False:
        return redirect(url_for('login'))
    cursor.execute('''
        SELECT profile.name,profile.DOB,profile.gender,authorisation.username,authorisation.password,authorisation.email
        FROM profile
        JOIN authorisation
        ON profile.auth_id = authorisation.id
        WHERE username = %s
    ''', (user_info,))
    profile_data = cursor.fetchone()
    strings = [profile_data[1].day, profile_data[1].month, profile_data[1].year]
    if 'del' in request.form:
        request.form.to_dict().pop('del')
        cursor.execute('''
            DELETE FROM authorisation
            WHERE username = %s
        ''', (user_info,))
        authorisation = False
        return redirect(url_for('home'))
    if 'edit_profile' in request.form:
        request.form.to_dict().pop('edit_profile')
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        name = request.form['name']
        gender = request.form['gender']
        year = str(request.form['dob_year'])
        month = str(request.form['dob_month'])
        day = str(request.form['dob_day'])
        str_dob = year + month + day
        dob = datetime.datetime.strptime(str_dob, '%Y%m%d').date()
        cursor.execute('''
            SELECT profile.auth_id
            FROM authorisation
            JOIN profile
            ON authorisation.id = profile.auth_id
            WHERE username = %s
        ''', (user_info,))
        parameter = cursor.fetchone()[0]
        cursor.execute('''
            UPDATE profile
            SET name = %s,gender = %s,DOB = %s
            WHERE auth_id = %s
        ''', (name, gender, dob, parameter))
        cursor.execute('''
            UPDATE authorisation
            SET username = %s,password = %s,email = %s
            WHERE username = %s
        ''', (username, password, email, user_info))
        user_info = username
        return redirect(url_for('profile'))
    connection.commit()
    return render_template('profile.html', data=profile_data, date_data=strings, gender=['Male', 'Female'], date=datetime.datetime.now(), years=reversed(range(datetime.datetime.now().year - 150, datetime.datetime.now().year + 1)), months=range(1, 13), days=range(1, 31))


@app.route('/my_groups', methods=['GET', 'POST'])
def my_groups():
    request.form.to_dict().clear()
    if authorisation == False:
        return redirect(url_for('login'))
    cursor.execute('''
        SELECT all_groups.group_name,all_groups.id
        FROM group_members
        JOIN authorisation
        ON authorisation.id = group_members.auth_id
        JOIN all_groups
        ON all_groups.id = group_members.group_id
        WHERE username = %s
    ''', (user_info,))
    all_groups = cursor.fetchall()
    cursor.execute('''
        SELECT profile.name
        FROM authorisation
        JOIN profile
        ON profile.auth_id = authorisation.id
        WHERE authorisation.username = %s
    ''', (user_info,))
    name = cursor.fetchone()[0]
    connection.commit()
    return render_template('my_groups.html', my_groups=all_groups, name=name)


@app.route('/group_details', methods=['GET', 'POST'])
def group_details():
    if authorisation == False:
        return redirect(url_for('login'))
    try:
        if request.method == 'POST' and request.form == {}:
            global value
            value = request.get_json()['id']
            request.get_json().pop('id')
        connection_2 = connector.connect(
            host="localhost",
            user="root",
            password="ssuhaass",
            database="secret_santa"
        )
        cursor_2 = connection_2.cursor(buffered=True)
        cursor_2.execute('''
            SELECT profile.name,authorisation.username,authorisation.id,all_groups.group_name,all_groups.special_key
            FROM authorisation
            JOIN profile
            ON authorisation.id = profile.auth_id
            JOIN group_members
            ON authorisation.id = group_members.auth_id
            JOIN all_groups
            ON all_groups.id = group_members.group_id
            WHERE all_groups.id = %s
        ''', (value,))
        members = cursor_2.fetchall()
        cursor_2.execute('''
            SELECT auth_id,group_id,id,name,price FROM wishes
            WHERE wishes.group_id = %s;
        ''', (value,))
        all_wishes = cursor_2.fetchall()
        wish_users = []
        no_wish_users = []
        cursor_2.execute('''
            SELECT auth_id FROM wishes
            WHERE group_id = %s
        ''', (value,))
        wish_auth_id = cursor_2.fetchall()
        cursor_2.execute('''
            SELECT id FROM authorisation
            WHERE username = %s
        ''', (user_info,))
        my_id = cursor_2.fetchone()[0]
        for member in members:
            if (member[2],) in wish_auth_id:
                wish_users.append(member[2])
            else:
                no_wish_users.append(member[2])
        print(request.form.to_dict())
        cursor_2.execute('''
            SELECT auth_id FROM ALL_GROUPS
            WHERE id = %s
        ''', (value,))
        leader_id = int(cursor_2.fetchone()[0])
        leader = None
        if leader_id == my_id:
            leader = True
        if 'create_wish' in request.form:
            request.form.to_dict().pop('create_wish')
            create_item_name = request.form['create_item_name']
            create_item_price = request.form['create_item_price']
            cursor_2.execute('''
                INSERT INTO WISHES (auth_id,group_id,name,price) VALUES (%s,%s,%s,%s)
            ''', (my_id, value, create_item_name, int(create_item_price)))
            connection_2.commit()
            return redirect(url_for('group_details'))
        if 'draw_names' in request.form:
            request.form.to_dict().pop('draw_names')
            import random
            cursor_2.execute('''
                SELECT auth_id,drawn_auth_id FROM GROUP_MEMBERS
                WHERE GROUP_ID = %s
            ''', (value,))
            people = cursor_2.fetchall()
            print(people)
            for person in range(len(people)):
                people[person] = people[person][0]
            print(people)
            draw = {}
            i = 0
            while len(draw) < len(people):
                key = random.choice(people)
                value = random.choice(people)
                if key != value:
                    if key not in draw and value not in draw.values():
                        draw[key] = value
                    else:
                      i += 1
                      if i == 5:
                        draw.clear()
                        i = 0
                        continue
            for i in draw:
                cursor_2.execute('''
                    UPDATE GROUP_MEMBERS
                    SET drawn_auth_id = %s
                    WHERE auth_id = %s
                ''', (draw[i], i))
            connection_2.commit()
            return redirect(url_for('my_groups'))
        if 'edit_wish' in request.form:
            request.form.to_dict().pop('edit_wish')
            item_name = request.form['item_name']
            item_price = request.form['item_price']
            cursor_2.execute('''
                UPDATE wishes
                SET name = %s , price = %s
                WHERE group_id = %s AND auth_id = %s
            ''', (item_name, int(item_price), int(value), int(my_id)))
            connection_2.commit()
            return redirect(url_for('group_details'))
        if 'chat' in request.form:
            request.form.to_dict().pop('chat')
            message = request.form['message']
            cursor_2.execute('''
                INSERT INTO group_chat(auth_id,group_id,text) VALUES(%s,%s,%s)
            ''', (my_id, value, message))
            connection_2.commit()
            return redirect(url_for('group_details'))
        cursor_2.execute('''
            SELECT group_chat.text,profile.name
            FROM group_chat
            JOIN profile
            ON group_chat.auth_id = profile.auth_id
            WHERE group_chat.group_id = %s
            ORDER BY group_chat.id DESC
        ''', (value,))
        all_chat = cursor_2.fetchall()
        try:
            cursor_2.execute('''
                SELECT PROFILE.NAME
                FROM GROUP_MEMBERS
                JOIN PROFILE
                ON GROUP_MEMBERS.DRAWN_AUTH_ID = PROFILE.AUTH_ID
                WHERE GROUP_MEMBERS.AUTH_ID = %s AND GROUP_MEMBERS.GROUP_ID = %s
            ''', (my_id, value))
            drawn_name = cursor_2.fetchone()[0]
        except:
            drawn_name = None
        cursor_2.execute('''
            SELECT drawn_auth_id FROM GROUP_MEMBERS
            WHERE GROUP_ID = %s
        ''', (value,))
        rand = cursor_2.fetchone()[0]
        return render_template('group_details.html', yes_no=rand, drawn_name=drawn_name, chats=all_chat, my_id=my_id, value=value, members=members, wishes=all_wishes, wish_users=wish_users, no_wish_users=no_wish_users, leader=leader)
    except:
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
