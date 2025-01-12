from fastapi import FastAPI
from routers import task, user

# Приложение(объект) FastAPI
app = FastAPI()

# маршрут для app - '/', по которому функция возвращает словарь
@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

# Импорт объектов APIRouter и подключение к ранее созданному
# приложению FastAPI, объединив все маршруты в одно приложение.
app.include_router(task.router)
app.include_router(user.router)