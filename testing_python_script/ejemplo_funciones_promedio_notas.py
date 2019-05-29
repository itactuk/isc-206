from typing import List, Union


def calcular_promedio(notas:List[Union[float, int]]) -> float:
    ac = 0
    cont = 0
    for i in notas:
        ac += i
        cont += 1
    promedio =  ac / cont
    return promedio
calcular_promedio()
x = calcular_promedio([100,98,87,40,])
print(x)
