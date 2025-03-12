import socket

def to_hex(data: bytes):
    return "".join(f"{x:02X}" for x in data)

UDP_IP = "192.168.100.2" # Escucha en todas las interfaces de red
UDP_PORT = 6101

# Crear socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Escuchando tráfico UDP en {UDP_IP}:{UDP_PORT}...\n")

while True:
    try:
        data, addr = sock.recvfrom(3000)
        #print(f"Mensaje recibido en bytes → {data}")
        hex_data = to_hex(data)
        print(f"Mensaje recibido, N bytes : {len(data)} hex → {hex_data}")
    except KeyboardInterrupt:
        print("\nCerrando socket...")
        sock.close()
        break
    except Exception as e:
        print(f"Error: {e}")
