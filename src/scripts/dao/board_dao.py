class BoardDAO:
    def __init__(self, db):
        self.db = db

    def create_board(self, title, project_id):
        query = "INSERT INTO Board (title, project_id) VALUES (%s, %s)"
        self.db.cursor.execute(query, (title, project_id))
        self.db.commit()
