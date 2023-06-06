from typing import Union

class Affine:
    @staticmethod
    def __gcd(a : int, b : int) -> int:
        while b:
            a, b = b, a % b
        return a
    
    @staticmethod
    def __mod_inverse(a : int, m : int) -> Union[int, None]:
        if Affine.__gcd(a, m) == 1:
            for x in range(1, m):
                if (a * x) % m == 1:
                    return x
        return None
    
    def encrypt(self, text : str, key : tuple) -> str:
        a, b = key
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                if char.isupper():
                    encrypted_text += chr((a * (ord(char) - 65) + b) % 26 + 65)
                else:
                    encrypted_text += chr((a * (ord(char) - 97) + b) % 26 + 97)
            else:
                encrypted_text += char
        return encrypted_text
    
    def decrypt(self, ciphertext : str, key : tuple) -> str:
        a, b = key
        decrypted_text = ""
        a_inverse = self.__mod_inverse(a, 26)
        if a_inverse is None:
            raise Exception("Error: Invalid key. 'a' and 26 must be coprime.")

        for char in ciphertext:
            if char.isalpha():
                if char.isupper():
                    decrypted_text += chr((a_inverse * (ord(char) - 65 - b)) % 26 + 65)
                else:
                    decrypted_text += chr((a_inverse * (ord(char) - 97 - b)) % 26 + 97)
            else:
                decrypted_text += char
        return decrypted_text
    
# Example usage:
plaintext = "Hello, World!"
key = (5, 7)  # 'a' = 5, 'b' = 7
affine = Affine()
encrypted_text = affine.encrypt(plaintext, key)
decrypted_text = affine.decrypt(encrypted_text, key)

print("Plaintext:", plaintext)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)