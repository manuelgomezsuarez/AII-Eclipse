# -*- coding: utf-8 -*-
'''
Created on 3 oct. 2017

@author: Manuel Gómez Suárez
'''
def saludoElectoral(tuplaNombres):
    """Escribir una función que reciba una tupla con nombres, y para cada nombre imprima 
        el mensaje Estimado <nombre>, vote por mí.""" 
    for n in tuplaNombres:
        print("Estimado "+n+", Vote por mí en las elecciones")
    print("####################################################")
    return 0


def saludoElectoralRestricciones(tuplaNombres,p,n):
    """Escribir una función que reciba una tupla con nombres, una posición de origen p y 
        una cantidad n, e imprima el mensaje anterior para los n nombres que se encuentran a 
        partir de la posición p. """
    contador=0
    for a in range(p,len(tuplaNombres)):
        if(contador<n):
            print("Estimado "+tuplaNombres[a]+", Vote por mí en las elecciones")
            contador+=1
    print("####################################################")
    return 0
#saludoElectoral(("Manuel","Pepe","Joaquin"))
#saludoElectoralRestricciones(("Manuel","Pepe","Joaquin","Beatriz","Ana","Alvaro","Lidia"),2,3)

def saludoElectoralRestriccionesGenero(tuplaNombresGeneros,p,n):
    """Escribir una función que reciba una tupla con nombres, una posición de origen p y 
        una cantidad n, e imprima el mensaje anterior para los n nombres que se encuentran a 
        partir de la posición p. """
    contador=0
    for a in range(p,len(tuplaNombresGeneros)):
        if(contador<n):
            if tuplaNombresGeneros[a][1]==("hombre"):
                print("Estimado "+tuplaNombresGeneros[a][0]+", Vote por mí en las elecciones")
            else:
                print("Estimada "+tuplaNombresGeneros[a][0]+", Vote por mí en las elecciones")
            contador+=1
    print("####################################################")
    return 0

def nombreApellidos(listaTuplas):
    """Escribir una función que reciba una lista de tuplas (Apellido, Nombre, 
        Inicial_segundo_nombre) y devuelva una lista de cadenas donde cada una contenga 
        primero el nombre, luego la inicial con un punto, y luego el apellido. """
    listaCadenaRes=[]
    for n in listaTuplas:
        listaCadenaRes+=[n[2]+" "+n[1]+". "+n[0]]
    print(listaCadenaRes)
    return listaCadenaRes




saludoElectoral(("Manuel","Pepe","Joaquin"))
saludoElectoralRestricciones(("Manuel","Pepe","Joaquin","Beatriz","Ana","Alvaro","Lidia"),2,3)
saludoElectoralRestriccionesGenero((("Manuel","hombre"),("Pepe","hombre"),("Joaquin","hombre"),
              ("Beatriz","mujer"),("Ana","mujer"),("Alvaro""hombre"),("Lidia","mujer")),2,3)
nombreApellidos([("Suarez","A","Manuel"),("Cabeza","U","Juan")])
