class UserDAO:
    def __init__(self, db):
        self.db = db

    def create_user(self, username, email, password_hash):
        query = "INSERT INTO User (username, email, passwordHash) VALUES (%s, %s, %s)"
        self.db.cursor.execute(query, (username, email, password_hash))
        self.db.commit()

    def get_user_by_username(self, username):
        query = "SELECT * FROM User WHERE username = %s"
        self.db.cursor.execute(query, (username,))
        return self.db.cursor.fetchone()
