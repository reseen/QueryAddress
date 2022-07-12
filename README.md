# QueryAddress
Client 通过 UDP 广播查找 Server IP 地址

## Server
qas.py 服务端程序

## Clicnt
qac.py 客户端程序

## 用法
在 termux 中通过 qas.sh 启动服务。

客户端在 windows 中使用 robointern 进行周期性查询，当服务端IP地址改变时，qac.py 修改客户端 hosts 文件。
