import socket
import binascii
import time
data_raw = ""

def raw_format(data):
    return binascii.unhexlify(data)  # Convierte la cadena hexadecimal en bytes

UDP_IP = "192.168.100.253" # ip panel led 
UDP_PORT = 6101
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = raw_format(data_raw)
bytes_enviados = sock.sendto(data, (UDP_IP, UDP_PORT))
print(f"Enviado {bytes_enviados} bytes a {UDP_IP}:{UDP_PORT}")

