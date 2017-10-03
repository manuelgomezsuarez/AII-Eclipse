# -*- coding: utf-8 -*-
'''
Created on 3 oct. 2017

@author: Manuel Gómez Suárez
'''
def Ejercicio1a(palabra):
    """Inserte el caracter ',' entre cada letra de la cadena. Ej: ’separar’ y ’,’ debería devolver
        ’s,e,p,a,r,a,r’"""
    nuevoString=""
    for n in range(len(palabra)):
        if(n==len(palabra)-1):
            nuevoString+=palabra[n]
        else:
            nuevoString+=palabra[n]+","
    print(nuevoString)
    return nuevoString

def Ejercicio1b(frase):
    """Reemplace todos los espacios por el caracter '_'. Ej: ’mi archivo de texto.txt’ y ’_’
        debería devolver ’mi_archivo_de_texto.txt’"""
    trozos=frase.split()
    numPalabras=len(trozos)
    res=""
    for palabra in trozos:
        if(palabra!= trozos[numPalabras-1]):
            res+=palabra+"_"
        else:
            res+=palabra
    print(res)
    return res

def Ejercicio1c(fraseConNumeros):
    """Reemplace todos los dígitos en la cadena por el caracter 'X'. Ej: ’su clave es: 1540’ y
        ’X’ debería devolver ’su clave es: XXXX’"""
    res=""
    for n in range(len(fraseConNumeros)):
        try:
            int(fraseConNumeros[n])
            res+="X"
        except:
            res+=fraseConNumeros[n]
    print (res)       
    return res

def Ejercicio1d(cadenaTexto):
    """Inserte el caracter '.' cada 3 dígitos en la cadena. Ej. ’2552552550’ y ’.’ debería
        devolver ’255.255.255.0’"""
    res=""
    for n in range(len(cadenaTexto)):
        if (n+1)%3 ==0:
            res+=cadenaTexto[n]+"."
        else:
            res+=cadenaTexto[n]
    print(res)
    return res    

Ejercicio1a("comasEnMedio")
Ejercicio1b("probando barras por espacios")
Ejercicio1c("Esta es mi clave: 12345")
Ejercicio1d("192168255255")