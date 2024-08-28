from flask import Flask, render_template, session, request, redirect, url_for
import os # It is used for making tokens. 
from typing import Any, Dict

#Make a Flask instance
app = Flask(__name__)

 # Make a random value with a parameter
key = os.urandom(21) 
app.secret_key = key # This will be a secret key to hold user session. 

#Make a dictionary Key, user ID : value, password
is_pwd: Dict[str, str] = {"lelouch" : "vermillioin"}

#Assuming it is a "main" function
# "/" indicates URL path
#Default is http://127.0.0.1:5000
@app.route("/")
def index() -> str:
	return "Hello World"

@app.route("/login")
def login():
	return render_template('login.html')

#Launch this app
if __name__ == "__main__":
	app.run(debug=True)