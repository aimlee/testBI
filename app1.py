from fastapi import FastAPI

app = FastAPI()

# Первая приложение который возвращает его имя и адрес
@app.get("/get_app1")
def read_root():
    return {
        "AppId": 1,
        "AppName": "First app",
        "PublishedPlace": "Almaty"
    }
