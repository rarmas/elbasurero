import pilas
# Permite que este ejemplo funcion incluso si no has instalado pilas.
import sys
sys.path.insert(0, "..")

pilas.iniciar()
actor = pilas.actores.Actor()


pilas.avisar("Este es un ejemplo de actor creado pero sin imagen.")
pilas.ejecutar()
