from concurrent.futures.thread import ThreadPoolExecutor
import nmap
from info import Info
from save2file import write2excel, write2txt, create

max_threads = 5


def scan(ip):
    s = Info("scan {}".format(ip))
    s.out_start()
    nm = nmap.PortScanner()
    nm.scan(ip, '0-65535', '-T4, -Pn, -sV')
    print(nm[ip]['tcp'])
    r = nm[ip]['tcp']
    ports = []
    excel_ports = []
    create()
    for i in r:
        ports.append(
            "{:^15s}{:^15s}{:^15s}{:^15s}".format(str(i), r[i]['state'], r[i]['name'], r[i]['version']))
        excel_ports.append(
            [str(i), r[i]['state'], r[i]['name'], r[i]['version']])
    print(ip)
    write2txt(ip, ports)
    write2excel(ip, excel_ports)
    s.out_end()


def read_txt():
    s = Info("read ip_list")
    s.out_start()
    ip_list = []
    with open('up_host.txt', 'r') as f:
        for i in f.readlines():
            ip_list.append(i.rstrip("\n"))
    f.close()
    s.out_end()
    return ip_list


if __name__ == '__main__':
    ip_list = read_txt()
    with ThreadPoolExecutor(max_workers=max_threads) as t:
        all_task = [t.submit(scan, i) for i in ip_list]
        # wait(all_task, timeout=180)
    print("{:^20s}".format('all scan completed!'))
    # scan('10.211.55.18')
