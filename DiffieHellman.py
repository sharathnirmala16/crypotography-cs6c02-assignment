class DiffieHellman:
    __shared_secret : int = None
    def __init__(self, g : int, p : int, x : int, y : int) -> None:
        public_key_A = (g ** x) % p
        public_key_B = (g ** y) % p

        shared_secret_A = (public_key_B ** x) % p
        shared_secret_B = (public_key_A ** y) % p

        assert shared_secret_A == shared_secret_B
        self.__shared_secret = shared_secret_A

    @property
    def shared_secret(self) -> int:
        return self.__shared_secret


g = 5  
p = 23  
x = 6  
y = 15  

symmetric_key = DiffieHellman(g, p, x, y).shared_secret

print("Symmetric Key:", symmetric_key)