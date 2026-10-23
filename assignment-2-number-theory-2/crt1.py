n = int(input("Enter no. of equations: "))
rem = list(map(int, input("Enter the remainders: ").split()))
mod = list(map(int, input("Enter the modulus: ").split()))
N = 1
for i in range(n):
    N *= mod[i]

x = 0
for i in range(n):
    Ni = N // mod[i]
    Mi = 0
    for j in range(1, mod[i]):
        if (Ni * j) % mod[i] == 1:
            Mi = j
            break
    x += rem[i] * Ni * Mi
    
print("Solution:", x % N)
