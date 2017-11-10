# -*- coding: utf-8 -*-
'''
Created on 24 oct. 2017

@author: Garbancito
'''

from Tkinter import *
import sqlite3
import urllib2
import os
import tkMessageBox
from bs4 import BeautifulSoup
from Tkinter import *
from whoosh.index import *
from whoosh.fields import *
from whoosh.qparser import QueryParser
import shutil
import os
import copy
def borraCreaIndex(arrayDatos):
    if os.path.exists("index"):
        shutil.rmtree("index")
    schema = Schema(titulo=TEXT(stored=True), link=KEYWORD(stored=True), 
                    username= KEYWORD(stored=True), userLink= TEXT(stored=True), 
                    fecha= TEXT(stored=True),numRespuestas=TEXT(stored=True),
                    numVisitas=TEXT(stored=True))
    if not os.path.exists("index"):
        os.mkdir("index")
        ix = create_in("index", schema)
    else:
        ix = open_dir("index")
    
    
    for datos in arrayDatos:
        writer = ix.writer()
        try:
            writer.add_document(titulo=unicode(datos[0]), link=unicode(datos[5]), username= unicode(datos[3]), userLink=unicode(datos[6].decode("utf-8")), fecha= unicode(datos[4]),numRespuestas=unicode(datos[1]),numVisitas=unicode(datos[2]))
        except Exception as ex:
            print(ex)
        writer.commit()
    
def borraCreaIndexRespuestas(arrayDatos):
    if os.path.exists("indexRespuestas"):
        shutil.rmtree("indexRespuestas")
    schema = Schema(titulo=TEXT(stored=True), fecha=TEXT(stored=True), 
                    textoRespuesta= TEXT(stored=True),username= KEYWORD(stored=True),userLink= TEXT(stored=True))
    if not os.path.exists("indexRespuestas"):
        os.mkdir("indexRespuestas")
        ix = create_in("indexRespuestas", schema)
    else:
        ix = open_dir("indexRespuestas")
    
    
    for datos in arrayDatos:
        writer = ix.writer()
        try:
            writer.add_document(titulo=unicode(datos[0]), fecha=unicode(datos[1]),textoRespuesta= unicode(datos[2]),username= unicode(datos[3]),userLink= unicode(datos[4]))
        except Exception as ex:
            print(ex)
        writer.commit()



def obtenDatosDePagina(enlace):
#     datosCategoria = urllib2.urlopen(enlace).read() #buscamos en cada categoria
#     soup = BeautifulSoup(datosCategoria, 'html.parser')
#     temas=soup.find_all("li",attrs={"class":"threadbit "}) 
    arrayGordo=[]
    arrayGordoRespuestas=[]
    datosArray=[0,0,0,0,0,0,0]
    datosArrayRespuestas=[0,0,0,0,0]
    for n in range(1,4):
        enlace="https://foros.derecho.com/foro/20-Derecho-Civil-General/page"+str(n)
        datosCategoria = urllib2.urlopen(enlace).read()
        soup = BeautifulSoup(datosCategoria, 'html.parser')
        temas=soup.find_all("li",attrs={"class":"threadbit "})
        for tema in temas:
            enlace = 'https://foros.derecho.com/' + tema.find('a', {'class':'title'})['href']
#             print enlace#enlace
#             print tema.find_all("a")[1].text#tema
#             print tema.find_all("ul")[0].find_all("li")[0].text#respuestas
#             print tema.find_all("ul")[0].find_all("li")[1].text#visitas
#             print tema.find_all("a")[2].text#creador
#             print tema.find_all("a")[2].get("href")
            userLink="https://foros.derecho.com/"
            userLink=userLink+str(tema.find_all("a")[2].get("href").encode("utf-8"))
#             print(userLink)
#             print tema.find_all("a")[2].get("title").split(",")[1].replace(" el ","")#fecha
#             print "*****************"
#             print
            datosArray[0]=tema.find_all("a")[1].text  #Titulo
            datosArray[1]=tema.find_all("ul")[0].find_all("li")[0].text  #numRespuestas
            datosArray[2]=tema.find_all("ul")[0].find_all("li")[1].text  #numVisitas
            datosArray[3]=tema.find_all("a")[2].text  #username
            datosArray[4]=tema.find_all("a")[2].get("title").split(",")[1].replace(" el ","") #Fecha
            datosArray[5]=enlace   #EnlaceTema
            datosArray[6]=userLink  #userLink
            arrayGordo.append(copy.copy(datosArray))

            if int(datosArray[1].split(" ")[1])>1:
                
                urlTema=enlace
                datosTema = urllib2.urlopen(urlTema.encode("utf-8")).read()
                soupTema = BeautifulSoup(datosTema, 'html.parser')
                respuestas=soupTema.find_all("li",attrs={"class":"postbitlegacy"})
                for p in range(1,len(respuestas)):
                    print(respuestas[p].blockquote.text.strip())   #texto respuesta
                    print(respuestas[p].find("a",attrs={"class":"username"}).strong.text.strip())
                    print(respuestas[p].div.span.text.strip())
                    print(userLink+str(respuestas[p].find("a",attrs={"class":"username"}).get("href")))
                    datosArrayRespuestas[0]=datosArray[0]
                    datosArrayRespuestas[1]=respuestas[p].div.span.text.strip()
                    datosArrayRespuestas[2]=respuestas[p].blockquote.text.strip()
                    datosArrayRespuestas[3]=respuestas[p].find("a",attrs={"class":"username"}).strong.text.strip()
                    datosArrayRespuestas[4]=userLink+str(respuestas[p].find("a",attrs={"class":"username"}).get("href"))
                    arrayGordoRespuestas.append(copy.copy(datosArrayRespuestas))

            
    print "datos extraidos correctamente" 
    print(arrayGordoRespuestas)
    return arrayGordo,arrayGordoRespuestas
     





def botonIndexar():
    
    enlace="https://foros.derecho.com/foro/20-Derecho-Civil-General"
    (datosArray,datosArrayRespuestas)=obtenDatosDePagina(enlace);
    borraCreaIndex(datosArray)
    borraCreaIndexRespuestas(datosArrayRespuestas)
    tkMessageBox.showinfo( "WHOOSH", "Indexado Correctamente \nHay " + str(len(datosArray)) + " Temas Indexados y "+str(len(datosArrayRespuestas))+" Respuestas Indexadas") 

def busquedaTitulo(titulo):        
    ix = open_dir("index")
    qp = QueryParser("titulo", schema=ix.schema)
    q = qp.parse(unicode(str(titulo)))
    s=ix.searcher()
    results = s.search(q)
    for hit in results:
        print(hit.get("titulo"))
        print(hit.get("username"))
        print(hit.get("fecha"))
    return results

def busquedaAutor(autor):        
    ix = open_dir("index")
    qp = QueryParser("username", schema=ix.schema)
    q = qp.parse(unicode(str(autor)))
    s=ix.searcher()
    results = s.search(q)
    for hit in results:
        print(hit.get("titulo"))
        print(hit.get("username"))
        print(hit.get("fecha"))
    return results

def busquedaRespuestas(texto):        
    ix = open_dir("indexRespuestas")
    qp = QueryParser("textoRespuesta", schema=ix.schema)
    q = qp.parse(unicode(str(texto)))
    s=ix.searcher()
    results = s.search(q)
    for hit in results:
        print(hit.get("titulo"))
        print(hit.get("username"))
        print(hit.get("fecha"))
    return results
def imprimir_etiqueta(results):
    v = Toplevel()
    sc = Scrollbar(v)
    sc.pack(side=RIGHT, fill=Y)
    lb = Listbox(v, width=150, yscrollcommand=sc.set)
    print(len(results))
    for hit in results:
        lb.insert(END,hit.get("titulo"))
        lb.insert(END,hit.get("username"))
        lb.insert(END,hit.get("fecha"))
        lb.insert(END,'*********************')
    lb.pack(side = LEFT, fill = BOTH)
    sc.config(command = lb.yview)


def botonBuscarTitulo():
    def listar_busqueda(Event):
       
        s = str(E1.get())
        print s
        results=busquedaTitulo(str(E1.get()))
        imprimir_etiqueta(results)

    v = Toplevel()
    lb = Label(v, text="Introduzca el titulo a buscar: ")
    lb.pack(side = LEFT)
    E1 = Entry(v)
    E1.bind("<Return>", listar_busqueda)
    E1.pack(side = LEFT)
    
def botonBuscarAutor():
    def listar_busqueda(Event):
       
        s = str(E1.get())
        print s
        results=busquedaAutor(str(E1.get()))
        imprimir_etiqueta(results)

    v = Toplevel()
    lb = Label(v, text="Introduzca el autor a buscar: ")
    lb.pack(side = LEFT)
    E1 = Entry(v)
    E1.bind("<Return>", listar_busqueda)
    E1.pack(side = LEFT)
    
def botonBuscarTexto():
    def listar_busqueda(Event):
       
        s = str(E1.get())
        print s
        results=busquedaRespuestas(str(E1.get()))
        imprimir_etiqueta(results)

    v = Toplevel()
    lb = Label(v, text="Introduzca el texto a buscar: ")
    lb.pack(side = LEFT)
    E1 = Entry(v)
    E1.bind("<Return>", listar_busqueda)
    E1.pack(side = LEFT)


    



    
def salir():
    quit()
    
def ventanaPrincipal():
   
#     buscarCategorias = Button(top, text="Mostrar Temas", command = listar_bd)
#     buscarCategorias.pack(side = LEFT)
#     
#     salida = Button(top, text="Salir Programa", command = salir)
#     salida.pack(side = LEFT)
# 
#     popular = Button(top, text="temas populares", command = listar_bdStats)
#     popular.pack(side = LEFT)
# 
#     
#     respuestas = Button(top, text="temas Activos", command = listar_bdRespuestas)
#     respuestas.pack(side = LEFT)

    
#     tema = Button(top, text="Buscar Tema", command = botonBuscarTema)
#     tema.pack(side = LEFT)
#     
#     fecha = Button(top, text="Buscar Fecha", command = botonBuscarFecha)
#     fecha.pack(side = LEFT)

    root = Tk()
    menu = Menu(root)
    root.config(menu=menu)
    
    iniciomenu = Menu(menu)
    menu.add_cascade(label="Datos", menu=iniciomenu)
    iniciomenu.add_command(label="Indexar", command=botonIndexar)
    iniciomenu.add_command(label="Salir", command=salir)
    
  
    
    temamenu = Menu(menu)
    temamenu.add_command(label="Titulo", command=botonBuscarTitulo)
    temamenu.add_command(label="Autor", command=botonBuscarAutor)
    
    buscarmenu = Menu(menu)
    menu.add_cascade(label="Buscar", menu=buscarmenu)
    buscarmenu.add_command(label="Respuestas", command=botonBuscarTexto)
    buscarmenu.add_cascade(label="Temas", menu=temamenu)

    mainloop()



if __name__ == "__main__":
    
    ventanaPrincipal()