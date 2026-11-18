import sqlite3, time
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "metrics.db"


def get_connection():
    DB_PATH.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)

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

    db.commit()
    db.close()

def save(cpu, memory, disk, net_recov, net_sent):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    db = get_connection()
    c = db.cursor()

    c.execute("INSERT INTO logs VALUES (?, ?, ?, ?, ?, ?)",
               (now, cpu, net_recov, net_sent, memory, disk))
    db.commit()
    db.close()


if __name__ == "__main__":
    init_db()
    print("Create table", DB_PATH)