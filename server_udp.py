import socket

socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口
socket.bind(('127.0.0.1',9999))
print('Bind UDP on 9999')
while True:
    #接收数据
    data,addr = socket.recvfrom(1024)
    print('Received from %s:%s' % addr)
    socket.sendto(b'Hello,%s!' % data,addr)
    