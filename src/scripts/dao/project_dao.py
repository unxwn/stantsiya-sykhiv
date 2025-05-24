class ProjectDAO:
    def __init__(self, db):
        self.db = db

    def create_project(self, title, description, owner_id):
        query = "INSERT INTO Project (title, description, owner_id) VALUES (%s, %s, %s)"
        self.db.cursor.execute(query, (title, description, owner_id))
        self.db.commit()

    def get_projects_by_owner(self, owner_id):
        query = "SELECT * FROM Project WHERE owner_id = %s"
        self.db.cursor.execute(query, (owner_id,))
        return self.db.cursor.fetchall()
