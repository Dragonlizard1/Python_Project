from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import time 
import datetime
import re
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

mysql = MySQLConnector(app,'emaillist')

@app.route('/')
def index():
	
	return render_template('index.html')


@app.route('/result', methods=['POST'])
def create():
	E_mail = request.form["email"]
	
	if E_mail == "":
		error = 1
		flash("The Email field is empty.", "error")
		return redirect('/')
	elif not EMAIL_REGEX.match(E_mail):
		error = 1
		flash("Invalid email address.", "error")
		print"error not match"
		return redirect('/')
	query = "INSERT INTO emails (email, created_at) VALUES (:email, NOW())"
	
	data = {
		'email': request.form['email']
		
	}

	mysql.query_db(query, data)
	return redirect('/success')

@app.route('/success')
def success():
	query = "SELECT * FROM emails"    
	email = mysql.query_db(query)
	toggle1 = "create"
	message1 = "The email address has been successfully added."
	return render_template('success.html', emails= email, message_correct = message1, toggle1 = toggle1 )

@app.route('/remove', methods=['POST'])
def delete():
	 
	message1 = "The email address has been successfully remove."
	toggle1 = "remove"
	query = "DELETE FROM emails WHERE email = :email"
	data = {'email': request.form["emailremove"]}
	mysql.query_db(query, data)

	query = "SELECT * FROM emails"    
	email = mysql.query_db(query)
	return render_template('/success.html', emails= email, message_correct = message1, toggle1 = toggle1)
'''
@app.route('/friends/<friend_id>')
def show(friend_id):
	
	query = "SELECT * FROM friends WHERE id = :specific_id"
	
	data = {'specific_id': friend_id}
	
	friends = mysql.query_db(query, data)
	
	return render_template('index.html', one_friend=friends[0])

@app.route('/update_friend/<friend_id>', methods=['POST'])
def update(friend_id):
	query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
	data = {
		'first_name': request.form['first_name'],
		'last_name':  request.form['last_name'],
		'occupation': request.form['occupation'],
		'id': friend_id
	}
	mysql.query_db(query, data)
	return redirect('/')

@app.route('/remove_friend/<friend_id>', methods=['POST'])
def delete(friend_id):
	query = "DELETE FROM friends WHERE id = :id"
	data = {'id': friend_id}
	mysql.query_db(query, data)
	return redirect('/')
'''
app.run(debug=True)

