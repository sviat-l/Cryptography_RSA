# Cryptography
Here is an implemention of safe messaging chat server that can be used in application, and RSA crypto-algorithm. 

## RSA
RSA is a cryptography algorithm that works with public/private keys. You can read more about it [here](https://www.educative.io/edpresso/what-is-the-rsa-algorithm) 
Firstly, you generate keys for each user. Private key can see only one user and is used to encrypt the message. Public key is avaliable for all users and uses to decrypt the message.\
Implementing RSA algorithm reqiers creating a function to generate key pairs, function to encode and decode the text. Relative functions are carried out in [rsa.py](../main/rsa.py).\
Also there is a hash check function to validate wheather message was delived correctly and hash of the decrypted text is equel to the initial text's hash.\
![image](https://user-images.githubusercontent.com/91615606/173145620-8901d033-8d36-4f97-be8e-a5afdf574669.png)

## How does it work?
In [server.py](../main/server.py) is a script to run a server. Here we get encrypted messages from users, save public keys, enctypt/decrypt text on server side and deliver messages for other people.\
[Client.py](../main/client.py) is used for generating users key, exchenging public key with the server and decrypt/encrypt message on user side./
 
### Short path order
1. Launching a server and generating it's keys
2. Adding clients with their generated private/public keys
3. Server gets users public keys.
4. __Message is created by user__
5. Message is encrypted with server's public key and sent to the server
6. Message is decrypted with server's private key
7. Server encrypts message with client's public key and send it to every clien
8. Clients decrypt message by their private key and read it on its windows

## Examples

## Usage
Firsly, you should lanch a server. Use command below:
```bash
$ python3 server.py
```
After that you can lanch clients windows (as many as you wamt) in different windows by command:
```bash
$ python3 client.py
```
Now you are connected with other users. You can write messages in your client window; and, also, read messages from other users.

If you want stop, press ctrl+Z
