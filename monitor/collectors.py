import psutil, time, sqlite3
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "metrics.db"

GB = 1024 ** 3

#---- фукнции для отслеживания статистики
def get_diskUsed():
    return str(psutil.disk_usage('/').used / GB)[:3]

def get_memory():
    return str(psutil.virtual_memory().used / GB)[:3]

def net_stat():
    net_before = psutil.net_io_counters()
    time.sleep(1)
    net_after = psutil.net_io_counters()

    bytes_recv = net_after.bytes_recv - net_before.bytes_recv
    bytes_sent = net_after.bytes_sent - net_before.bytes_sent

    mbps_recv = (bytes_recv * 8) / 1_000_000
    mbps_sent = (bytes_sent * 8) / 1_000_000

    return mbps_recv, mbps_sent
def get_cpu():
    return psutil.cpu_percent(interval=1)

#---- проверка на существование пути и создание логов

db = sqlite3.connect("log.db")

with open("/var/log/host-guard", "a") as log:
    log.write(f"{time.ctime()} \n--------------------------- \n")
    log.write(f"cpu = {get_cpu()} \n")
    log.write(f"memory = {get_memory()} \n")
    log.write(f"disk = {get_diskUsed()} \n")
    log.write(f"net = {net_stat()} \n")
    log.write("--------------------------- \n\n\n")

