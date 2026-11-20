from monitor.collectors import get_cpu, get_diskUsed, get_memory, net_stat
from monitor.storage import init_db, save, get_sample, clean_logs
from monitor.checker import check_load

init_db()
net_recv, net_sent = net_stat()
save(get_cpu(), get_memory(), get_diskUsed(), net_recv, net_sent)
print(check_load(get_sample(15)))
