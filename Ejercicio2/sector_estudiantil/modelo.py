class Alumno(object):
    def __init__(self):
        self.nombre = ""
        self.docente_matematica = ""
        self.docente_sociales = ""

    def agregar_nombre(self, n):
        self.nombre = n

    def obtener_nombre(self):
        return self.nombre

    def agregar_docente_matematica(self, dm):
        self.docente_matematica = dm

    def obtener_docente_matematica(self):
        return self.docente_matematica

    def agregar_docente_sociales(self, ds):
        self.docente_sociales = ds

    def obtener_docente_sociales(self):
        return self.docente_sociales
    
    def presentar_datos(self):
        cadena = "\tDatos de estudiante: %s\nNombre Docente Matematica: %s \nApellido Docente Matematica: %s\n Titulo: %s \nNombre Docente Sociales: %s \nApellido Docente Sociales: %s \nTitulo: %s" %(self.obtener_nombre(), 
            self.obtener_docente_matematica().obtener_nombre(), self.obtener_docente_matematica().obtener_apellido(), self.obtener_docente_matematica().obtener_titulo(), 
            self.obtener_docente_sociales().obtener_nombre(), self.obtener_docente_sociales().obtener_apellido(), self.obtener_docente_sociales().obtener_titulo())
        return cadena