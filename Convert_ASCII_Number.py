"""
se da un string `abcd` convertirlo a un numero entero
a == 97
b == 98
abcd == 979899100
"""

def convert(s: str) -> int:
    result = 0
    for letter in s:
        aux = ord(letter)
        result *= 10 ** (len(str(aux))) 
        result += aux
    return result
print(convert("abcde"))

assert convert("abcde") == 979899100101
assert ord('a') == 97
