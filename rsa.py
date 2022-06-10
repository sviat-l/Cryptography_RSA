"""
encrypt and decrypt messages with publuc and private keys, RSA crypto
"""

from list_primes import primes
import random
from hashlib import sha256


def gcd(a, b):
    """
    gcd of two numbers a, b
    """
    return gcd(b, a % b) if b else a


def modular_multiplicative_inverse(a, b):
    """
    gcd of two numbers with modular multiplicative inverse of two number a, b
    """
    if a == 0:
        return 0, 1
    a1, b1 = modular_multiplicative_inverse(b % a, a)
    return b1 - (b//a)*a1, a1


def create_keys():
    """
    create public and private keys for users
    """
    while True:
        p = random.choice(primes)
        q = random.choice(primes)
        if p != q:
            N = p*q
            if N > 10000:
                break
    M = N - p - q + 1

    e = random.choice(primes)
    while gcd(e, M) != 1:
        e = random.choice(primes)

    d = (modular_multiplicative_inverse(e, M)[0]+M) % M
    return (e, N), (d, N)


def decrypt(encrypted_text, private_key):
    """
    decrypt message with private key
    """
    d, n = private_key
    return  ''.join([ chr(((int(number)) ** d) % n) for number in encrypted_text.split()])


def encrypt(text, public_key):
    """
    encrypt message with public key
    """
    e, n = public_key
    return ' '.join([str((ord(s) ** e) % n) for s in text])
    # return ' '.join([str(pow(ord(s), e, n)) for s in text])


def hash_check(message):
    """
    compare initial and decrypted messages and its hash
    """
    public_key, private_key = create_keys()
    print(public_key, private_key)
    hash1 = sha256(message.encode("utf-8"))
    encrypted_message = encrypt(message, public_key)
    decrypted_message = decrypt(encrypted_message, private_key)
    hash2 = sha256(decrypted_message.encode("utf-8"))
    print('---Initial text---\n' + message)
    print("---Encrypted text---\n" + encrypted_message)
    print("---Decrypted text---\n" + decrypted_message)
    print("\nHash of an initial message == hash of a decrypted message",
          hash1.digest() == hash2.digest(), sep='\n')
    print('---- Initial text hash ----', hash1.digest(),
          '--- Decrypted text hash ---', hash2.digest(), sep='\n')


if __name__ == '__main__':
    message = 'qwerty йцукен'
    hash_check(message)
