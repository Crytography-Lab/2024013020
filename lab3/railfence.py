pt=input("Enter plaintext: ").replace(" ","")
r=int(input("Enter number of rails: "))
fence=[["" for _ in range(len(pt))] for _ in range(r)]
row=0
d=1
for i,c in enumerate(pt):
    fence[row][i]=c
    if row==0:
        d=1
    elif row==r-1:
        d=-1
    row+=d
ct=""
for i in range(r):
    for j in range(len(pt)):
        ct+=fence[i][j]
print("Ciphertext:",ct)
mark=[["" for _ in range(len(ct))] for _ in range(r)]
row=0
d=1
for i in range(len(ct)):
    mark[row][i]="*"
    if row==0:
        d=1
    elif row==r-1:
        d=-1
    row+=d
idx=0
for i in range(r):
    for j in range(len(ct)):
        if mark[i][j]=="*":
            mark[i][j]=ct[idx]
            idx+=1
dt=""
row=0
d=1
for i in range(len(ct)):
    dt+=mark[row][i]
    if row==0:
        d=1
    elif row==r-1:
        d=-1
    row+=d
print("Decrypted:",dt)