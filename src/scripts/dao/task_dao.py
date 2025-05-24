class TaskDAO:
    def __init__(self, db):
        self.db = db

    def create_task(self, title, description, start_date, end_date, status, project_id, assignee_id=None):
        query = "INSERT INTO Task (title, description, start_date, end_date, status, project_id, assignee_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.db.cursor.execute(query, (title, description, start_date, end_date, status, project_id, assignee_id))
        self.db.commit()
