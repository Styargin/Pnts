# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # For TCP use SOCK_STREAM
# s.bind(('0.0.0.0', 8888))  # Default s.bind(('127.0.0.1', 8888))
# result = s.recv(1024)
# print('Message:', result.decode('utf-8'))
# s.close()

# Ispol'zuem TCP

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8888))
s.listen(5)
while 1:
    try:
        client, addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        break
    else:
        result = client.recv(1024)
        print('Message:', result.decode('utf-8'))
