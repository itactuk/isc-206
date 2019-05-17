
meses = {
    1:'Enero',
    2:'Febrero',
    3:'Marzo',
    4:'Abril',
    5:'Mayo',
    6:'Junio',
    7:'Julio',
    8:'Agosto',
    9:'Septiembre',
    10: 'Octubre',
    11: 'Noviembre',
    12: 'Diciembre',
}

mes_numerico = int(input("Digita mes numerico: "))

if mes_numerico in meses:
    mes_texto = meses[mes_numerico]
    print('El mes es ' + mes_texto)
else:
    print('No es un mes')
