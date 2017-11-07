# -*- coding: utf-8 -*-
'''
Created on 7 nov. 2017

@author: Admin
'''
from whoosh.index import *
from whoosh.fields import *
from whoosh.qparser import QueryParser
import shutil
import os

def borraCreaIndex():
    if os.path.exists("index"):
        shutil.rmtree("index")
    schema = Schema(remitente=KEYWORD(stored=True), destinatarios=KEYWORD(stored=True), asunto= KEYWORD(stored=True), cuerpo= TEXT(stored=True))
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
            textoPorPartes=(texto.split("\n",3))
            writer.add_document(remitente=unicode(textoPorPartes[0]),destinatarios=unicode(textoPorPartes[1]),asunto=unicode(textoPorPartes[2]),cuerpo=unicode(textoPorPartes[3]))
            numeroFichero=numeroFichero+1
            print(textoPorPartes)
        except Exception as ex:
            print(ex)
            print("No hay mas ficheros")
            writer.commit()
            quedanFicheros=False
        
def busqueda(remitente):        
    ix = open_dir("index")
    qp = QueryParser("remitente", schema=ix.schema)
    q = qp.parse(unicode(str(remitente)))
    s=ix.searcher()
    results = s.search(q)
    for hit in results:
        print(hit.get("destinatarios"))
        print(hit.get("asunto"))
    return results