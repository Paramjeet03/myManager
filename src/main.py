from fastapi import FastAPI
from src.api  import Welcome,login,createAccount,update,report,deleteAccount,readAccount,get_all_api,personal_account
from src.api  import taskAssign,taskUpdate,seeTask,taskDeletion,adminGetAlltask,see_task_by_mail
from src.api import setLog,getLogadmin,getlogUser,updateLog,getalllogadm
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(Welcome.router,prefix="/Welcome",tags=["Welcome"])
app.include_router(login.router,prefix="/login",tags=["Login"])


app.include_router(createAccount.router,prefix="/Admin/createAccount",tags=["Account CRUD"])
app.include_router(update.router,prefix="/Admin/updateAccount",tags=["Account CRUD"])
app.include_router(deleteAccount.router,prefix="/Admin/deleteAccount",tags=["Account CRUD"])
app.include_router(readAccount.router,prefix="/Admin/seeAccount",tags=["Account CRUD"])
app.include_router(get_all_api.router,prefix="/Admin_get_all/seeAccount",tags=["Account CRUD"])
app.include_router(personal_account.router,prefix="/user/seeAccount",tags=["Account CRUD"])


app.include_router(taskAssign.router,prefix="/Admin/assignTask",tags=["Task CRUD"])
app.include_router(seeTask.router,prefix="/User/seeTask",tags=["Task CRUD"])
app.include_router(taskUpdate.router,prefix="/Admin/taskUpdate",tags=["Task CRUD"])
app.include_router(taskDeletion.router,prefix="/Admin/task_deletion",tags=["Task CRUD"])
app.include_router(adminGetAlltask.router,prefix="/Admin/Get_all",tags=["Task CRUD"])
app.include_router(see_task_by_mail.router,prefix="/Admin/Get_all_by_mail",tags=["Task CRUD"])

app.include_router(setLog.router,prefix="/User/addLog",tags=["Log Crud"])
app.include_router(getLogadmin.router,prefix="/Admin/getLog",tags=["Log Crud"])
app.include_router(getlogUser.router,prefix="/User/getLog",tags=["Log Crud"])
app.include_router(updateLog.router,prefix="/User/updateLog",tags=["Log Crud"])
app.include_router(getalllogadm.router,prefix="/admin/getAllLog",tags=["Log Crud"])


app.include_router(report.router,prefix="/totalReport",tags=["Report"])
