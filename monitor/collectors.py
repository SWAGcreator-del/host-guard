import psutil, time


GB = 1024 ** 3

#---- фукнции для отслеживания статистики
def get_diskUsed():
    return round(psutil.disk_usage('/').used / GB, 2)

def get_memory():
    return round(psutil.virtual_memory().used / GB, 2)

def net_stat():
    net_before = psutil.net_io_counters()
    time.sleep(1)
    net_after = psutil.net_io_counters()

    bytes_recv = net_after.bytes_recv - net_before.bytes_recv
    bytes_sent = net_after.bytes_sent - net_before.bytes_sent

    mbps_recv = (bytes_recv * 8) / 1_000_000
    mbps_sent = (bytes_sent * 8) / 1_000_000

    return round(mbps_recv, 2), round(mbps_sent, 2)


def get_cpu():
    return psutil.cpu_percent(interval=1)

def test():
    print(f"cpu = {get_cpu()}")
    print(f"memory = {get_memory()}")
    print(f"net = {net_stat()}")
    print(f"disk = {get_diskUsed()}")


if __name__ == "__main__":
    test()
