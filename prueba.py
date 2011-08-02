import random
import pilas
from basura import Basura
pilas.iniciar()

velocidad = 5
GRAVEDAD = 0.9

class var:
    dy = 0
    colision = False
    gravedad = True

class variables:
    velocidad = 5


class tiles:
    def __init__(self):
        self.tiles = []

    def agregar_tile(self, y, x, ruta):
        img = pilas.imagenes.cargar(ruta)
        tile = pilas.actores.Actor(img)

        tile.x = (32 * (x - 10)) + 16
        tile.y = (32 * (-y + 7))

        self.tiles.append(tile)

class Bolsa():

    def __init__(self, x=0, y=0):
        self.basuras = []
        self.limite = 5
        self.x = x
        self.y = y

    def agregar_basura(self, basura):
        if len(self.basuras) < self.limite:
            self.basuras.append(Basura(tipo=basura.tipo))
            basura.eliminar()
            self.mostrar()

    def mostrar(self):
        for i in range(len(self.basuras)):
            self.basuras[i].definir_posicion(self.x + i * 30 + 5, self.y)

#capas = layers(modo = 'manual')
#
##capas.agregar('cielo.png')
#capas.agregar('montes.png', 1, sentido = -1)
#capas.agregar('pasto.png', 3, sentido = -1, y = -120)
#capas.agregar('arboles.png', 4, sentido = -1, y = -90)

bolsa = Bolsa(-200, -200 )
tilset = tiles()

# suelo
for i in range(40):
    tilset.agregar_tile(14, i, 'b.png')


imagen = pilas.imagenes.cargar("cuadrado.png")
caja = pilas.actores.Actor(imagen)
caja.centro = ("centro", "abajo")

basuras = []



def crear_basura():
    if len(basuras) < 10:
        b = Basura(random.randint(-300,300),200,random.randint(0,2))
        b.centro = ("centro", "abajo")
        b.aprender(pilas.habilidades.RebotaComoPelota)
        basuras.append(b)

def press(evento):
    caja.y -= var.dy
    var.dy += GRAVEDAD
    if var.dy >= 0:
        if var.colision == False:
            var.gravedad = True

    if caja.y <= -240:
        var.dy = 0
        caja.y = -240

    for i in tilset.tiles:
        if var.gravedad == True:
            if i.colisiona_con_un_punto(caja.x, caja.y):
                var.colision = True
                var.dy = 0
                caja.y = (i.y + 16)
            else:
                var.colision = False

    for i in basuras:
        if var.gravedad == True:
            if i.colisiona_con_un_punto(caja.x, caja.y):
                bolsa.agregar_basura(i)
                basuras.remove(i)

    if pilas.mundo.control.izquierda:
        caja.x -= velocidad

    if pilas.mundo.control.derecha:
        caja.x += velocidad

    if var.dy == 0:
        var.colision = False
        if pilas.mundo.control.arriba:
            var.gravedad = False
            var.dy = -10



pilas.mundo.agregar_tarea_siempre(1, crear_basura)



pilas.eventos.actualizar.conectar(press)

pilas.ejecutar()
