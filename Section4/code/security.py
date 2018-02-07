from user import User
# users is a list of dictionaries
users = [
    User(1, 'xucong', 'asdf')
]

# username_mapping is a dictionary with a username as the key
# and the user dictionary as the value
# i.e. mapping from 'username' to user dictionary object

# a key-value pair of u.username:u, where u is an item of the list 'users'
username_mapping = {u.username: u for u in users}
# mapping from 'userid' to a user dictionary object
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and password == user.password:
        # If user exists and the password matches, return user
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
