
def main():
    n1 = int(input("Introduzca 1 numero: "))
    n2 = int(input("Introduzca 2 numero: "))
    n3 = int(input("Introduzca 3 numero: "))
    n4 = int(input("Introduzca 4 numero: "))
    print("La mediana es: " + str(calc_mediana(n1, n2, n3, n4)))

def calc_mediana(a:float, b:float, c:float, d:float) -> float:
    if a>b and a>c and a>d and b<c and b<d: # a es el mayor y b es el menor
        return (c+d)/2
    elif a>b and a>c and a>d and c<b and c<d: # a es el mayor y c es el menor
        return (b+d)/2
    elif a>b and a>c and a>d and d<b and d<c: # a es el mayor y d es el menor
        return (b+c)/2
    elif b>a and b>c and b>d and a<b and a<c: # b es el mayor y a es el menor
        return (c+d)/2
    elif b > a and b > c and b > d and c < b and c < a:  # b es el mayor y c es el menor
        return (a+d)/2
    elif b > a and b > c and b > d and d < b and d < a:  # b es el mayor y d es el menor
        return (a+c)/2
    elif c > a and c > b and c > d and a < b and a < d:  # c es el mayor y a es el menor
        return (b+d)/2
    elif c > a and c > b and c > d and b < a and b < d:  # c es el mayor y b es el menor
        return (a+d)/2
    elif c > a and c > b and c > d and d < a and d < b:  # c es el mayor y d es el menor
        return (a + b) / 2
    elif d > a and d > b and d > c and a < c and a < b:  # d es el mayor y a es el menor
        return (c + b) / 2
    elif d > a and d > b and d > c and b < c and b < a:  # d es el mayor y b es el menor
        return (c + a) / 2
    else:  # d es el mayor y c es el menor
        return (b + a) / 2

if __name__ == '__main__' or __name__ == 'ejemplo_T1_mediana4':
    main()