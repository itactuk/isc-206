n = int(input())
i = 0
s = 0
m = n
if n<2:
    print("n es muy pequeno")
else:
    while n>0:
        valor = int(input())
        s += valor
        n-=1
    p = s/m
    print(p)