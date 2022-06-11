# Cryptography
Here is an implementation of a safe messaging chat server that can be used in the application and RSA crypto-algorithm. 

## RSA
RSA is a cryptography algorithm that works with public/private keys. You can read more about it [here](https://www.educative.io/edpresso/what-is-the-rsa-algorithm).\
Firstly, you generate keys for each user. The private key can see only one user and is used to encrypt the message. The public key is available for all users and is used to decrypt the message.\
Implementing RSA algorithm requires creating a function to generate key pairs and functions to encode and decode the text. Relative functions are carried out in [rsa.py](../main/rsa.py).\
Also, there is a hash check function to validate whether a message was delivered correctly and the hash of the decrypted text is equal to the initial text's hash.\
![image](https://user-images.githubusercontent.com/91615606/173145620-8901d033-8d36-4f97-be8e-a5afdf574669.png)

## How does it work?
In [server.py](../main/server.py) is a script to run a server. Here we get encrypted messages from users, save public keys, encrypt/decrypt text on the server-side and deliver messages to other people.\
[Client.py](../main/client.py) is used for generating users' keys, exchanging public keys with the server, and decrypting/encrypting messages on the user side./
 
### Short path order
1. Launching a server and generating its keys
2. Adding clients with their generated private/public keys
3. Server gets the user's public keys.
4. __Message is created by user__
5. Message is encrypted with the server's public key and sent to the server
6. Message is decrypted with the server's private key
7. Server encrypts the message with the client's public key and sends it to every client
8. Clients decrypt messages by their private key and read them on their windows

## Examples
Example, with two people
![image](https://user-images.githubusercontent.com/91615606/173161800-75e73d28-0dfa-4d30-92fc-6dbfd6051d7b.png)
Example with more people. Note that if you connect later, you can not see previous messages.
![image](https://user-images.githubusercontent.com/91615606/173163286-0a62d288-e48d-4e79-8ba2-8898b9d342ce.png)


## Usage
Firstly, you should launch a server. Use the command below:
```bash
$ python3 server.py
```
After that, you can launch clients' windows (as many as you want) in different windows by command:
```bash
$ python3 client.py
```
Now you are connected with other users. You can write messages in your client window and also read messages from other users.

If you want to stop, press ctrl+Z
