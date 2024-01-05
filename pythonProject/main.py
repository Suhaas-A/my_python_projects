from flask import Flask, render_template, request
import mysql.connector as mysql
from datetime import datetime
application = Flask(__name__)

global connection
global cursor
connection = mysql.connect(
            host='localhost',
            username='root',
            password='ssuhaass',
            db='shopping'
        )
cursor = connection.cursor()


def rename():
    try:
        if 'submit_2' in request.form:
            cursor.execute('''
                UPDATE Items
                SET name = %s, price = %s
                WHERE name = %s
            ''', (request.form['new_name'], request.form['new_price'], request.form['old_name']))
            connection.commit()
    except:
        None


def delete():
    try:
        print(request.form['delete_item'])
        cursor.execute('''
            DELETE FROM Items
            WHERE name = %s
        ''', (request.form['delete_item'],))
        connection.commit()
    except:
        None


@application.route('/', methods=['POST', 'GET'])
def home():
    print('hello')
    if request.method == "POST":
        if 'submit_1' in request.form:
            print('true')
            item = request.form['name']
            price = request.form['price']
    try:
        cursor.execute('''
            INSERT INTO ITEMS(name,price) VALUES(%s,%s)
        ''', (item, price))
    except:
        None
    cursor.execute('''
        SELECT * FROM ITEMS
    ''')
    info = cursor.fetchall()
    connection.commit()
    print('yes')
    return render_template('home_page.html', info=info, rename=rename, delete=delete)


global readings
readings = ''


def database():
    global readings
    cursor.execute('''
        SELECT name,price FROM ITEMS
    ''')
    readings = cursor.fetchall()
    connection.commit()


global item_price, new_readings
item_price = None
new_readings = []


def adding_items():
    global item_price, new_readings
    if 'item_submit' in request.form:
        clause = request.form['clause']
        print(clause)
        item_name = request.form['item_name']
        item_quantity = request.form['item_quantity']
        cursor.execute('''
            SELECT price FROM ITEMS WHERE name = %s
        ''', (item_name,))
        item_price = cursor.fetchall()[0][0]
        item_price *= int(item_quantity)
        cursor.execute('''
            INSERT INTO BILL_ITEMS(item_name,item_price,item_quantity,bill_id) VALUES(%s,%s,%s,%s)
        ''', (item_name, item_price, int(item_quantity), int(clause)))
        cursor.execute('''
            SELECT item_name,item_price,item_quantity
            FROM BILL_ITEMS
            JOIN BILLS
            ON BILL_ITEMS.BILL_ID = BILLS.ID
            WHERE bills.id = %s
        ''', (int(clause),))
        new_readings = cursor.fetchall()
        connection.commit()


global all_information
all_information = []


def insert_bill():
    global all_information
    if 'submit_bill_name' in request.form:
        bill_name = request.form['bill_name']
        phone_number = request.form['phone_number']
        email_id = request.form['email']
        cursor.execute('''
            INSERT INTO BILLS(bill_name,phone_number,email_id,date) VALUES(%s,%s,%s,%s)
        ''', (bill_name, int(phone_number), email_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        connection.commit()


global total_price
total_price = 0


@application.route("/bill", methods=['GET', 'POST'])
def billing():
    global  total_price
    all_prices = []
    global new_readings
    try:
        print(request.get_json()['value'])
        cursor.execute('''
                SELECT item_name,item_price,item_quantity
                FROM BILL_ITEMS
                JOIN BILLS
                ON BILL_ITEMS.BILL_ID = BILLS.ID
                WHERE bills.id = %s
            ''', (int(request.get_json()['value']),))
        new_readings = cursor.fetchall()
        for price in new_readings:
            all_prices.append(price[1])
        total_price = sum(all_prices)
        print(total_price)
        connection.commit()
    except:None
    global all_information
    cursor.execute('''SELECT bill_name,phone_number,email_id,date,id FROM BILLS''')
    all_information = cursor.fetchall()
    connection.commit()
    return render_template('billing_page.html', total_price=total_price, all_information=all_information, insert_bill=insert_bill, database=database, readings=readings, price=item_price, new_readings=new_readings, adding_items=adding_items)


if '__main__' == __name__:
    application.run()
