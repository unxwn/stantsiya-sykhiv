class CommentDAO:
    def __init__(self, db):
        self.db = db

    def create_comment(self, task_id, author_id, content, timestamp):
        query = "INSERT INTO Comment (task_id, author_id, content, timestamp) VALUES (%s, %s, %s, %s)"
        self.db.cursor.execute(query, (task_id, author_id, content, timestamp))
        self.db.commit()
