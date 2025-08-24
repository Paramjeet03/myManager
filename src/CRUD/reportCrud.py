from src.Database.session import localSession
from src.Database.db_model import User_table,Task_table

def report_db():
    db=localSession()
    Total_account=db.query(User_table.email).count()
    Total_user=db.query(User_table.email).filter(User_table.role != "admin").count()
    Total_Done=db.query(Task_table).filter(Task_table.status == "done").count()
    Total_task=db.query(Task_table).count()
    Total_pending=db.query(Task_table).filter(Task_table.status != "done" and Task_table.status != "start" and Task_table.status != "given" ).count()
    return {"Total_account":Total_account,"Total_user":Total_user,"Total_admin":Total_account-Total_user,"Total_Done_project":Total_Done,"Total_task":Total_task,"Total_pending":Total_pending}
