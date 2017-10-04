# -*- coding: utf-8 -*-
'''
Created on 3 oct. 2017

@author: Admin
'''
class Corcho(object):
    def __init__(self,bodega=""):
        if bodega:
            self.bodega=bodega
        else:
            raise AttributeError("Nombre de bodega incorrecto, no lo deje vacio")
        
    def __str__(self):
        return "La Bodega del corcho es:"+str(self.bodega)

class Botella(object):
    def __init__(self,Corcho=""):
        if Corcho:
            self.corchoPuesto=Corcho
        else:
            self.corchoPuesto=None
            
    def __str__(self):
        if not self.corchotapado:
            return "La botella esta destapada"
        else :
            return "La botella esta tapada y tiene el corcho :"+str(self.corchotapado)            
            
       

class Sacacorchos(object):
    """Abstraccion de la clase Sacacorchos"""
    def __init__(self,botella="",corcho=""):
        """Constructor de la clase Botella"""
        self.botella=botella
        self.corchotapado=corcho
    def __str__(self):
        return "Tengo la botella : "+str(self.botella)+" y el corcho : "+str(self.corchotapado)
    def destapar(self):
        """Saca el corcho de la botella"""
        if self.corchotapado!=None:
            corchodestapado=self.corchotapado
            self.corchotapado=None
            print("Corcho Destapado")
            return corchodestapado
        else :
            raise AttributeError("La botella ya esta destapada")
    def limpiar(self,destapar):
        """Saca el corcho del sacacorchos,o levanta una excepcion en el caso de que no tenga corcho el mismo"""
        if destapar!=None:
            self.corchotapado=None
            print("sacacorchos limpio")
        else:
            raise AttributeError("El sacacorchos no tiene corcho")
        
        
corcho=Corcho("Bodega Garcia Velazquez")
botella=Botella("true")
sacacorchos= Sacacorchos(botella,corcho)
sacacorchos.destapar()


        
        