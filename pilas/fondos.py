# -*- encoding: utf-8 -*-
# pilas engine - a video game framework.
#
# copyright 2010 - hugo ruscitti
# license: lgplv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# website - http://www.pilas-engine.com.ar

import pilas

class Fondo(pilas.actores.Actor):

    def __init__(self, imagen):
        pilas.actores.Actor.__init__(self, imagen)
        self.z = 1000

class Volley(Fondo):
    "Muestra una escena que tiene un fondo de pantalla de paisaje."

    def __init__(self):
        Fondo.__init__(self, "fondos/volley.png")

class Pasto(Fondo):
    "Muestra una escena que tiene un fondo de pantalla de paisaje."

    def __init__(self):
        Fondo.__init__(self, "fondos/pasto.png")

class Selva(Fondo):
    "Muestra una escena que tiene un fondo de pantalla de paisaje."

    def __init__(self):
        Fondo.__init__(self, "fondos/selva.png")


class Tarde(Fondo):
    "Representa una escena de fondo casi naranja."

    def __init__(self):
        Fondo.__init__(self, "fondos/tarde.png")


class Espacio(Fondo):
    "Es un espacio con estrellas."

    def __init__(self):
        Fondo.__init__(self, "fondos/espacio.png")

class Noche(Fondo):
    "Muestra una escena que tiene un fondo de pantalla de paisaje."

    def __init__(self):
        Fondo.__init__(self, "fondos/noche.png")

class Color(Fondo):
    
    def __init__(self, color):
        Fondo.__init__(self, "invisible.png")
        self.color = color
        self.lienzo = pilas.imagenes.cargar_lienzo()

    def dibujar(self, motor):
        if self.color:
            self.lienzo.pintar(motor, self.color)
