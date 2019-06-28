
def es_primo(n):
    if n==2:
        return True
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

suma=0
for i in range(0, 2000):
    if es_primo(i):
        suma+=i

print(suma)