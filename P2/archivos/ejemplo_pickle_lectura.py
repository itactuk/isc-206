import pickle



archivo_binario = open('mi_data.bin','rb')
mi_variables = pickle.load(archivo_binario)
archivo_binario.close()

print(mi_variables)