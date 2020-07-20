import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # For TCP use SOCK_STREAM
s.sendto(b'<Your message>', ('127.0.0.1', 8888))
