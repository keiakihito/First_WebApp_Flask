from flask import Flask, render_template, session, request, redirect, url_for, Response
import os # It is used for making tokens. 
from typing import Any, Dict, List, Tuple, Optional, Union, # This is for type hints
# Union: Allows you to specify multiple types for a variable. 
# For example, Union[int, str] means the variable can be an integer or a string.


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
def login() -> str:
	# Supposed to return the rendered HTML template as a string
	return render_template('login.html')

# Login authentication
 # The function returns either string (a URL) or a Flask"Response" object
@app.route("/logincheck", methods=["POST"])
def logincheck() -> Union[str, "Response"]: 
	user_id: str = request.form["user_id", ""]
	password: str  = request.form["password", ""]

	if user_id in id_pwd and password == id_pwd.get(user_id):
			session["login"] = True
	else:
		session["login"] = False

	# The url_for function takes the name of a view function 
	#(i.e., the function that is decorated with @app.route) and 
	# returns the corresponding URL for that function. 
	if session["login"]:
		return redirect(url_for("index"))
	else:
		return redirect(url_for("login"))



#Launch this app
if __name__ == "__main__":
	app.run(debug=True)