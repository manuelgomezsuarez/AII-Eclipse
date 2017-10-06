# -*- coding: utf-8 -*-
'''
Created on 6 oct. 2017

@author: Admin
'''
import urllib
import re
import datetime
"""
try:
    conexion= urllib.urlretrieve("http://www.us.es/rss/feed/portada","noticias.txt")
    conexion.close()
except:
    print("Ocurrió un error inesperado, intentelo de nuevo")
    """
fichero=open("noticias.txt")
texto=fichero.read()
titulos=re.findall("<title>(.+)</title>", texto)
links=re.findall("<link>(.+)</link>", texto)
fechas=re.findall("<pubDate>(.+)</pubDate>", texto)
diccionario={"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}
noticias=[]
fechasFormato=[]

for fecha in fechas:
    dia=fecha[5:7]
    mes=diccionario[fecha[8:11]]
    ano=fecha[12:16]
    fechasFormato.append(dia+"-"+mes+"-"+ano)

for n in range(1,len(titulos)):
    noticias.append(["Titulo: "+titulos[n],"\nLink: "+links[n],"\nFecha: "+fechasFormato[n]])

def muestraNoticias(fechaNoticia=""):    
    for x in noticias:
        if(fechaNoticia):
            if(fechaNoticia==x[2][8::]):
                print(x[0])
                print(x[1])
                print(x[2])
            else:
                pass
        else:
            print(x[0])
            print(x[1])
            print(x[2])
            print("-----------------------------------------------")


def menu():
    print("Escriba una fecha con el siguiente formato: 03-10-2017 o pulse intro para buscar todas las noticias" )
    fechaBusqueda=raw_input()
    muestraNoticias(fechaBusqueda)

menu()
    
    
    
    
    
    