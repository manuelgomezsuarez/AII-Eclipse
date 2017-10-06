# -*- coding: utf-8 -*-
'''
Created on 6 oct. 2017

@author: admin
'''
class Personaje(object):
    def __init__(self,vida,posicion,velocidad):
        self.vida=vida
        self.posicion=posicion
        self.velocidad=velocidad
    def recibirAtaque(self,dano):
        if self.vida<=0:
            print("Vidas agotadas, Game Over")
        if dano:
            self.vida=self.vida-dano
            print("Has recibido daño,  vida actual:"+ str(self.vida))
        return self.vida
    def mover(self,direccion):
        if direccion==("left"):
            self.posicion-=self.velocidad
            print("posicion actual: "+str(self.posicion))
        elif direccion=="right":
            self.posicion+=self.velocidad
            print("posicio actual: "+str(self.posicion))
        else:
            print("direccion incorrecta, no se ha desplazado nada.")
            
        return self.posicion
    
class Soldado(Personaje):
    def __init__(self,vida,posicion,velocidad,ataque):
        Personaje.__init__(self,vida,posicion,velocidad)
        self.ataque=ataque
    
    def atacar(self,personaje):
        if personaje.vida>0:
            personaje.vida-=self.ataque
            print("Le has hecho: "+str(self.ataque))+" puntos de daño"
            print("Su vida actual es de: "+str(personaje.vida))
        else:
            print("El personaje ya esta muerto, no es posible atacar")
            
class Campesino(Personaje):
    def __init__(self,cosecha):
        self.cosecha=cosecha
    def cosechar(self,cantidad):
        if cantidad>0:
            self.cosecha+=cantidad
            print("Cantidad cosechada: "+str(self.cosecha))
    
personajeTest=Personaje(9,0,2)
personajeTest.recibirAtaque(2)
personajeTest.mover("left")
soldadoTest=Soldado(9,0,2,4)
soldadoTest.atacar(personajeTest)
campesinoTest=Campesino(100)
campesinoTest.cosechar(150)
