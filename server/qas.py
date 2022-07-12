# 该脚本为服务端响应程序

import socket
import datetime

# 创建socket对象

# AF_INIT     ipv4 协议
# SOCK_DGRAM  udp  模式
port = 9001
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

sock.bind(('', port))    # 绑定 ip/端口
sock.settimeout(1.0)     # 接收超时

print("------ QAS Start ------")
print("port: ", port)
print("time: ", datetime.datetime.now())

while(True):
    try:
        data, addr = sock.recvfrom(1024)
        if data.decode() == "miscoco":             # 得到寻呼口令
            sock.sendto("success".encode(), addr)  # 应答
            print(datetime.datetime.now(), addr)   # 记录

    except socket.timeout:
        pass

sock.close()
