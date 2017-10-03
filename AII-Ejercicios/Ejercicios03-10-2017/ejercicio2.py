# -*- coding: utf-8 -*-
'''
Created on 3 oct. 2017

@author: Manuel Gómez Suárez
'''
"""Escribir funciones que dadas dos cadenas de caracteres: """

def Ejercicio2a(cadena1,cadena2):
    """Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, 
    ’cadena’ es una subcadena de ’subcadena’."""
    res=cadena1+ " No contiene la cadena: "+cadena2 
    if cadena2 in cadena1:
        res= cadena1+ " Contiene la cadena: "+cadena2 
    print(res)
    return res



def Ejercicio2b(cadena1,cadena2):
    """Devuelva la que sea anterior en orden alfábetico . Por ejemplo, si recibe ’kde’ y 
        ’gnome’ debe devolver ’gnome’. """
    listaNombres=[cadena1,cadena2]
    listaNombres.sort()
    print(listaNombres)
    return listaNombres

Ejercicio2a("subsuelo", "suelo")
Ejercicio2a("vaca", "lechera")
Ejercicio2b("Manuel", "Agustin")