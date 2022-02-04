from flask import Flask, request

import sample_login
import user

# Security Interview
#
# Security Flaws:
# Guessable Authentication Key
# Same key for each login
# Role encoded in query string
# Config URL exposed for discovery
# API documentation exposed without key
# SQL query update without escaping web content

app = Flask(__name__)

METHOD_GET: str = 'GET'
METHOD_POST: str = 'POST'
METHOD_PUT: str = 'PUT'

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return sample_login.do_login()
    else:
        return sample_login.show_login_form()

@app.route('/user', methods=['GET', 'POST', 'PUT'])
def user_handler():
    # Check key and role.

    if request.method == METHOD_GET:
        return user.get_user()
    elif request.method == METHOD_POST:
        return user.create_user
    elif request.method == METHOD_PUT:
        return user.update_user
    else:
        return "<p>Invalid Request</p>"
