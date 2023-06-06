import os
import hashlib

class Password:
    @staticmethod
    def generate_salt(length : int=16) -> bytes:
        return os.urandom(length)
    
    @staticmethod
    def compute_hash(password : str, salt : bytes) -> str:
        hash_object = hashlib.sha256()
        salted_password = password.encode('utf-8') + salt
        hash_object.update(salted_password)
        hash_value = hash_object.hexdigest()
        return hash_value
    
    @staticmethod
    def verify_password(password : str, salt : bytes, hash_value : str) -> bool:
        computed_hash = Password.compute_hash(password, salt)
        if computed_hash == hash_value:
            return True
        return False
    
passwords = [
    "password1",
    "abc123",
    "qwerty",
    "letmein",
    "pass1234",
    "hello123",
    "password123",
    "changeme",
    "iloveyou",
    "admin123"
]

salts = []
for password in passwords:
    salts.append(Password.generate_salt())

hashes = []
for i, password in enumerate(passwords):
    hash_value = Password.compute_hash(password, salts[i])
    hashes.append(hash_value)

input_password = input("Enter your password: ")
input_index = int(input("Enter the index of your password (0-9): "))

if Password.verify_password(input_password, salts[input_index], hashes[input_index]):
    print("Access granted: Password is correct.")
else:
    print("Access denied: Password is incorrect.")