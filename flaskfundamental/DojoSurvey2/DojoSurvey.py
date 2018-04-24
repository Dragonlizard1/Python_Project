from flask import Flask, render_template, request, session, redirect, flash
app = Flask(__name__)      
app.secret_key = 'ThisIsSecret'

@app.route("/")         
def index():
	return render_template("form.html")

@app.route("/result", methods = ["POST"])
def infoprocess():

	name = request.form["name"]
	location = request.form["location"]
	language = request.form["language"]
	comment = request.form["comment"]
	if name == "":
		flash("The name field is empty.")
		if comment == "":
			flash("Please add comment in.")
		elif len(comment) > 120:
			flash("Please put in less than 120 characters.")
		
		return redirect ("/")

	if comment == "":
		flash("Please add comment in.")
		return redirect ("/")
	elif len(comment) > 120:
		flash("Please put in less than 120 characters.")
		return redirect ("/")
	#print name
	return render_template("result.html", name1 = name, location1 = location, language1 = language, comment1 = comment) 


app.run(debug=True)     

