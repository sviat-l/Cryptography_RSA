"""
Module to handle server clients
"""

import socket
import threading
import rsa


class Server:

    def __init__(self, port: int) -> None:
        self.host = '127.0.0.1'
        self.port = port
        self.clients = []
        self.username_lookup = {}
        self.users_public_keys = {}
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.s.bind((self.host, self.port))
        self.s.listen(100)

        # initialize the pair of keys for server
        self.public_key, self.private_key = rsa.create_keys()

        while True:
            c, addr = self.s.accept()

            # send server's public key to the client
            c.send((str(self.public_key).encode()))

            # get client name and public key
            client_info = c.recv(2048).decode()
            username, client_public_key = client_info.split("\n")
            client_public_key = tuple(int(x) for x in client_public_key[1:-1].split(','))

            print(f"{username} tries to connect")
            self.broadcast(f'{username} joined')
            self.username_lookup[c] = username
            self.users_public_keys[c] = client_public_key
            self.clients.append(c)

            threading.Thread(target=self.handle_client, args=(c, addr)).start()

    def broadcast(self, msg: str):
        for client in self.clients:

            # encrypt the message
            encrypted = rsa.encrypt(msg, self.users_public_keys[client])

            client.send(str(encrypted).encode())

    def handle_client(self, c: socket, addr):
        while True:
            message = rsa.decrypt(c.recv(1024).decode(), self.private_key)
            message = f'{self.username_lookup[c]}: ' + message

            # decode message using clients' keys
            for client in self.clients:
                if client != c:
                    encrypted = rsa.encrypt(
                        message, self.users_public_keys[client])
                    client.send(encrypted.encode())


if __name__ == "__main__":
    s = Server(9001)
    s.start()
