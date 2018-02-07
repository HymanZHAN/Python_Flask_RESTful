import sqlite3
from flask_restful import Resource, reqparse


class User:
    def __init__(self, user_id, username, password):
        self.id = user_id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        # execute action has to use tuple data type
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, user_id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        # execute action has to use tuple data type
        result = cursor.execute(query, (user_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user


class UserRegister(Resource):

    # Define parser for registration arguments
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True,
                        help="User name cannot be blank!")
    parser.add_argument('password', type=str, required=True,
                        help="Password cannot be blank!")

    def post(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {"message": "Username has already been used!"}

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()
        return {"message": "User created succesfully."}, 201
