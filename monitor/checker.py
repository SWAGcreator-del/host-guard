CPU, NET_RECV, NET_SENT, MEMORY, DISK = 80.0, 12.95, 12.95, 50.0, 450.0
def check_load(load):
    # Проверка на достаточное количество логов
    if len(load) < 10:
        return []
    
    check_cpu = 0
    check_netrecv = 0
    check_netsent = 0
    check_memory = 0
    check_disk = 0

    # Параметры проверки
    for l in load:
        _, cpu, net_recv, net_sent, ram, disk = l
        if cpu > CPU:
            check_cpu += 1
        if net_recv > NET_RECV:
            check_netrecv += 1
        if net_sent > NET_SENT:
            check_netsent += 1
        if ram > MEMORY:
            check_memory += 1
        if disk > DISK:
            check_disk += 1

    # Нахождение проблем, после подсчета
    problems = []
    if check_cpu == len(load):
        problems.append("cpu")
    if check_memory == len(load):
        problems.append("ram")
    if check_netsent == len(load):
        problems.append("netSent")
    if check_netrecv == len(load):
        problems.append("netRecv")
    if check_disk == len(load):
        problems.append("disk")
    return problems

if __name__ == "__main__":
    test = [("t", 10, 0, 0, 6, 540)] * 15 # тестик хпхппх запускать без флага -m
    print(check_load(test))        




