import unittest
from rsaCipher.rsa import RSA

class TestRSA(unittest.TestCase):
    def setUp(self):
        self.rsa = RSA()
        self.rsa.generate_keys()

    def test_key_generation(self):
        self.assertIsNotNone(self.rsa.public_key)
        self.assertIsNotNone(self.rsa.private_key)
        self.assertNotEqual(self.rsa.public_key, self.rsa.private_key)

    def test_encrypt_decrypt(self):
        message = "HELLO RSA"
        encrypted = self.rsa.encrypt(message)
        decrypted = self.rsa.decrypt(encrypted)
        self.assertEqual(decrypted, message)

    def test_encrypt_with_custom_key(self):
        message = "TEST"
        pub = self.rsa.public_key
        encrypted = self.rsa.encrypt(message, pub)
        self.assertTrue(all(isinstance(x, int) for x in encrypted))

    def test_decrypt_with_custom_key(self):
        message = "CUSTOM"
        pub = self.rsa.public_key
        priv = self.rsa.private_key
        encrypted = self.rsa.encrypt(message, pub)
        decrypted = self.rsa.decrypt(encrypted, priv)
        self.assertEqual(decrypted, message)
