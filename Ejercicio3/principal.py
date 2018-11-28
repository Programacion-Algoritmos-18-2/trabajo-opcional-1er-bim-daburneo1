from modelado.modelo import *

g1 = Garante()
g1.agregar_nombre("Juan")
g1.agregar_apellido("Velez")
g1.agregar_sueldo(700)

g2 = Garante()
g2.agregar_nombre("Patricio")
g2.agregar_apellido("Ordoñez")
g2.agregar_sueldo(2500)

p = Prestamo()
p.agregar_nombre_beneficiario("David")
p.agregar_sueldo(1200)
p.agregar_monto_prestamo(7000)
p.agregar_interes(4.18)
p.agregar_tiempo_prestamo_anios(4)
p.agregar_garante(g1)

print(p.presentar_datos(), g1.presentar_datos())

p2 = PrestamosAutomovil()
p2.agregar_nombre_beneficiario("Pedro")
p2.agregar_sueldo(1700)
p2.agregar_monto_prestamo(11000)
p2.agregar_interes(5.16)
p2.agregar_tiempo_prestamo_anios(5)
p2.agregar_garante(g1)
p2.agregar_tipo_vehiculo("Jeep")
p2.agregar_marca_vehiculo("Mitsubishi")
p2.agregar_garante2(g2)

print(p2.presentar_datos(), g2.presentar_datos())