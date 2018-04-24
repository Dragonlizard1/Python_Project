from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import time 
import re
import md5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
CHARUP_REGEX = re.compile(r'^[A-Z]+$')
app = Flask(__name__)      
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app,'logandreg')

@app.route('/')
def index():
	if "toggle" in session:
		session.pop("toggle")
	return render_template('index.html' )

@app.route("/result", methods = ["POST"])
def infoprocess():
	error = None
	num1 = False
	upperchar = False
	F_name = request.form["first_name"]
	L_name = request.form["last_name"]
	E_mail = request.form["email"]
	P_word = request.form["password"]
	CP_word = request.form["c_password"]
	salt = "gatsby"

	if F_name == "":
		error = 1
		flash("The First Name field is empty.", "error")
	elif len(F_name) < 3:
		error = 1
		flash("The First Name field need to have 3 character or more.", "error")
	elif not NAME_REGEX.match(F_name):
		error = 1
		flash("The First Name field must not have number.", "error")
	
	if L_name == "":
		error = 1
		flash("The Last Name field is empty.", "error")
	elif len(F_name) < 3:
		error = 1
		flash("The Last Name field need to have 3 character or more.", "error")
	elif not NAME_REGEX.match(L_name):
		error = 1
		flash("The Last Name field must not have number.", "error")
	
	if E_mail == "":
		error = 1
		flash("The Email field is empty.", "error")
	elif not EMAIL_REGEX.match(E_mail):
		error = 1
		flash("Invalid email address.", "error")
	
	if P_word == "":
		error = 1
		flash("The Password field is empty.", "error")
	elif len(P_word) < 8:
		error = 1
		flash("The Password field is less than 8 characters.", "error")
	
	if CP_word == "":
		error = 1
		flash("The Confirm Password field is empty.", "error")
	elif P_word != CP_word:
		error = 1
		flash("The Confirm Password field does not match with password.", "error")
			

	if error == None:
		flash("Thank you for submitting your information.", "correct")
	else:
		return redirect("/") 


	hashed_password = md5.new(P_word + salt).hexdigest()

	query = "INSERT INTO users (first_name, last_name, email, password, salt, created_at) VALUES (:first_name, :last_name, :email, :password, :salt, NOW())"

	data = {	
		'first_name': request.form['first_name'],
		'last_name': request.form['last_name'],
		'email': request.form['email'],
		'password': hashed_password,
		'salt': salt
	}
	
	mysql.query_db(query, data)
	session["toggle"] = "registration"

	return redirect('/success')

@app.route('/success')
def success():
	
	if session["toggle"] == "registration":
		message1 = "You have successfully register."
	elif session["toggle"] == "login":
	
		message1 = "You have login in:", session['name'] 
	return render_template('success.html', message_correct = message1 )

@app.route('/login', methods = ["POST"])
def login1():
	error = None
	E_mail = request.form["email"]
	password = request.form['password']

	if E_mail == "":
		error = 1
		flash("The Email field is empty.", "error")
		return redirect("/")
	elif not EMAIL_REGEX.match(E_mail):
		error = 1
		flash("Invalid email address.", "error")
		return redirect("/")

	user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
	query_data = {'email': E_mail}
	user = mysql.query_db(user_query, query_data)
	session['name'] = user[0]["first_name"] + " " + user[0]["last_name"]

	
	if len(user) != 0:
		encrypted_password = md5.new(password + user[0]['salt']).hexdigest()
		if user[0]['password'] != encrypted_password:
			error = 1
			flash("Invalid password.", "error")
			return redirect("/")
	else:
		error = 1
		flash("Invalid email address.", "error")
		return redirect("/") 


	if error == None:
		session["toggle"] = "login"
		return redirect("/success") 
	else:
		return redirect("/") 

app.run(debug=True)

