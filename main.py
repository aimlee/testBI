import threading
import sqlite3
import dbapp

createStatus = """ CREATE TABLE status (
            AppID INT NOT NULL,
            
            StatusCode CHAR(25)
        ); """

sqlcon = sqlite3.connect('jdbc:sqlite:identifier.sqlite')
mycur = sqlcon.cursor()
#mycur.execute(createStatus)

# Тут вызываем запрос который писали в задание2 и добавляем статус в новым таблице где храняется статус запроса
def check_status():
    try:
        values = dbapp.appcheck()
        for val in values:
            mycur.execute(f'INSERT INTO status (AppID, StatusCode) VALUES {val}')
            sqlcon.commit()
    except sqlite3.Error as error:
        print("\033[91m Error in", error)
    finally:
        sqlcon.close()

# Проеверять таблицу с статусами
def check_db():
    try:
        sqlcon = sqlite3.connect('jdbc:sqlite:identifier.sqlite')
        mycur = sqlcon.cursor()
        mycur.execute(f'SELECT * FROM status')
        return mycur.fetchall()
    except sqlite3.Error as error:
        print("\033[91m Error in", error)
    finally:
        sqlcon.close()

# Пока открыто приложение он будет через каждый 5 секуд проверить статус
while True:
    start_time = threading.Timer(5, check_status)
    start_time.start()
