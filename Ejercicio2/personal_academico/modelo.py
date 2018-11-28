class Docente(object):
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.titulo = ""

    def agregar_nombre(self, n):
        self.nombre = n

    def obtener_nombre(self):
        return self.nombre

    def agregar_apellido(self, a):
        self.apellido = a

    def obtener_apellido(self):
        return self.apellido

    def agregar_titulo(self, t):
        self.titulo = t

    def obtener_titulo(self):
        return self.titulo

    def presentar_datos(self):
        cadena = "\tDatos del docente: \nNombre: %s \tApellido: %s \tTitulo: %s" %(self.obtener_nombre(), self.obtener_apellido(), self.obtener_titulo())