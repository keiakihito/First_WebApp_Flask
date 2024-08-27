from flask import Flask, render_template, session, request, redirect, url_for

#Make a Flask instance
app = Flask(__name__)


#Assuming it is a "main" function
# "/" indicates URL path
#Default is localhost:5000/
@app.route("/")
def index() -> str:
	return "Hello World"


#Launch this app
if __name__ == "__main__":
	app.run(debug=True)