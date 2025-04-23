import random
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 % m0

def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_prime(max_value=10**6):
    while True:
        p = random.randint(10000, max_value)
        if is_prime(p):
            return p

class RSA:
    def __init__(self):
        self.public_key = None
        self.private_key = None

    def generate_keys(self):
        p = generate_prime()
        q = generate_prime()
        while p == q:
            q = generate_prime()

        n = p * q
        phi = (p - 1) * (q - 1)

        e = 65537
        if gcd(e, phi) != 1:
            e = 3
            while gcd(e, phi) != 1:
                e += 2

        d = modinv(e, phi)

        self.public_key = (e, n)
        self.private_key = (d, n)

    def encrypt(self, plaintext, public_key=None):
        if public_key is None:
            public_key = self.public_key
        e, n = public_key
        return [pow(ord(char), e, n) for char in plaintext]

    def decrypt(self, ciphertext, private_key=None):
        if private_key is None:
            private_key = self.private_key
        d, n = private_key
        return ''.join([chr(pow(char, d, n)) for char in ciphertext])
