def do_login():
    return "<p>Successfully Logged In!</p>"

def show_login_form():
    response: str = "<div>"
    response += '''<form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
            </form>'''
    response += "</div>"
    return response
