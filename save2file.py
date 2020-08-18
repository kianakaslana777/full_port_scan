import openpyxl
from info import Info


def create():
    s = Info("create sheet")
    s.out_start()
    wb = openpyxl.Workbook()
    sheet = wb.active

    sheet['A1'] = "IP"
    sheet['B1'] = "端口"
    sheet['C1'] = "端口状态"
    sheet['D1'] = "服务"
    sheet['E1'] = "服务版本"

    wb.save("full_port_scan_result.xlsx")
    s.out_end()


def load_sheet():
    s = Info("load sheet")
    s.out_start()
    wb = openpyxl.load_workbook("full_port_scan_result.xlsx")
    s.out_end()
    return wb


def write2excel(ip, ports):
    s = Info("save {} result to XLSX".format(ip))
    s.out_start()
    wb = load_sheet()
    sheet = wb.active
    cols = []
    for i in ports:
        col = [ip, i[0], i[1], i[2], i[3]]
        cols.append(col)
    try:
        for i in cols:
            print(i)
            sheet.append(i)
            wb.save('full_port_scan_result.xlsx')
    except BaseException as e:
        print(e)
        sheet.append('扫描{}时发生了未预料到的异常{}'.format(ip, '\n'))
        wb.save('full_port_scan_result.xlsx')
    else:
        s.out_end()


def write2txt(ip, ports):
    s = Info("save {} result to TXT".format(ip))
    s.out_start()
    try:
        with open('full_port_result.txt', 'a') as f:
            f.write('{}{}'.format(ip, ':\n'))
            for i in ports:
                f.write('{}{}{}'.format('\t', i, '\n'))
            f.write('\n')
            f.close()
    except BaseException as e:
        print(e)
        with open('full_port_result.txt', 'a') as f:
            f.write("扫描{}时，出现了未预料的异常{}".format(ip, '\n'))
    else:
        s.out_end()


if __name__ == '__main__':
    ip = '127.0.0.1'
    ports = [['22', 'open', 'ssh', ''], ['23', 'open', 'telnet', '1.1']]
    write2excel(ip, ports)
