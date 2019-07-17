#!/usr/bin/python3

# Open a file
with open("..\\foo.txt", "a") as fo:
    fo.write( "Python is a great language.\nYeah its great!!\n")

with open("foo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)