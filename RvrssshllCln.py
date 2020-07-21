# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # For TCP use SOCK_STREAM
# s.sendto(b'<Your message>', ('192.168.0.1', 8888))  # Default s.sendto(b'<Your message>', ('127.0.0.1', 8888))

# Ispol'zuem TCP

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.11', 8888))  # Default s.connect(('127.0.0.1', 8888))
s.send(b'<YOUR MESSAGE>')
s.close()