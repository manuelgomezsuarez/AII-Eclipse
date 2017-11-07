# -*- coding: utf-8 -*-
'''
Created on 7 nov. 2017

@author: Admin
'''

import funciones

from Tkinter import *
from whoosh.index import *

def ventanaPrincipal():  
    top = Tk()
    indexar = Button(top, text="Indexar Correos", command = botonIndexar)
    indexar.pack(side = LEFT) 
    buscar = Button(top, text="Buscar Por Remitente", command = BotonBuscarRemitente)
    buscar.pack(side = LEFT) 


    top.mainloop()
        
def imprimir_etiqueta(results):
    v = Toplevel()
    sc = Scrollbar(v)
    sc.pack(side=RIGHT, fill=Y)
    lb = Listbox(v, width=150, yscrollcommand=sc.set)
    for hit in results:
        lb.insert(END,hit.get("remitente"))
        lb.insert(END,hit.get("destinatarios"))
        lb.insert(END,hit.get("asunto"))
        lb.insert(END,'*********************')
    lb.pack(side = LEFT, fill = BOTH)
    sc.config(command = lb.yview)

def BotonBuscarRemitente():
    def listar_busqueda(event):
        results = funciones.busqueda(en.get())
        imprimir_etiqueta(results)
    v = Toplevel()
    lb = Label(v, text="Introduzca el remitente ")
    lb.pack(side = LEFT)
    en = Entry(v)
    en.bind("<Return>", listar_busqueda)
    en.pack(side = LEFT)

       
def botonIndexar():

    funciones.borraCreaIndex()
    
    print "Correos Indexados Correctamente"
    
ventanaPrincipal()