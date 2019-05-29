# Inicio	H. norte	H. sur
# 20-21 Marzo	Primavera	Otoño
# 21-22 Junio	Verano	Invierno
# 22-24 Septiembre	Otoño	Primavera
# 21-22 Diciembre	Invierno

dia = int(input('Día: '))
mes = int(input('Mes: '))

mes_31_dias = [1,3,5,7,8,10,12]

estacion = None
if dia <=0 or (dia >31) or (mes not in mes_31_dias and dia>30) or (mes==2 and dia>28):
    pass
elif (mes>=1 and mes <= 2) or (mes == 3 and dia <=20):
    estacion = 'Invierno'
elif (mes>=7 and mes <= 8) or (mes == 6 and dia >=21) or (mes == 9 and dia <=22):
    estacion = 'Verano'
elif (mes>=10 and mes <= 11) or (mes == 9 and dia >=22) or (mes == 12 and dia <=21):
    estacion = 'Otoño'
elif (mes>=4 and mes <= 5) or (mes == 3 and dia >=21) or (mes == 6 and dia <=21):
    estacion = 'Primavera'

if estacion is not None:
    print('La estacion es ' + estacion)
else:
    print("Fecha Invalida")
