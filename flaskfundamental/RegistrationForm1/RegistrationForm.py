from flask import Flask, render_template, request, session, redirect, flash
import re
import time
app = Flask(__name__)      
app.secret_key = 'ThisIsSecret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
CHARUP_REGEX = re.compile(r'^[A-Z]+$')



@app.route("/")         
def index():
	return render_template("form.html")

@app.route("/result", methods = ["POST"])
def infoprocess():
	error = None
	num1 = False
	upperchar = False
	DOBletter = False
	F_name = request.form["F_name"]
	L_name = request.form["L_name"]
	E_mail = request.form["E_mail"]
	P_word = request.form["P_word"]
	CP_word = request.form["CP_word"]
	DOB = request.form["DOB"]
	DOB = DOB.split("/")

	if F_name == "":
		error = 1
		flash("The First Name field is empty.", "error")
	elif not NAME_REGEX.match(F_name):
		error = 1
		flash("The First Name field must not have number.", "error")
	
	if L_name == "":
		error = 1
		flash("The Last Name field is empty.", "error")
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
	else:
		for char1 in P_word:
			if char1.isdigit():
				num1 = True
			if CHARUP_REGEX.match(char1):
				upperchar = True
		if upperchar == False:
			flash("Must have 1 letter capital.", "error")
		elif (num1 == False):
			flash("Must enter 1 number in password.", "error")

	if CP_word == "":
		error = 1
		flash("The Confirm Password field is empty.", "error")
	elif P_word != CP_word:
		error = 1
		flash("The Confirm Password field does not match with password.", "error")
			
	

	for element in DOB:
		if NAME_REGEX.match(element):
			DOBletter = True
	if len(DOB) < 3:
		flash("Please use correct seperation for DOB.", "error")
	elif DOBletter == True:
		flash("Please no character in DOB.", "error")
	elif int(DOB[2]) > time.strftime("%Y"):  # year check
		flash("The year is incorrect in DOB.", "error")
	elif int(DOB[0]) > 12:
		flash("Month is incorrect in DOB.", "error")
	elif int(DOB[2]) <= time.strftime("%Y"):
		
		if (int(DOB[0]) > int(time.strftime("%m"))) and (int(DOB[2]) == int(time.strftime("%Y"))):
			
			flash("Month is incorrect in DOB.", "error")
		elif (int(DOB[0]) == int(time.strftime("%m"))) and (int(DOB[2]) == int(time.strftime("%Y"))) and (int(DOB[1]) > int(time.strftime("%d"))):
			flash("Day is incorrect in DOB.", "error")
		elif (int(DOB[0]) in [1,3,5,7,8,10,12]):
			if int(DOB[1]) > 31:
				flash("The day is incorrect in DOB.", "error")				
		elif (int(DOB[0]) in [4,5,9,11]):
			if int(DOB[1]) > 30:
				flash("The day is incorrect in DOB.", "error")
		elif int(DOB[1]) > 28:  #it does not count for leap year
			flash("The day is incorrect in DOB.", "error")

	if error == None:
		flash("Thank you for submitting your information.", "correct")
	return redirect("/") 


app.run(debug=True)     

