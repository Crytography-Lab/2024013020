pt=input("Enter plaintext: ")
k=int(input("Enter key: "))
ct=""
for c in pt:
    if c.isalpha():
        b=65 if c.isupper() else 97
        ct+=chr((ord(c)-b+k)%26+b)
    else:
        ct+=c
print("Ciphertext:",ct)
dt=""
for c in ct:
    if c.isalpha():
        b=65 if c.isupper() else 97
        dt+=chr((ord(c)-b-k)%26+b)
    else:
        dt+=c
print("Decrypted:",dt)