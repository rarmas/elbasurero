# -*- encoding: utf-8 -*-
# Pilas engine - A video game framework.
#
# Copyright 2010 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar

from pilas.actores import Actor
import pilas

class Basura(Actor):
    "Representa un bloque que tiene fisica como una caja."

    def __init__(self, x=0, y=0,tipo=0):
        if tipo==0:
            imagen = pilas.imagenes.cargar('basura1.png')
        elif tipo==1:
            imagen = pilas.imagenes.cargar('basura2.png')
        elif tipo==2:
            imagen = pilas.imagenes.cargar('basura3.png')
        Actor.__init__(self, imagen)
        self.tipo = tipo
        self.rotacion = 0
        self.x = x
        self.y = y
        self.radio_de_colision = 20


