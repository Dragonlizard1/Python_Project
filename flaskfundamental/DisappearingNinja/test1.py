from flask import Flask, render_template, request, redirect
app = Flask(__name__)      

@app.route("/")         
def index():
	emptyninja = "There is no ninja here"
	return render_template("index.html", no_ninja = emptyninja)

@app.route("/ninja")         
def allninja():
	head1 = '<head><link rel="stylesheet" type="text/css" href="../static/my_style_sheet.css"></head>'

	ninja = "<body><div id = 'tmnt'>"
	ninja += "<h1>TMNT Master</h1>"
	ninja += '<img src = "../static/tmnt.png">'
	ninja += "<a href = '/ninja/blue'>Leonardo</a>"
	ninja += "<a href = '/ninja/red'>Raphael</a>"
	ninja += "<a href = '/ninja/purple'>Donatello</a>"
	ninja += "<a href = '/ninja/orange'>Michelangelo</a>"
	ninja += "</div></body>"
	head1 += ninja
	return head1
	#return render_template("ninjas.html", leo1 = leonardo, mich1 = michangelo, don1 = donatello, ralph1 = raphael)

@app.route("/ninja/blue")
def leoninja():
	head1 = '<head><link rel="stylesheet" type="text/css" href="../static/my_style_sheet.css"></head>'

	ninja = "<body><div id = 'leonardo'>"
	ninja += "<h2>Leonardo</h2>"
	ninja += '<img src = "../static/leonardo.jpg">'
	ninja += "</div></body>"
	head1 += ninja
	return head1

@app.route("/ninja/orange")
def michninja():
	head1 = '<head><link rel="stylesheet" type="text/css" href="../static/my_style_sheet.css"></head>'

	ninja = "<body><div id = 'michelangelo'>"
	ninja += "<h2>Michelangelo</h2>"
	ninja += '<img src = "../static/michelangelo.jpg">'
	ninja += "</div></body>"
	head1 += ninja
	return head1

@app.route("/ninja/red")
def ralphninja():
	head1 = '<head><link rel="stylesheet" type="text/css" href="../static/my_style_sheet.css"></head>'

	ninja = "<body><div id = 'raphael'>"
	ninja += "<h2>Raphael</h2>"
	ninja += '<img src = "../static/raphael.jpg">'
	ninja += "</div></body>"
	head1 += ninja
	return head1

@app.route("/ninja/purple")
def donninja():
	head1 = '<head><link rel="stylesheet" type="text/css" href="../static/my_style_sheet.css"></head>'

	ninja = "<body><div id = 'donatello'>"
	ninja += "<h2>Donatello</h2>"
	ninja += '<img src = "../static/donatello.jpg">'
	ninja += "</div></body>"
	head1 += ninja
	return head1

@app.errorhandler(404)
def page_not_found(e):
	head1 = '<head><link rel="stylesheet" type="text/css" href="../static/my_style_sheet.css"></head>'

	ninja = "<body><div id = 'notapril'>"
	ninja += "<h2>Notapril</h2>"
	ninja += '<img src = "../static/notapril.jpg">'
	ninja += "</div></body>"
	head1 += ninja
	return head1

app.run(debug=True)     

