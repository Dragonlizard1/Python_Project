from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)    
app.secret_key = 'ThisIsSecret4'  



@app.route("/")  
def index():
	

	if "toggled" in session:
		
		
		
		if int(session["guessT"])  < session["fixnum"]:
			toggle1 = "lose"
			answer1 = "To Low!"
			print "inside if"
			return render_template("index.html", toggle1 = toggle1, answer1 = answer1)
		elif int(session["guessT"]) > session["fixnum"]:
			toggle1 = "lose"
			answer1 = "To High"
			print "inside if"
			return render_template("index.html", toggle1 = toggle1, answer1 = answer1)
		else:
			toggle1 = "win"
			answer1 = str(session["fixnum"]) + " was the number!"
			print "inside else"
			return render_template("index.html", toggle1 = toggle1, answer1 = answer1)
	else:
		if "guessT" in session:	
			session.pop("guessT")
		if "toggled" in session:	
			session.pop("toggled")
		session["fixnum"] = int(random.random() * 100)
		print session["fixnum"]
		toggle1 = "start"
		session["toggled"] = "toggled"
		answer1 = 'other'
	
	print "start 1"
	return render_template("index.html", toggle1 = toggle1, answer1 = answer1)

@app.route("/guess", methods = ["POST"])
def infoprocess():
	
	session["guessT"] = request.form["guessa"]
	return redirect("/")

@app.route("/reset", methods = ["POST"])
def reset():
	session.pop("guessT")

	session.pop("toggled")
	return redirect("/")

@app.route("/reset1")
def reset1():
	if "guessT" in session:	
		session.pop("guessT")
	if "toggled" in session:	
		session.pop("toggled")
	return redirect("/")


app.run(debug=True)  
   

