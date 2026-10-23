import random
import string
pt=input("Enter plaintext: ").upper()
a=list(string.ascii_uppercase)
b=a.copy()
random.shuffle(b)
print("Key used:","".join(b))
ct=""
for c in pt:
    if c in a:
        ct+=b[a.index(c)]
    else:
        ct+=c
print("Ciphertext:",ct)
dt=""
for c in ct:
    if c in b:
        dt+=a[b.index(c)]
    else:
        dt+=c
print("Decrypted:",dt)