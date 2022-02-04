from flask import Flask, make_response, request

import auth
import sample_login
import user

# Security Interview
#
# Usage
# Security key in header value "Auth" for API access
# Use the query string param "role" to specify role for operation.
#   Valid roles are: admin, editor, user
#   admin can do all operations
#   editor can do update and read
#   user can do read

app = Flask(__name__)

METHOD_GET: str = 'GET'
METHOD_POST: str = 'POST'
METHOD_PUT: str = 'PUT'
RESPONSE_MESSAGE: str = 'message'

@app.route("/")
def hello_world():
    return '<p>Sample User Service</p>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return sample_login.do_login()
    else:
        return sample_login.show_login_form()

@app.route('/key', methods=['POST'])
def generate_key():
    return auth.create_key

@app.route('/user', methods=['GET', 'POST', 'PUT'])
def user_handler():
    # Check key and role.
    auth_key = extract_auth_key(request)
    if not auth.check_key(auth_key):
        return make_response({RESPONSE_MESSAGE: 'Authentication failed'}, 403)
    user_role = request.args.get('role', '')

    if request.method == METHOD_GET:
        if auth.check_role(user_role, METHOD_GET):
            return user.get_user()
        else:
            return return_forbidden()
    elif request.method == METHOD_POST:
        if auth.check_role(user_role, METHOD_GET):
            return user.create_user()
        else:
            return return_forbidden()
    elif request.method == METHOD_PUT:
        if auth.check_role(user_role, METHOD_GET):
            return user.update_user()
        else:
            return return_forbidden()
    else:
        response = make_response({RESPONSE_MESSAGE: 'Method not allowed'}, 405)
        return response

def extract_auth_key(req: request):
    return req.headers['Auth'] if req.headers.has_key('Auth') else None

def return_forbidden():
    return make_response({RESPONSE_MESSAGE: 'Authentication failed'}, 403)