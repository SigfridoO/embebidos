import socket
import threading

class ServidorSocket:
    DIRECCION = "192.168.0.115"
    PUERTO = 65440

    def __init__(self):
        print("Dentro del servidor")
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor.bind((self.DIRECCION, self.PUERTO))
        self.servidor.listen(0)

        self.cliente_socket = None
        self.iniciar_conexiones()
        
    # def simulador_datos(self):
    #     contador = 0
    #     while True:
    #         if self.cliente_socket and self.cliente_socket.
    def iniciar_conexiones(self):
        print(f"Escuchando en la dirección {self.DIRECCION} : {self.PUERTO}")

        while True:
            self.cliente_socket, cliente_direccion = self.servidor.accept()
            tarea = threading.Thread(target=self.manejar_conexion, args=(self.cliente_socket, cliente_direccion))
            tarea.start()

    def manejar_conexion(self, cliente_socket, cliente_direccion):
        print(f"Aceptando conexión de : {cliente_direccion[0]}:{cliente_direccion[1]}")

        while True:
            try:
                request = cliente_socket.recv(20)
                request = request.decode("utf-8")

                if request.lower() == "cerrar":
                    cliente_socket.send("cerrada".encode("utf-8"))
                    break

                print(f"recibido: {request}")
                response = "aceptada".encode("utf-8")
                cliente_socket.send(response)

                # texto = input("Escribe algo")
                # cliente_socket.send(texto.encode("utf-8"))

            except Exception:
                print("Conexion Cerrada por el cliente")
                break

        cliente_socket.close()
        print("Conexión cerrada")

    def enviar_mensaje(self, cliente_socket, mensaje):
        cliente_socket.send(mensaje.encode("utf-8"))



def main():
    servidor = ServidorSocket()

if __name__ == "__main__":
    main()