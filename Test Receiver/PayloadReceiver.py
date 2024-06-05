import socket
import os

class Ps4PayloadServer:
    def __init__(self, host='0.0.0.0', port=9999):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        print(f"Server listening on {self.host}:{self.port}")

    def start_server(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Connection from {addr}")

            with client_socket:
                payload_size_bytes = client_socket.recv(4)
                if not payload_size_bytes:
                    continue

                payload_size = int.from_bytes(payload_size_bytes, byteorder='big')
                payload_data = client_socket.recv(payload_size)

                if payload_data:
                    with open("payload.bin", "wb") as payload_file:
                        payload_file.write(payload_data)
                    print(f"Payload received and saved as 'payload.bin'")
                else:
                    print("No payload received")

                client_socket.sendall(b"Payload received successfully")

if __name__ == "__main__":
    server = Ps4PayloadServer()
    server.start_server()
