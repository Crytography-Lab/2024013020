ct = input("Enter cipher text: ")
k = int(input("Enter key: "))
pt = ""
for i in ct:
    pt += chr((ord(i)-k-65)%26+97)
print("Plain text is: ", pt)