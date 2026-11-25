from monitor.collectors import get_cpu, get_diskUsed, get_memory, net_stat
from monitor.storage import init_db, save, get_sample, clean_logs
from monitor.checker import check_load
from monitor.bot import send
clean_logs(0)
init_db()
net_recv, net_sent = net_stat()
save(get_cpu(), get_memory(), get_diskUsed(), net_recv, net_sent)
problems = (check_load(get_sample(15)))

def check_problems(problems):
    errormesange = "Серверу плохо, причины:"
    for i in problems:
        if i == "cpu":
            errormesange += " CPU ПЕРЕГРУЖЕН!"
        if i == "ram":
            errormesange += " Утечка памяти!"
        if i == "netSent":
            errormesange += " Отправляется слишком много данных!"
        if i == "netRecv":
            errormesange += " Возможна DDOS атака!"
        if i == "disk":
            errormesange += " Хранилище переполнено!"
    if errormesange == "Серверу плохо, причины:":
        pass
    else:
        return send(errormesange)
check_problems(problems)
        
