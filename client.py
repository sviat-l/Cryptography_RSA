"""
Module to work with server clients
"""
import socket
import threading
import rsa
import random


class Client:
    def __init__(self, server_ip: str, port: int, username: str) -> None:
        self.server_ip = server_ip
        self.port = port
        self.username = username

    def init_connection(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect((self.server_ip, self.port))
        except Exception as e:
            print("[client]: could not connect to server: ", e)
            return
        print(f'Your username: {self.username}')

        # create key pairs
        self.public_key, self.private_key = rsa.create_keys()

        # exchange public keys
        client_data = self.username + '\n' + str(self.public_key)
        self.s.send(client_data.encode())

        # receive the encrypted secret key
        self.server_public_key = self.s.recv(2048).decode()
        self.server_public_key = tuple(int(x) for x in self.server_public_key[1:-1].split(','))

        message_handler = threading.Thread(target=self.read_handler, args=())
        message_handler.start()
        input_handler = threading.Thread(target=self.write_handler, args=())
        input_handler.start()

    def read_handler(self):
        while True:
            message = self.s.recv(1024).decode()

            # decrypt message with the secrete key
            decrypted = rsa.decrypt(message, self.private_key)

            print(decrypted)

    def write_handler(self):
        while True:
            message = input()

            # encrypt message with the secrete key
            encrypted = rsa.encrypt(message, self.server_public_key)

            self.s.send(encrypted.encode())


if __name__ == "__main__":
    cl = Client("127.0.0.1", 9001, f"user{random.randint(10000, 100000)}")
    cl.init_connection()
