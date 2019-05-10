
lectura = input("Digita a: ")

a = int(lectura)
b = int(input("Digita b: "))
c = int(input("Digita c: "))

d = ((b**2) - (4 * a * c))**0.5

x1 = (-b + d) / (2 *a)
x2 = (-b - d) / (2 *a)

print("El resultado es x1=" + str(x1) + " y x2=" + str(x2))