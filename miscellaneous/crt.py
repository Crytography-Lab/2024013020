n = int(input("Enter number of equations: "))

remainders = []
moduli = []

for i in range(n):
    r = int(input("Enter remainder: "))
    m = int(input("Enter modulus: "))
    remainders.append(r)
    moduli.append(m)

x = 0
step = 1

for i in range(n):
    r = remainders[i]
    m = moduli[i]

    while x % m != r:
        x += step

    step *= m

print("Solution:", x)