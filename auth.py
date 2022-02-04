SECRET_KEY = "123456"
ROLE_ADMIN = "admin"
ROLE_EDITOR = "editor"
ROLE_USER = "user"

def create_key():
    return SECRET_KEY

def check_key(candidate_key: str):
    if candidate_key == SECRET_KEY:
        return True
    else:
        return False

def check_role(candidate_role: str):
    if candidate_role == ROLE_ADMIN:
        return ROLE_ADMIN
    elif candidate_role == ROLE_EDITOR:
        return ROLE_EDITOR
    elif candidate_role == ROLE_USER:
        return ROLE_USER
    else:
        return None