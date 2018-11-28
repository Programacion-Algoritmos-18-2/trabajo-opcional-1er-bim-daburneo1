from modelado.modelo import *

e = Equipo()
e.agregar_nombre_equipo("Manchester United")
e.agregar_pais("Inglaterra")

e2 = Equipo()
e2.agregar_nombre_equipo("Nexaca")
e2.agregar_pais("Mexico")

e3 = Equipo()
e3.agregar_nombre_equipo("Lazio")
e3.agregar_pais("Italia")

f = Futbolista()
f.agregar_nombre("Antonio")
f.agregar_apellido("Valencia")
f.agregar_equipo(e)
f.agregar_posicion("LATERAL")
f.agregar_dorsal(25)

print(f.presentar_datos())

f2 = Futbolista()
f2.agregar_nombre("Alex")
f2.agregar_apellido("Aguinaga")
f2.agregar_equipo(e2)
f2.agregar_posicion("MEDIOCENTRO")
f2.agregar_dorsal(7)

print(f2.presentar_datos())

f3 = Futbolista()
f3.agregar_nombre("Felipe")
f3.agregar_apellido("Caicedo")
f3.agregar_equipo(e3)
f3.agregar_posicion("DELANTERO")
f3.agregar_dorsal(32)

print(f3.presentar_datos())
