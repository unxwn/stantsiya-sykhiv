class ColumnDAO:
    def __init__(self, db):
        self.db = db

    def create_column(self, title, board_id, order):
        query = "INSERT INTO `Column` (title, board_id, `order`) VALUES (%s, %s, %s)"
        self.db.cursor.execute(query, (title, board_id, order))
        self.db.commit()
