
inside of myEnvironment  folder
call flaskEnv\scripts\activate


from flask import Flask  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/')    

get will save data

how to post to send information as a no save data

@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   name = request.form['name']
   email = request.form['email']
   # redirects back to the '/' route
   return redirect('/')

In html need to setup post.

  <form action='/users' method='post'>
    Name:<input type='text' name='name'>
    Email:<input type='text' name='email'>
    <input type='submit' value='Submit'>
</form>

render template folder name must be name:  templates

@app.route('/ninjas')
def ninja():
	return render_template('ninjas.html')

Static filename
put in folder must be name:  static
defined a folder name placement

<!-- linking a css style sheet -->
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='my_style_sheet.css') }}">
<!-- linking a javascript file -->
<script type="text/javascript" src="{{ url_for('static', filename='my_script.js') }}"></script>
<!-- linking an image -->
<img src="{{ url_for('static', filename='my_img.png') }}">

custom error file page

@app.errorhandler(404)
def page_not_found(e):

------
api and ajax file creation
need to import jsonify and request

from flask import jsonify

@app.route('/_get_current_user')
def get_current_user():
    return jsonify(username=g.user.username,
                   email=g.user.email,
                   id=g.user.id)

another example

from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


>>> from time import gmtime, strftime
>>> strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
'Thu, 28 Jun 2001 14:17:15 +0000'

%m  for month
%p   for am or pm
--------

for loop in html
{% for x in session["activity1"]: %}
  {{x}}
  {% endfor %}

reverse loop html
{% for x in session["activity1"] | reverse: %}

if else statement html

  {% if toggle1 == "lose" %}
  {% elif toggle1 == "win"  %}
  {% endif %}

  ----------
  to flash message in html
  flash("test") inside python in array
  get_flashed_messages() inside html

  validation char

  r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'