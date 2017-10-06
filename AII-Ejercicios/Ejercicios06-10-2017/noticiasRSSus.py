# -*- coding: utf-8 -*-
'''
Created on 6 oct. 2017

@author: admin
'''
import feedparser

url="http://www.us.es/rss/feed/portada"
rss=feedparser.parse(url)
entradas=rss.entries
def showNoticias():
    for noticia in entradas:
        print("Título: "+str(noticia.title.encode('utf-8')))
        print("Link: "+str(noticia.link.encode('utf-8')))
        fecha=str(noticia.published_parsed[2])+"/" +str(noticia.published_parsed[1])+"/" +str(noticia.published_parsed[0])
        print(fecha)
        
        print("\n\n")
def showNoticiasFecha():
    print("""Introduzca una fecha con el siguiente formato: "(dd­mm­aaaa):8-9-2017"  """)
    fechaBusqueda= str(input())
    print(fechaBusqueda)
    try :
        for noticia in entradas:
            fechaFormatoInput=fecha=str(noticia.published_parsed[2])+"-" +str(noticia.published_parsed[1])+"-" +str(noticia.published_parsed[0])
            if(fechaBusqueda==fechaFormatoInput):
                print("Título: "+str(noticia.title.encode('utf-8')))
                print("Link: "+str(noticia.link.encode('utf-8')))
                fecha=str(noticia.published_parsed[2])+"/" +str(noticia.published_parsed[1])+"/" +str(noticia.published_parsed[0])
                print(fecha)

    except:
        print("Fecha introducidad de forma incorrecta, intentelo de nuevo")
        showNoticiasFecha()
    
showNoticiasFecha()