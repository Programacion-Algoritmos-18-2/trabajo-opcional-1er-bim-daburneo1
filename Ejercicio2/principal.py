from personal_academico.modelo import *
from sector_estudiantil.modelo import *

alumno = input("Ingrese el nombre del alumno: ")
d = Docente()
nombre = input("Nombre Docente: ")
d.agregar_nombre(nombre)
apellido = input("Apellido Docente: ")
d.agregar_apellido(apellido)
titulo = input("Titulo: ")
d.agregar_titulo(titulo)

d1 = Docente()
nombre = input("Nombre Docente: ")
d1.agregar_nombre(nombre)
apellido = input("Apellido Docente: ")
d1.agregar_apellido(apellido)
titulo = input("Titulo: ")
d1.agregar_titulo(titulo)

a = Alumno()
a.agregar_nombre(alumno)
a.agregar_docente_matematica(d)
a.agregar_docente_sociales(d1)
print(a.presentar_datos())