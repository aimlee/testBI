from fastapi import FastAPI

app = FastAPI()

# Вторая приложение который возвращает его имя и адрес
@app.get("/get_app2")
def read_root():
    return{"AppId": 2,
           "AppName": "Second app",
           "PublishedPlace": "Nur-Sultan"}