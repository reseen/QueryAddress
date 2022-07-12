# 该脚本为客户端响应程序
import sys
import socket
import datetime


hostFile = "C:\\Windows\\System32\\drivers\\etc\\hosts"
hostBack = "C:\\Windows\\System32\\drivers\\etc\\hosts.qac.bak"


# 写日志
def logWrite(msg):
    path = sys.argv[0].replace('qac.py', 'qac.log')
    print(msg)
    with open(path, 'a+') as fp:
        fp.write('%s\n' % msg)
        fp.close()


# 获取时间
def getTime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


# 修改Host文件
def modifyHosts(ip):
    # 先检测服务器IP是否发生改变
    with open(hostFile, 'r') as fr:
        dt = fr.readlines()
        if "%s termux.miscoco.com" % ip in dt:
            logWrite("%s server ip no change" % getTime())
            return

    # 备份HOSTS
    with open(hostFile, 'rb') as fr, open(hostBack, 'wb') as fw:
        fw.write(fr.read())

    # 写新的HOSTS
    with open(hostBack, 'r') as fr, open(hostFile, 'w') as fw:
        dt = fr.readlines()
        for li in dt:
            if 'termux.miscoco.com' in li:
                continue
            fw.write(li)
        fw.write("%s termux.miscoco.com" % ip)
        logWrite("%s hosts file update [tag]" % getTime())


# 检测服务器
def checkServer():
    host = socket.gethostname()
    ip = socket.gethostbyname(host).split('.')
    ip[3] = '255'
    cast = '.'.join(ip)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(3.0)
    sock.sendto("miscoco".encode(), (cast, 9001))

    try:
        data, addr = sock.recvfrom(1024)
        if data.decode() == "success":
            modifyHosts(addr[0])

    except socket.timeout:
        logWrite("%s timeout" % getTime())

    sock.close()


if __name__ == "__main__":
    checkServer()
