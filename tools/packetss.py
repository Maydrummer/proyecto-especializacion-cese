import socket
import time 

online_packet =  b"\x48\x54\x00\x1B\x00\x1F\x05"+ b"\x00" * 19 + b"\x01\x00\x00\xDC\xAA"

UDP_IP = "192.168.100.253" # ip panel led 
UDP_PORT = 6101


def digit_packet(integer: int, decimal: int) -> bytes:
    if integer > 0xFFFFFFFF or integer < 0:
        raise ValueError(f"integer part out of limits")
    if decimal > 0xFFFFFFFF or decimal < 0:
        raise ValueError(f"decimal part out of limits")
    packet = b"\x48\x54\x00\x1B\x00\x29\x24" + b"\x00" * 19 + b"\x01\x0B\x02"
    packet += integer.to_bytes(4, "big") + decimal.to_bytes(4, "big")
    packet += (sum(packet) & 0xFFFFFF).to_bytes(3, "big") + b"\xAA"
    return bytes(packet)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Paquete a enviar
num = 19
dec = 1
data = digit_packet(num, dec)

print(num.to_bytes(4, "big"))
print(dec.to_bytes(4, "big"))
while True:
    try:
        # Enviar datos por UDP
        bytes_enviados = sock.sendto(data, (UDP_IP, UDP_PORT))
        print(f"Enviado {bytes_enviados} bytes a {UDP_IP}:{UDP_PORT}")
        time.sleep(5)
    except KeyboardInterrupt:
        print("\nCerrando socket...")
        sock.close()
        break
    except Exception as e:
        print(f"Error: {e}")