import sqlite3


class UserModel:
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
