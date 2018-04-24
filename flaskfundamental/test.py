from flask import Flask, render_template # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
print __name__        # directly, or importing it as a module.
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.
def hello_world():
	htmlWelcome = "<h1>Welcome to my Portfolio</h1>"
	htmlWelcome +="<p>My name is Robert.</p>"
	return htmlWelcome  # Return the string 'Hello World!' as a response.copy

@app.route('/projects')
def project():
	htmlString = "<h1>My Projects:</h1>"
	htmlString += "<ul><li>Hospital</li>"
	htmlString += "<li>Call Center</li>"
	htmlString += "<li>Pokedex</li>"
	htmlString += "<li>Api/Ajax</li></ul>"
	return htmlString


@app.route('/about')
def aboutme():
	htmlString1 ="I am a Python web developer and coding. I love golf. I love gaming. I love food. I love Coding Dojo"
	return htmlString1

app.run(debug=True)      # Run the app in debug mode.

