coste  = int(input("coste: "))
vida_util  = int(input("vida util: "))
marca = input("Marca: ")
valor_rescate=int(input("valor_rescate"))

depreciacion = (coste-valor_rescate)/vida_util

print("Nivel depreciacion: ", end="")
if depreciacion < 10000:
    print("baja")
elif depreciacion>= 10000 and depreciacion<=800000:
    if marca == "Honda":
        print("baja")
    elif marca == "Toyota":
        print("media")
    else:
        print("alta")
else:
    print("alta")

depreciacion_acc = 0
print(
        'Año\t'
        + 'Depreciacion\t'
        + 'Depreciacion_Acumulada\t'
        + 'Valor_Anual'
    )
for ano in range(1,7):
    ano_absoluto = ano + 1995
    depreciacion_acc += depreciacion
    valor_anual = coste - depreciacion_acc
    print(
        str(ano) + '(' + str(ano_absoluto) + ')\t'
        + str(depreciacion) + '\t'
        + str(depreciacion_acc) +'\t'
        + str(valor_anual)
    )












