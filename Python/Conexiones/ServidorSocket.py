import socket


class ServidorSocket:
    DIRECCION = "192.168.0.115"
    PUERTO = 65440

    def __init__(self):
        print("Dentro del servidor")
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.bind((self.DIRECCION, self.PUERTO))
        servidor.listen(0)
        print(f"Escuchando en la dirección {self.DIRECCION} : {self.PUERTO}")

        cliente_socket, cliente_direccion = servidor.accept()
        print(f"Aceptando conexión de : {cliente_direccion[0]}:{cliente_direccion[1]}")

        while True:
            request = cliente_socket.recv(20)
            request = request.decode("utf-8")

            if request.lower() == "cerrar":
                cliente_socket.send("cerrada".encode("utf-8"))
                break

            print(f"recibido: {request}")
            response = "aceptada".encode("utf-8")
            cliente_socket.send(response)

            texto = input("Escribe algo")
            cliente_socket.send(texto.encode("utf-8"))

        cliente_socket.close()
        print("Conexión cerrada")
def main():
    servidor = ServidorSocket()

if __name__ == "__main__":
    main()