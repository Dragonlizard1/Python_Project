from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)    
app.secret_key = 'ThisIsSecret'  


@app.route("/")  
def start():
	
	

	if "count" in session:
		session["count"] = 1 + session["count"] 
		return render_template("index.html", count = session["count"])
	else:
		session["count"] = 1
		return render_template("index.html", count = session["count"])

@app.route("/plus2")
def plus2():
	session["count"] += 1
	return redirect("/")

@app.route("/reset")
def reset():
	session.pop("count")
	
	return redirect("/")

 #<input name='counter' type='text' value= 1>


app.run(debug=True)     

