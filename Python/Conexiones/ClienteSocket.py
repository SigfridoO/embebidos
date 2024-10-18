import socket


class ClienteSocket:
    DIRECCION = "192.168.0.100"
    PUERTO = 65432

    def __init__(self):
        print("Dentro del cliente")
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((self.DIRECCION, self.PUERTO))
        
        while True:
            mensaje = input("Escriba un mensaje: ")
            cliente.send(mensaje.encode("utf-8")[:1024])
            
            response = cliente.recv(1024)
            response = response.decode("utf-8")

            if response.lower() == "cerrada":
                break

            print(f"recibido: {response}")

        cliente.close()
        print("Conexión cerrada")
def main():
    cliente = ClienteSocket()

if __name__ == "__main__":
    main()