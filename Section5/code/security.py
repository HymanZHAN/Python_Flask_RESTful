from user import User
# users is a list of dictionaries


def authenticate(username, password):
    user = User.find_by_username(username)
    if user and password == user.password:
        # If user exists and the password matches, return user
        return user


def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
