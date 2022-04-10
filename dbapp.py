import sqlite3
import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Создаем БД для хранение все приложение
createSQL = """ CREATE TABLE AUTOREQ (
            AppID INT NOT NULL,
            AppNAME CHAR(25) NOT NULL,
            PublishAddress CHAR(25)
        ); """
# Запрос для проверки ДБ с приложенями
getItemSQL = "SELECT * FROM AUTOREQ ORDER BY AppID"
getSQLAddress = "SELECT AppID, PublishAddress FROM AUTOREQ"


class PostItems(BaseModel):
    AppId: int
    AppName: str
    PublishedPlace: str


# Создаем ДБ локально
@app.get("/create")
def createdb():
    try:
        sqlcon = sqlite3.connect('jdbc:sqlite:identifier.sqlite')
        mycur = sqlcon.cursor()
        mycur.execute(createSQL)
    except sqlite3.Error as error:
        print("\033[91m Error while connecting to sqlite", error)
    finally:
        sqlcon.close()


# Проверяем что есть в ДБ
@app.get("/item")
def read_root():
    try:
        sqlcon = sqlite3.connect('jdbc:sqlite:identifier.sqlite')
        mycur = sqlcon.cursor()
        mycur.execute(getItemSQL)
        return mycur.fetchall()
    except sqlite3.Error as error:
        print("\033[91m Error while connecting to sqlite", error)
    finally:
        sqlcon.close()


# Сохранить первый приложения в ДБ
@app.get("/addapp1db")
def app1():
    try:
        sqlcon = sqlite3.connect('jdbc:sqlite:identifier.sqlite')
        mycur = sqlcon.cursor()
        app = "http://0.0.0.0:8081/get_app1"
        r = requests.get(url=app)
        data = r.json()
        val = (data['AppId'], data['AppName'], app)
        mycur.execute(f'INSERT INTO AUTOREQ (AppID, AppNAME, PublishAddress) VALUES {val}')
    except sqlite3.Error as error:
        print("\033[91m Error while connecting to sqlite", error)
    else:
        sqlcon.commit()
    finally:
        sqlcon.close()


# Сохранить второй приложения в ДБ
@app.get("/addapp2db")
def app2():
    try:
        sqlcon = sqlite3.connect('jdbc:sqlite:identifier.sqlite')
        mycur = sqlcon.cursor()
        app = "http://0.0.0.0:8080/get_app2"
        r = requests.get(url=app)
        data = r.json()
        val = (data['AppId'], data['AppName'], app)
        mycur.execute(f'INSERT INTO AUTOREQ (AppID, AppNAME, PublishAddress) VALUES {val}')
    except sqlite3.Error as error:
        print("\033[91m Error while connecting to sqlite", error)
    else:
        sqlcon.commit()
    finally:
        sqlcon.close()


# Взять адрес с БД и проверять каждый адрес на статус
@app.get("/checkapp")
def appcheck():
    try:
        sqlcon = sqlite3.connect('jdbc:sqlite:identifier.sqlite')
        mycur = sqlcon.cursor()
        mycur.execute(getSQLAddress)
        app_address = mycur.fetchall()
        ans = []
        for address in app_address:
            r = requests.get(url=address[1])
            ans.append((address[0], r.status_code))
        return ans
    except sqlite3.Error as error:
        print("\033[91m Error while connecting to sqlite", error)


# Обычный пост запрос что бы проверить и добавить запись в ДБ
@app.post("/addtodb")
async def create_post(item: PostItems):
    try:
        sqlcon = sqlite3.connect('jdbc:sqlite:identifier.sqlite')
        mycur = sqlcon.cursor()
        val = (int(item.AppId), str(item.AppName), str(item.PublishedPlace))
        mycur.execute(f'INSERT INTO AUTOREQ (AppID, AppNAME, PublishAddress) VALUES {val}')
    except sqlite3.Error as error:
        print("\033[91m Error while connecting to sqlite", error)
    else:
        sqlcon.commit()
    finally:
        sqlcon.close()
