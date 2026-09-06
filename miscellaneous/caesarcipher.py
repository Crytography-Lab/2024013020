pt = input("Enter plain text: ")
k = int(input("Enter key: "))
ct = ""
for i in pt:
    ct += chr((ord(i)+k-97)%26+65)
print("Cipher text is: ", ct)