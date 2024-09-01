from flask import Flask, render_template, session, request, redirect, url_for, Response
import os # It is used for making tokens. 
from pref_question import pref_location
from typing import Any, Dict, List, Tuple, Optional, Union # This is for type hints

# Union: Allows you to specify multiple types for a variable.
# For example, Union[int, str] means the variable can be an integer or a string.
from werkzeug.wrappers import Response as WerkzeugResponse

from pref_question import pref_location

#Make a Flask instance
app = Flask(__name__)

 # Make a random value with a parameter
key = os.urandom(21) 
app.secret_key = key # This will be a secret key to hold user session. 

#Make a dictionary Key, user ID : value, password
id_pwd: Dict[str, str] = {"lelouch" : "vermillioin"}

#Assuming it is a "main" function
# "/" indicates URL path
#Default is http://127.0.0.1:5000
@app.route("/")
#The redirect function actually returns an instance of werkzeug.wrappers.response.Response
# Supposed to return the rendered HTML template as a string or WerkzeugResponse
def index() -> Union[str, WerkzeugResponse]:
    # Session is a special object provided by Flask as login status
    # between different HTTP requests, across the entire session of a user’s interaction with your web application.
    # It allows you to store information specific to a user across different requests.
    if not session.get("login"):
        return redirect(url_for("login"))
    else:
        return render_template("index.html")

@app.route("/login")
def login() -> Union[str, WerkzeugResponse]:

	# Supposed to return the rendered HTML template as a string
	return render_template('login.html')

# Login authentication
# The function returns either string (a URL) or a Flask"Response" object
@app.route("/logincheck", methods=["POST"])
def logincheck() -> Union[str, WerkzeugResponse]:
    user_id: str = request.form.get("user_id", "")
    password: str = request.form.get("password", "")

    if user_id in id_pwd and password == id_pwd.get(user_id):
        session["login"] = True
    else:
        session["login"] = False

    # The url_for function takes the name of a view function
    # (i.e., the function that is decorated with @app.route) and
    # returns the corresponding URL for that function.
    if session["login"]:
        return redirect(url_for("index"))
    else:
        return redirect(url_for("login"))

@app.route("/pref_quiz", methods=["GET", "POST"])
def pref_quiz() -> Union[str, WerkzeugResponse]:
    random_pref: str
    city_name: str
    pref_url: str

    random_pref, city_name, pref_url = pref_location()
    #Store to session for using other pages
    session["prefecture"] = random_pref
    session["city"] = city_name
    session["url"] = pref_url
    # sending prefecture name to quiz.html and it will display {{prefecture}}
    return render_template("quiz.html", prefecture=random_pref)

@app.route("/answercheck", methods=["POST"])
def answercheck() -> Union[str, WerkzeugResponse]:
    user_answer: str = request.form['city']
    prefecture: str =  session.get('prefecture')
    city: str = session.get('city')
    url: str = session.get('url')

    if user_answer == city:
        result: str = "Correct!"
    else:
        result: str = "Wrong!"
    return render_template("result.html", result=result, prefecture=prefecture, city=city, url=url)



#Launch this app
if __name__ == "__main__":
    # print("Starting minimal Flask app...")
    # print(app.url_map)
    app.run(debug=True)