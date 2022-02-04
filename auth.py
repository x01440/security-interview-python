from lib2to3.pgen2.token import OP


SECRET_KEY = "123456"
ROLE_ADMIN = "admin"
ROLE_EDITOR = "editor"
ROLE_USER = "user"
OPERATION_READ = "GET"
OPERATION_CREATE = "POST"
OPERATION_UPDATE = "PUT"

AUTHORIZATION_CREDS = {
    ROLE_ADMIN: [OPERATION_READ, OPERATION_CREATE, OPERATION_UPDATE],
    ROLE_EDITOR: [OPERATION_READ, OPERATION_UPDATE],
    ROLE_USER: [OPERATION_READ]
}

def create_key():
    return SECRET_KEY

def check_key(candidate_key: str):
    if candidate_key == SECRET_KEY:
        return True
    else:
        return False

def check_role(candidate_role: str, operation: str):
    if candidate_role == None:
        return False
    if operation in AUTHORIZATION_CREDS[candidate_role]:
        return True
    else:
        return False
