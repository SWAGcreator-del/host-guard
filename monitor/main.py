from monitor.collectors import get_cpu, get_diskUsed, get_memory, net_stat
from monitor.storage import init_db, save, get_sample, clean_logs, read_alerts, delete_old_alerts, add_last_alert
from monitor.checker import check_load
from monitor.bot import send
TEXTS = {
    "cpu": "CPU ПЕРЕГРУЖЕН!",
    "ram": "Утечка памяти!",
    "netSent": "Отправляется слишком много данных!",
    "netRecv": "Возможна DDOS атака!",
    "disk": "Хранилище переполнено!",
}
WINDOW_MINUTES = 15
COOLDOWN_MINUTES = 15
KEEP_HOURS = 2


init_db()
net_recv, net_sent = net_stat()
save(get_cpu(), get_memory(), get_diskUsed(), net_recv, net_sent)
problems = (check_load(get_sample(WINDOW_MINUTES)))

def check_problems(problems):
    # получение старого alert
    recent = read_alerts(COOLDOWN_MINUTES)
    new = [p for p in problems if p not in recent]
    if not new:
        return

    text = "Серверу плохо, причины: " + " ".join(TEXTS[p] for p in new)
    send(text)
    add_last_alert(new)
check_problems(problems)
clean_logs(KEEP_HOURS)
delete_old_alerts(KEEP_HOURS)
        
