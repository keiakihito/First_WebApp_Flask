from flask import Flask, render_template, session, request, redirect, url_for
import os # It is used for making tokens. 

#Make a Flask instance
app = Flask(__name__)

 # Make a random value with a parameter
key = os.urandom(21) 
app.secret_key = key # This will be a secret key to hold user session. 



#Assuming it is a "main" function
# "/" indicates URL path
#Default is http://127.0.0.1:5000
@app.route("/")
def index() -> str:
	return "Hello World"


#Launch this app
if __name__ == "__main__":
	app.run(debug=True)