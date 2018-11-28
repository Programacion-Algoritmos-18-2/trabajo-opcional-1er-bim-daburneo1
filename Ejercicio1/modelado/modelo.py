class Equipo(object):
    def __init__(self):
        self.nombre_equipo = ""
        self.pais = ""

    def agregar_nombre_equipo(self, ne):
        self.nombre_equipo = ne

    def obtener_nombre_equipo(self):
        return self.nombre_equipo

    def agregar_pais(self, p):
        self.pais = p

    def obtener_pais(self):
        return self.pais

class Futbolista(object):
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.equipo = ""
        self.posicion = ""
        self.dorsal = 0

    def agregar_nombre(self, n):
        self.nombre = n

    def obtener_nombre(self):
        return self.nombre

    def agregar_apellido(self, a):
        self.apellido = a

    def obtener_apellido(self):
        return self.apellido

    def agregar_equipo(self, e):
        self.equipo = e

    def obtener_equipo(self):
        return self.equipo

    def agregar_posicion(self, p):
        self.posicion = p

    def obtener_posicion(self):
        return self.posicion

    def agregar_dorsal(self, d):
        self.dorsal = d

    def obtener_dorsal(self):
        return self.dorsal

    def presentar_datos(self):
        return "Jugador:\n\t%s %s, \n\tpertenece al equipo %s del pais %s,\n\tsu posicion es %s y \n\tsu dorsal es el numero %d" % (self.obtener_nombre(), self.obtener_apellido(), self.obtener_equipo().obtener_nombre_equipo(), self.obtener_equipo().obtener_pais(), self.obtener_posicion(), self.obtener_dorsal())     
        