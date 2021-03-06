# -*- encoding: utf-8 -*-
# Pilas engine - A video game framework.
#
# Copyright 2010 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar

from pilas.actores import Actor

class Ejes(Actor):
    "Representa el eje de coordenadas tomado como sistema de referencia."

    def __init__(self, x=0, y=0):
        Actor.__init__(self, "ejes.png", x=x, y=y)
        self.z = 100
