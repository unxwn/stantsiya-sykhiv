from database import Database
from dao.user_dao import UserDAO
from dao.project_dao import ProjectDAO
from dao.board_dao import BoardDAO
from dao.column_dao import ColumnDAO
from dao.task_dao import TaskDAO
from dao.task_column_link_dao import TaskColumnLinkDAO
from dao.comment_dao import CommentDAO
from datetime import datetime

def main():
    db = Database()

    user_dao = UserDAO(db)
    project_dao = ProjectDAO(db)
    board_dao = BoardDAO(db)
    column_dao = ColumnDAO(db)
    task_dao = TaskDAO(db)
    task_column_link_dao = TaskColumnLinkDAO(db)
    comment_dao = CommentDAO(db)

    # Create user
    user_dao.create_user("Vatroslav", "vatroslav@example.com", "password123")
    user = user_dao.get_user_by_username("Vatroslav")

    # Create project
    project_dao.create_project("Project A", "Description of Project A", user["id"])

    # Get project
    projects = project_dao.get_projects_by_owner(user["id"])
    project_id = projects[0]["id"]

    # Create board
    board_dao.create_board("Board A", project_id)

    # Create column
    column_dao.create_column("To Do", 1, 1)

    # Create task
    task_dao.create_task("Task 1", "Do something", "2024-05-01", "2024-05-10", "Open", project_id, user["id"])

    # Link task to column
    task_column_link_dao.link_task_to_column(1, 1)

    # Add comment
    comment_dao.create_comment(1, user["id"], "Looks good", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    db.close()

if __name__ == "__main__":
    main()
