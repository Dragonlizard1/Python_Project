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
mysql = MySQLConnector(app,'wallpost')

@app.route('/')
def index():
	if "id" in session:
		session.pop("id")

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
	session['message'] = "You have successfully registered."

	return redirect('/')

@app.route('/login', methods = ["POST"])
def login1():
	session["toggle"] = "other"
	session['message'] = ""
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
		session["id"] = user[0]["idusers"]
		session["activity"] = "start"
		return redirect("/wall") 
	else:
		return redirect("/") 

@app.route('/wall')
def wallpost():


	user_query = "SELECT users.idusers, CONCAT(users.first_name, ' ', users.last_name) as name, posts.idposts, posts.created_at, posts.posting FROM users "
	user_query += "Join posts on users.idusers = posts.users_id "
	user_query += "Order By posts.created_at DESC"
	#user_query += "WHERE users.idusers = :id"
#	query_data = {'id': int(session["id"])}
	posting1 = mysql.query_db(user_query)

	user_query = "SELECT posts.users_id, comments.posts_id, comments.comment, comments.created_at, " 
	user_query += "CONCAT(users2.first_name, ' ', users2.last_name) as name2 from posts "
	user_query += "Join comments on posts.idposts = comments.posts_id "
	user_query += "JOIN users as users2 on comments.users_id  = users2.idusers "
	user_query += "Order By posts.created_at DESC"
	#user_query += "WHERE posts.users_id = :id"
	#query_data = {'id': int(session["id"])}
	comment1 = mysql.query_db(user_query)
	


	return render_template('wall.html', posting1 = posting1, comment1 = comment1  )

@app.route('/addwall',  methods = ["POST"])
def addpost():
	query = "INSERT INTO posts (users_id, posting, created_at) VALUES (:id1, :posting, NOW())"
	
	data = {	
		"id1" : session["id"],
		'posting': request.form['post_text']		
	}

	mysql.query_db(query, data)

	return redirect("/wall") 


@app.route('/addcomment/<idposts>',  methods = ["POST"])
def addcomment(idposts):
	
	query = "INSERT INTO comments (users_id, posts_id, comment, created_at) VALUES (:id1, :idposts, :comment, NOW())"

	data = {	
		"id1" : session["id"],
		"idposts" : int(idposts),
		'comment': request.form['new_comment_text']		
	}

	mysql.query_db(query, data)
	return redirect("/wall") 

app.run(debug=True)

