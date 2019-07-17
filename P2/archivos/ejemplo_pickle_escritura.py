import pickle

mi_variables = {
    'maria': 23,
    'jose':24,
    'francisco':25
}

archivo_binario = open('mi_data.bin','wb')
pickle.dump(mi_variables, archivo_binario)
archivo_binario.close()