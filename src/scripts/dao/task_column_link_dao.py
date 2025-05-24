class TaskColumnLinkDAO:
    def __init__(self, db):
        self.db = db

    def link_task_to_column(self, task_id, column_id):
        query = "INSERT INTO TaskColumnLink (task_id, column_id) VALUES (%s, %s)"
        self.db.cursor.execute(query, (task_id, column_id))
        self.db.commit()
