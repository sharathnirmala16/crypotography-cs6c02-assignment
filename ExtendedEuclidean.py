from typing import Union

class ExtendedEuclidean:
    @staticmethod
    def __extended_euclidean(a : int, b : int) -> tuple[int, int, int]:
        if b == 0:
            return a, 1, 0
        else:
            gcd, x, y = ExtendedEuclidean.__extended_euclidean(b, a % b)
            return gcd, y, x - (a // b) * y

    def mod_inverse(self, a : int, m : int) -> Union[int, None]:
        gcd, x, g = self.__extended_euclidean(a, m)
        if gcd == 1:
            return x % m
        return None

a = int(input('Enter a number:'))
m = int(input('Enter the length of Z*:'))

extended_euclidean = ExtendedEuclidean()
inverse = extended_euclidean.mod_inverse(a, m)

print(f"The modular inverse of the {a} modulo {m} is: {inverse}")