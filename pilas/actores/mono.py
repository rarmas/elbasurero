# -*- encoding: utf-8 -*-
# Pilas engine - A video game framework.
#
# Copyright 2010 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar

from pilas.actores import Actor
import pilas

class Mono(Actor):
    """Representa la cara de un mono de color marrón.

    Este personaje se usa como ejemplo básico de un actor. Sus
    métodos mas usados son:

    - sonreir
    - gritar

    El primero hace que el mono se ría y el segundo que grite.
    """

    def __init__(self, x=0, y=0):
        # carga las imagenes adicionales.
        self.image_normal = pilas.imagenes.cargar('monkey_normal.png')
        self.image_smile = pilas.imagenes.cargar('monkey_smile.png')
        self.image_shout = pilas.imagenes.cargar('monkey_shout.png')

        self.sound_shout = pilas.sonidos.cargar('shout.wav')
        self.sound_smile = pilas.sonidos.cargar('smile.wav')

        # Inicializa el actor.
        Actor.__init__(self, self.image_normal, x=x, y=y)
        self.radio_de_colision = 50

    def sonreir(self):
        self.definir_imagen(self.image_smile)
        # Luego de un segundo regresa a la normalidad
        pilas.mundo.agregar_tarea_una_vez(0.5, self.normal)
        self.sound_smile.reproducir()

    def gritar(self):
        self.definir_imagen(self.image_shout)
        # Luego de un segundo regresa a la normalidad
        pilas.mundo.agregar_tarea_una_vez(1, self.normal)
        self.sound_shout.reproducir()

    def normal(self):
        self.definir_imagen(self.image_normal)

    def decir(self, mensaje):
        self.sonreir()
        Actor.decir(self, mensaje)
