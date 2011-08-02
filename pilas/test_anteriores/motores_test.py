# -*- encoding: utf-8 -*-
import random
import unittest
import pilas
import pilas.motores
from time import sleep as pausa

class AbstractTest():

    def iniciar(self):
        self.motor.crear_ventana(320, 240, "test")
        self.motor.centrar_ventana()

        # A partir de ahora todas las llamadas internas de
        # pilas se delegan en este motor.
        pilas.motor = self.motor

    def test_creacion_de_ventana(self):
        self.iniciar()

    def test_control(self):
        self.iniciar()
        import pilas.control

        c = pilas.control.Control()
        c.actualizar()

        self.assertFalse(c.izquierda)
        self.assertFalse(c.derecha)
        
    def test_camara(self):
        #pilas.motor.definir_centro_de_la_camara(0, 0)
        pass

    def test_eventos(self):
        pilas.motor.procesar_y_emitir_eventos()

    def test_pantalla(self):
        pilas.motor.actualizar_pantalla()

    def test_colores(self):
        self.iniciar()
        import pilas.colores
        pilas.colores.gris

    def test_cargar_image(self):
        self.iniciar()
        import pilas.imagenes
        imagen1 = pilas.imagenes.cargar("./ceferino.png")
        imagen2 = pilas.motor.cargar_imagen("./ceferino.png")
        self.assertEquals(imagen1.__class__, imagen2.__class__)

class TestPygameMotor(unittest.TestCase, AbstractTest):
    "Verifica que todas las llamadas a pygame funcionan correctamente."

    def setUp(self):
        self.motor = pilas.motores.Pygame()

class TestPySFMLMotor(unittest.TestCase, AbstractTest):
    "Verifica que todas las llamadas a pySFML funcionan correctamente."

    def setUp(self):
        self.motor = pilas.motores.pySFML()

if __name__ == '__main__':
    unittest.main()
