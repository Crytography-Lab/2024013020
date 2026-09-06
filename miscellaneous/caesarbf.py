ct = input("Enter cipher text: ")
pt = ""
for k in range(26):
    for i in ct:
        if i == " ":
            pt += " "
        else:
            pt += chr((ord(i)-k-65)%26+97)
    print("Plain text is: ", pt, ", key: ", k)
    pt = ""