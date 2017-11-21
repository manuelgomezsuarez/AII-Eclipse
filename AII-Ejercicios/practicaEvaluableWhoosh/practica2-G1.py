# -*- coding: utf-8 -*-
'''
Created on 17 nov. 2017

@author: admin
'''
import sqlite3
import urllib2
import os
import tkMessageBox
from bs4 import BeautifulSoup
from Tkinter import *
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT, KEYWORD, ID, DATETIME
from whoosh.qparser import QueryParser
from whoosh.qparser.default import MultifieldParser
from whoosh.qparser.dateparse import DateParserPlugin
import datetime




def obtenDatosDePagina1(enlace):
    datosCategoria = urllib2.urlopen(enlace).read() #buscamos en cada categoria
    soup = BeautifulSoup(datosCategoria, 'html.parser')
    
    jornadas=soup.find_all("li",attrs={"class":"contenedorCalendarioInt"}) 
    datosArrayGordo=[]
    datosArray=[0,0,0,0,0,0,0,0] #jornada,enlace,titulo,resultado,tablaGoles
    
    cont=0
    jornadaContador=1 
    for partido in jornadas[0].find_all("article"):
        
        
        cont=cont+1
        if cont>10:
            jornadaContador=jornadaContador+1
            cont=0
        if(jornadaContador==4):
            break   
           
        #print cont
        print jornadaContador
        print partido.a.get("href") #enlace
        print partido.a.get("title") #titulo
        print partido.a.find_all("span")[2].text #resultado
        print "********"
        
        #ahora entramos a cada pagina y sacamos el que marco y en que minuto
        try:
            datosCategoria1 = urllib2.urlopen(partido.a.get("href")).read() #buscamos en cada categoria
            soup1 = BeautifulSoup(datosCategoria1, 'html.parser')
            goles=soup1.find_all("div",attrs={"class":"firma"})
            
            for gol in goles:
                fecha= gol.find_all("span")[1].text.split(" ")[0] #fecha
                autor= gol.find_all("span")[0].text #autor
                
            
            titular=soup1.find_all("section",attrs={"class":"columnaTitular"})
            
            for tit in titular:
                titularResult= tit.h3.text #titular
                tituloResult= tit.h4.text #titulo
            
            cuerpos=soup1.find_all("div",attrs={"class":"cuerpo_articulo"})
            
            for cuerpo in cuerpos:
                cuerpoResult= cuerpo.text
                
        except:
            pass
        fechaArray=fecha.split("/")
        fechanueva=fechaArray[2]+fechaArray[1]+fechaArray[0]
        datosArray[0]=jornadaContador #numero jornada
        datosArray[1]=fechanueva#fecha
        datosArray[2]=partido.a.get("title") #equipos
        datosArray[3]=partido.a.find_all("span")[2].text #resultado
        datosArray[4]=tituloResult #titular
        datosArray[5]=titularResult #titulo
        datosArray[6]=cuerpoResult #cuerpo
        datosArray[7]=autor #autor noticia
        datosArrayGordo.append(datosArray)
        datosArray=[0,0,0,0,0,0,0,0]
        
    return datosArrayGordo
#     tkMessageBox.showinfo( "Base Datos", "Base de datos creada correctamente \nHay " + str(cursor1.fetchone()[0]) + " PARTIDOS y "+str(cursor2.fetchone()[0]) +" GOLES") 
        



def getSchema():
    """ Crea y devuelve un esquema para la búsqueda"""
    return Schema(jornada=KEYWORD(stored=True),
                  equipos=TEXT(stored=True),
                  resultado=TEXT(stored=True),
                  fecha=KEYWORD(stored=True),
                  autor=TEXT(stored=True), 
                  titular=TEXT(stored=True),
                  titulo=KEYWORD(stored=True),
                  cuerpo=TEXT())

def add_doc(writer, datos):
    """Añade un documento al index con los campos necesarios"""
    for dato in datos:
        jrnda = unicode(str(dato[0]))
        eqpos = unicode(dato[2])
        rado = unicode(dato[3])
        fcha = unicode(dato[1])
        ator = unicode(dato[7])
        ttlar = unicode(dato[4])
        ttlo = unicode(dato[5])
        crpo = unicode(dato[6])
    
        writer.add_document(jornada=jrnda,
                            equipos=eqpos,
                            resultado=rado,
                            fecha=fcha,
                            autor=ator, 
                            titular=ttlar,
                            titulo=ttlo,
                            cuerpo=crpo)



def indexa():
    datos = obtenDatosDePagina1("http://www.marca.com/futbol/primera-division/calendario.html")
    """Crea el index, de los datos."""
    if not os.path.exists('index'):
        os.mkdir('index')
    
    ix = create_in('index', schema=getSchema()) # Crea el objeto index
    writer = ix.writer() 
    add_doc(writer, datos)

    tkMessageBox.showinfo("Fin de indexado", "Se han indexado "+str(len(datos))+ " partidos") 
    writer.commit()

def salir():
    quit()
    
def apartado_a():
    """Realiza bu"""
    def mostrar_lista(event):
        """Crea la lista con los resultados"""
        lb.delete(0, END)   #borra toda la lista
        ix = open_dir("index")      
        with ix.searcher() as searcher:
            query = QueryParser("cuerpo", schema=ix.schema).parse(unicode(en.get()))
            results = searcher.search(query)
            for r in results:
                lb.insert(END, r['jornada'])
                lb.insert(END, r['fecha'])
                lb.insert(END, r['equipos'])
                lb.insert(END, r['resultado'])
                lb.insert(END, r['titular'])
                lb.insert(END, r['titulo'])
                lb.insert(END, r['autor'])
                lb.insert(END, '')
    
    v = Toplevel()
    v.title("Busqueda de Noticia ")
    f = Frame(v)
    f.pack(side=TOP)
    l = Label(f, text="Introduzca su búsqueda:")
    l.pack(side=LEFT)
    en = Entry(f)
    en.bind("<Return>", mostrar_lista)
    en.pack(side=LEFT)
    sc = Scrollbar(v)
    sc.pack(side=RIGHT, fill=Y)
    lb = Listbox(v, yscrollcommand=sc.set)
    lb.pack(side=BOTTOM, fill=BOTH)
    sc.config(command=lb.yview)

def apartado_b():
    """Realiza bu"""
    def mostrar_lista(event):
        """Crea la lista con los resultados"""
        lb.delete(0, END)   #borra toda la lista
        ix = open_dir("index")      
        with ix.searcher() as searcher:
            
            ix = open_dir("index")
            
            query = QueryParser("fecha", ix.schema).parse(unicode(en.get()))
            results = searcher.search(query)     
    
            for r in results:
                lb.insert(END, r['jornada'])
                lb.insert(END, r['fecha'])
                lb.insert(END, r['equipos'])
                lb.insert(END, r['resultado'])
                lb.insert(END, r['titular'])
                lb.insert(END, r['titulo'])
                lb.insert(END, r['autor'])
                lb.insert(END, '')
    
    v = Toplevel()
    v.title("Busqueda por Fecha")
    f = Frame(v)
    f.pack(side=TOP)
    l = Label(f, text="Introduzca su búsqueda (YYYYMMDD):")
    l.pack(side=LEFT)
    en = Entry(f)
    en.bind("<Return>", mostrar_lista)
    en.pack(side=LEFT)
    sc = Scrollbar(v)
    sc.pack(side=RIGHT, fill=Y)
    lb = Listbox(v, yscrollcommand=sc.set)
    lb.pack(side=BOTTOM, fill=BOTH)
    sc.config(command=lb.yview)
def apartadoC():
    def botonIntroducirCategoria(Event):
        print w.get()
        v = Toplevel()
        sc = Scrollbar(v)
        sc.pack(side=RIGHT, fill=Y)
        lb = Listbox(v, width=150, yscrollcommand=sc.set)
        ix = open_dir("index")      
        with ix.searcher() as searcher:
            
           
            
            query = QueryParser("autor", ix.schema).parse(unicode(w.get()))
            results = searcher.search(query)     
    
            for r in results:
                lb.insert(END, r['jornada'])
                lb.insert(END, r['fecha'])
                lb.insert(END, r['equipos'])
                lb.insert(END, r['resultado'])
                lb.insert(END, r['titular'])
                lb.insert(END, r['titulo'])
                lb.insert(END, r['autor'])
                lb.insert(END, '')
        lb.pack(side = LEFT, fill = BOTH)
        sc.config(command = lb.yview)
        #conn.close()
    
    master = Toplevel()
    w = Spinbox(master,values=(list(busquedaAutores())))
    w.pack(side = LEFT)
    w.bind("<Return>", botonIntroducirCategoria)
def busquedaAutores():    
    autores=set()    
    ix = open_dir("index")
    qp = QueryParser("autor", schema=ix.schema)
    q = qp.parse("[a to z]")
    s=ix.searcher()
    results = s.search(q)
    for r in results:
        autores.add(r.get("autor"))
    
    
    return autores
def ventana_principal():
    """Crea la ventana principal"""
    root = Tk()
    menu = Menu(root)
    root.config(menu=menu)
    
    datosmenu = Menu(menu)
    menu.add_cascade(label="Datos", menu=datosmenu)
    datosmenu.add_command(label="Cargar", command=indexa)
    datosmenu.add_command(label="Salir", command=salir)
    
    buscarmenu = Menu(menu)
    menu.add_cascade(label="Buscar", menu=buscarmenu)
    buscarmenu.add_command(label="Noticia", command=apartado_a)
    buscarmenu.add_command(label="Fecha", command=apartado_b)
    buscarmenu.add_command(label="Autor", command=apartadoC)
    mainloop()
    
    
if __name__ == "__main__":
    ventana_principal()
