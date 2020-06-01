import subprocess
p = subprocess.run("pip3 install -e package/", shell=True)

import re
from cipherpy import base, cipher


file = open("./plain_input.txt", "r")
inputs = [line for line in file]
file.close()

inputs = [re.sub(r'[^\w]', '', line.strip()).split('\\n') for line in inputs]
clean_input = []
[[clean_input.append(split_line.lower()) for split_line in line] for line in inputs]

# Brief explorations of functions

encoded = cipher.caesar_encode(clean_input[0], 1)
print(cipher.caesar_decode(encoded, 1))
encoded2 = (cipher.keyed_caesar_encode("helloworld", 1, "hello"))
print(cipher.keyed_caesar_decode(encoded2, 1, "hello"))
print(base.atbash("abcd"))
print(cipher.vigenere_encode("helloworld", "cardiff"))
print(cipher.vigenere_decode("jecowbttlu", "cardiff"))
print(cipher.keyed_vigenere_encode("helloworld", "cardiff", "hello"))
print(cipher.keyed_vigenere_decode("cbtgmajxcy", "cardiff", "hello"))
print(cipher.playfair_encode("hellooneandall"))
print(cipher.playfair_decode("kcnvmppoabocfqnv"))
print(cipher.keyed_playfair_encode("hellooneandall", "cardiff"))
print(cipher.keyed_playfair_decode("fgmwmkkobrtgbqmw", "cardiff"))