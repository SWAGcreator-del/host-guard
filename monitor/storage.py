import sqlite3, time
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent # resolve делает путь обсолютным
DB_PATH = BASE_DIR / "data" / "metrics.db" # / используется для склейки путей

# конектимся по пути
def get_connection():
    DB_PATH.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)

# создаем базу данных
def init_db():
    db = get_connection()
    c = db.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS logs (
        datetime text,
        cpu REAL,
        net_recv REAL,
        net_sent REAL,
        memory REAL,
        disk REAL
    )""")

    db.commit() # сохранить параметры
    db.close()

# Добавиление новых параметров 
def save(cpu, memory, disk, net_recov, net_sent):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    db = get_connection()
    c = db.cursor()

    c.execute("INSERT INTO logs VALUES (?, ?, ?, ?, ?, ?)",
               (now, cpu, net_recov, net_sent, memory, disk))
    db.commit()
    db.close()

# Получаем замеры
def get_sample(minutes):
    db = get_connection()
    c = db.cursor()
    border = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() - minutes * 60))
    c.execute("SELECT * FROM logs WHERE datetime > ?", (border,))
    res = c.fetchall()
    db.close()
    return res

# Тест
if __name__ == "__main__":
    init_db()
    print("Create table", DB_PATH)