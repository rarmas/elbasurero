# -*- encoding: utf-8 -*-
# Pilas engine - A video game framework.
#
# Copyright 2010 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar

import pilas
from pilas.actores import Actor

class Pausa(Actor):

    def __init__(self, x=0, y=0):
        Actor.__init__(self, x=x, y=y)
        self.centro = ('centro', 'centro')
        self.imagen = "icono_pausa.png"
