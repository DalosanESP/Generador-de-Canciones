import os
from Graph import *
from Vertex import *
canciones = []
letras = 0
palabras = ""

class Graph:
     def __init__(self,listaVertex):
        self.listaVertex = listaVertex

class Vertex:
    def __init__(self,palabra,conexion):
        self.palabra = palabra 
        self.conexion = conexion

class Reader:
    directorio = 'songs/'
    with os.scandir(directorio) as ficheros:
        for fichero in ficheros:
            canciones.append(fichero.name)

    listacancion = Graph([Vertex])
    
    for i in range(len(canciones)):
        open('songs/' + canciones[i])
        letras = open('songs/'+canciones[i])
        leidas = letras.read()
        letraLimpia = leidas.replace(",", "").replace("(", "").replace(")", "").replace(
            "?", "").replace('"', "").replace("'", "").replace("-", "")
        letraFinal = letraLimpia.lower()
        palabraLimpia = letraFinal.split()
        print(palabraLimpia)

        for j in range(len(palabraLimpia)):
            if j < len(palabraLimpia) - 1:
                for k in range:
                    if palabraLimpia[j] not in listacancion.listaVertex[k].palabra:
                        esta = False
                    else:
                        esta = True
                    if j == len(palabraLimpia)-1:
                        if esta == False:
                            canciones.listaVertex.insert(Vertex(palabraLimpia[j],[[],[Vertex]]))

    # usar u netxt en algun momento
    # lista de punteros
    # por cada palabra un vertex


# conseguir que lea las canciones y que por cada palabra crear vertex y añada al grafo, pero un vertex por palabra


# metodo iniciar(numero de palabras total)
# qyue busqye una palabra y que escriba las siguientes hasta 100 (por ejemplo)

# hacer codigo bonito
