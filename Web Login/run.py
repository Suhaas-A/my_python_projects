import mysql.connector as mysql
import imaplib
import email
from email.utils import parsedate_to_datetime
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

global username
global password
username = None
password = None

@app.route('/gmail', methods=['GET', 'POST'])
def gmail():
	global username
	global password
	print(username)
	print(password)
	i = 0
	connection = mysql.connect(
			username='root',
			password='ssuhaass',
			host='localhost',
			db='emails'
		)
	cursor = connection.cursor()
		
	cursor.execute('''
		SELECT reciever FROM recievers
	''')
	try:
		all_users = cursor.fetchall()
	except:
		all_users = ['']

	print((username,) in all_users, all_users , (username,))
	if (username,) in all_users:
		try:
			print('yes')
			cursor.execute('''
				SELECT message_number , reciever
				FROM email
				JOIN recievers
				ON email.to_id = recievers.to_id
				WHERE reciever = %s
			''',(username,))
			all_msgnums = cursor.fetchall()

			mails = []
			imap = imaplib.IMAP4_SSL("imap.gmail.com")
			imap.login(str(username), str(password))
			imap.select('inbox')
			_,msgnums = imap.search(None, 'ALL')
			for msgnum in msgnums[0].split():
				if int(msgnum) <= int(all_msgnums[len(all_msgnums) - 1][0]):continue
				if int(msgnum) == 101 + int(all_msgnums[len(all_msgnums) - 1][0]):break
				_,data = imap.fetch(msgnum, "(RFC822)")
				message = email.message_from_bytes(data[0][1])
				for part in message.walk():
					if part.get_content_type() == 'text/plain':
						mails.append([int(msgnum),parsedate_to_datetime(message.get('Date')).strftime('%Y-%m-%d %H:%M:%S'),message.get('From'),message.get('To'),message.get('Subject'),part.get_payload()])
				

			cursor.execute('''
				SELECT to_id FROM recievers WHERE reciever = %s
			''',(username,))
			to_id = cursor.fetchone()

			for mail in mails:
				cursor.execute('''
					SELECT sender FROM senders
				''')
				all_senders = cursor.fetchall()
				print(str(mail[2]) , all_senders , str(mail[2]) in all_senders)
				if (mail[2].lower(),) in all_senders:
					print('nice')
					cursor.execute('''
						SELECT from_id FROM senders WHERE sender = %s
					''', (mail[2].lower(),))
					from_id = cursor.fetchone()
					cursor.execute('''
						INSERT INTO email VALUES(%s,%s,%s,%s,%s,%s)
					''',(str(mail[0]),str(mail[1]),str(mail[4]),str(mail[5]),from_id[0],to_id[0]))
				else:	
					cursor.execute('''
						INSERT INTO senders(sender) VALUES(%s)
					''',(mail[2].lower(),))
					cursor.execute('''
						SELECT from_id FROM senders WHERE sender = %s
					''', (mail[2].lower(),))
					from_id = cursor.fetchone()
					cursor.execute('''
						INSERT INTO email() VALUES(%s,%s,%s,%s,%s,%s)
					''',(mail[0],mail[1],mail[4],mail[5],from_id[0],to_id[0]))
				connection.commit()
		except:None
	else:
		mails = []
		imap = imaplib.IMAP4_SSL("imap.gmail.com")
		imap.login(str(username), str(password))
		imap.select('inbox')
		_,msgnums = imap.search(None, 'ALL')
		for msgnum in msgnums[0].split():
			if int(msgnum) == 101:break
			_,data = imap.fetch(msgnum, "(RFC822)")
			message = email.message_from_bytes(data[0][1])
			for part in message.walk():
				if part.get_content_type() == 'text/plain':
					mails.append([msgnum,parsedate_to_datetime(message.get('Date')).strftime('%Y-%m-%d %H:%M:%S'),message.get('From'),message.get('To'),message.get('Subject'),part.get_payload()])
					print(msgnum)

		cursor.execute('''
			INSERT INTO recievers(reciever) VALUES(%s)
		''',(username,))
		cursor.execute('''
			SELECT to_id FROM recievers WHERE reciever = %s
		''',(username,))
		to_id = cursor.fetchone()

		for mail in mails:
			cursor.execute('''
				SELECT sender FROM senders
			''')
			all_senders = cursor.fetchall()
			print((mail[2],) in all_senders,(mail[2],),all_senders)
			if (mail[2].lower(),) in all_senders:
				print('nice')
				cursor.execute('''
					SELECT from_id FROM senders WHERE sender = %s
				''', (mail[2].lower(),))
				from_id = cursor.fetchone()
				cursor.execute('''
					INSERT INTO email VALUES(%s,%s,%s,%s,%s,%s)
				''',(mail[0],mail[1],mail[4],mail[5],from_id[0],to_id[0]))
	
			else:
				cursor.execute('''
					INSERT INTO senders(sender) VALUES(%s)
				''',(mail[2].lower(),))
				cursor.execute('''
					SELECT from_id FROM senders WHERE sender = %s
				''', (mail[2].lower(),))
				from_id = cursor.fetchone()
				cursor.execute('''
					INSERT INTO email() VALUES(%s,%s,%s,%s,%s,%s)
				''',(mail[0],mail[1],mail[4],mail[5],from_id[0],to_id[0]))
			connection.commit()

	cursor.execute('''
		SELECT message_number,date_time,subject,content,reciever,sender
		FROM email
		JOIN recievers
		ON email.to_id = recievers.to_id
		JOIN senders
		ON email.from_id = senders.from_id
		WHERE reciever = %s
		ORDER BY message_number DESC
	''',(username,))

	i = 0

	all_info = cursor.fetchall()

	connection.commit()						
 
	return render_template('gmail.html', all_info=all_info, username=username, password=password)

@app.route('/', methods=['GET', 'POST'])
def home():
	global username
	global password
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		return redirect(url_for('gmail'))
	return render_template('home.html')

if '__main__' == __name__:
	app.run()