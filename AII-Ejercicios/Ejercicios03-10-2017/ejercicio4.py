# -*- coding: utf-8 -*-
'''
Created on 3 oct. 2017

@author: Admin
'''
def buscaCadenaTuplas(cadena,listaTuplas):
    """Escribir una función que reciba una cadena a buscar y una lista de tuplas 
        (nombre_completo, telefono), y busque dentro de la lista, todas las entradas que 
        contengan en el nombre completo la cadena recibida (puede ser el nombre, el apellido 
        o sólo una parte de cualquiera de ellos). Debe devolver una lista con todas las tuplas 
        encontradas. """
    busqueda=[]
    for n in range(len(listaTuplas)):
        if cadena in listaTuplas[n][0]:
            busqueda.append(listaTuplas[n])
    print(busqueda)
    return busqueda
        
        
buscaCadenaTuplas("pepe", [("pepe antonio delgado","656256687"),("jose pepe ramirez","666999887"),("Ana rodriguez matamoros","555889977")])
        
        