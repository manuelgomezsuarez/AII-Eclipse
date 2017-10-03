# -*- coding: utf-8 -*-
'''
Created on 3 oct. 2017

@author: Manuel Gómez Suárez
'''
agendaContactos={"pepe":"656258877","maria":"777889944","juan":"444556699"}
print ("""Introduzca un nombre para añadir o modificar contactos, ejemplo: "pepe", no olvide las comillas """)
a= input()
if a in agendaContactos.keys():
    print ("El contacto ya esta en la agenda con el número: "+agendaContactos.get(a))
    print("Introduzca el nuevo número para "+a+ """ ejemplo: "666998877" """ )
    nuevoNumero=input()
    agendaContactos[a]=nuevoNumero
    print("número modificado correctamente")
    print(a,agendaContactos[a])
else:
    print("El contacto no existe, introduzca un nuevo numero para este contacto: ")
    nuevoNumero2=input()
    agendaContactos[a]=nuevoNumero2
    print("Añadido con éxito, a continuación se muestra la agenda completa:")
    print(agendaContactos)
    
    
    