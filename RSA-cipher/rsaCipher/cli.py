from rsaCipher.rsa import RSA

def interactive_mode():
    rsa = RSA()
    rsa.generate_keys()

    print("\nRSA Keys generated.")
    print("Public Key (e, n):", rsa.public_key)
    print("Private Key (d, n):", rsa.private_key)

    while True:
        mode = input("\nChoose mode: (E)ncrypt / (D)ecrypt / (Q)uit: ").strip().upper()
        if mode == 'E':
            plaintext = input("Enter plaintext: ")
            encrypted = rsa.encrypt(plaintext)
            print("Encrypted:", encrypted)
        elif mode == 'D':
            ciphertext = input("Enter encrypted numbers (comma-separated): ")
            try:
                nums = [int(x) for x in ciphertext.split(',')]
                decrypted = rsa.decrypt(nums)
                print("Decrypted:", decrypted)
            except ValueError:
                print("Invalid ciphertext input. Use comma-separated integers.")
        elif mode == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose E, D, or Q.")

if __name__ == "__main__":
    interactive_mode()
