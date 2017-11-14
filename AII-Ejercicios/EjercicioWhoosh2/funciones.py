# -*- coding: utf-8 -*-
'''
Created on 7 nov. 2017

@author: Admin
'''
from whoosh.index import *
from whoosh.fields import *
from whoosh import fields
from whoosh.qparser import QueryParser
from whoosh.qparser.dateparse import DateParserPlugin
import shutil
import os
from whoosh.qparser.default import MultifieldParser
import datetime

def borraCreaIndex():
    if os.path.exists("index"):
        shutil.rmtree("index")
    schema = Schema(remitente=KEYWORD(stored=True), 
                    destinatarios=KEYWORD(stored=True),
                    fecha=fields.DATETIME(stored=True),
                     asunto= KEYWORD(stored=True), cuerpo= TEXT(stored=True))
    if not os.path.exists("index"):
        os.mkdir("index")
        ix = create_in("index", schema)
    else:
        ix = open_dir("index")
    
    quedanFicheros=True
    numeroFichero=1
    writer = ix.writer()
    while quedanFicheros:
        try:
            fichero=open("Correos/"+str(numeroFichero)+".txt")
            texto=fichero.read()
            textoPorPartes=(texto.split("\n",4))
            fechaFormat=datetime.datetime.strptime(textoPorPartes[2].strip(),"%Y%m%d")
            
            writer.add_document(remitente=unicode(textoPorPartes[0]),
                                destinatarios=unicode(textoPorPartes[1]),
                                fecha=fechaFormat,asunto=unicode(textoPorPartes[3]),
                                cuerpo=unicode(textoPorPartes[4]))
            numeroFichero=numeroFichero+1
        except Exception as ex:
            print("No hay mas ficheros")
            writer.commit()
            quedanFicheros=False
            
def borraCreaIndexAgenda():
    if os.path.exists("indexAgenda"):
        shutil.rmtree("indexAgenda")
    schema = Schema(email=KEYWORD(stored=True), nombreApellidos=KEYWORD(stored=True))
    if not os.path.exists("indexAgenda"):
        os.mkdir("indexAgenda")
        ix = create_in("indexAgenda", schema)
    else:
        ix = open_dir("indexAgenda")
        
    writer = ix.writer()
    fichero=open("Agenda/agenda.txt")
    texto=fichero.read()
    textoPorPartes=(texto.split("\n"))
    for n in range(0,len(textoPorPartes),2):
        writer.add_document(email=unicode(textoPorPartes[n]),
                            nombreApellidos=unicode(textoPorPartes[n+1]))
    writer.commit()
    print("Agenda Indexada Correctamente")
        
def busqueda(remitente):        
    ix = open_dir("index")
    qp = QueryParser("remitente", schema=ix.schema)
    q = qp.parse(unicode(str(remitente)))
    s=ix.searcher()
    results = s.search(q)
    return results

def busquedaPorAsuntoCuerpo(aBuscar):        
    ix = open_dir("index")
    qp = MultifieldParser(["asunto","cuerpo"], schema=ix.schema)
    q = qp.parse(unicode(str(aBuscar)))
    s=ix.searcher()
    results = s.search(q)
    return results

def busquedaPorEmail(email):        
    ix = open_dir("indexAgenda")
    qp = QueryParser("email", schema=ix.schema)
    q = qp.parse(unicode(str(email)))
    s=ix.searcher()
    results = s.search(q)
    return results

def busquedaPorFecha(fecha):        
    ix = open_dir("index")
    qp = QueryParser("fecha", schema=ix.schema)
    query = unicode(raw_input(""))
    qp.add_plugin(DateParserPlugin())
    q = qp.parse(query)
    print(q)
    s=ix.searcher()
    results = s.search(q)
    print(results)
    for n in results:
        print n.get("fecha")
    return results

def ApartadoA(palabra):
    for n in busquedaPorAsuntoCuerpo(palabra):
        res=busquedaPorEmail(n.get("remitente"))
        print(res[0].get("nombreApellidos"))
        print(n.get("asunto"))

#def ApartadoB(fecha):

#borraCreaIndex()
#borraCreaIndexAgenda()
#print(date.datetime.now().strftime("%Y%m%d"))
busquedaPorFecha("20101015")

#ApartadoA("Gracias")