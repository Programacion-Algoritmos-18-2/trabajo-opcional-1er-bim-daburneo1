class Garante(object):
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.sueldo = ""

    def agregar_nombre(self, n):
        self.nombre = n

    def obtener_nombre(self):
        return self.nombre

    def agregar_apellido(self, a):
        self.apellido = a

    def obtener_apellido(self):
        return self.apellido

    def agregar_sueldo(self, s):
        self.sueldo = s

    def obtener_sueldo(self):
        return self.sueldo

    def presentar_datos(self):
    	cadena = ("Nombre: %s \n \tApellido: %s \n \tSueldo:%s ") % (self.obtener_nombre(), self.obtener_apellido(), self.obtener_sueldo())
    	return cadena

class Prestamo(object):
    def __init__(self):
        self.nombre_beneficiario = ""
        self.sueldo = 0
        self.monto_prestamo = 0
        self.interes = 0
        self.tiempo_prestamo_anios = 0
        self.garante = ""

    def agregar_nombre_beneficiario(self, nb):
        self.nombre_beneficiario = nb

    def obtener_nombre_beneficiario(self):
        return self.nombre_beneficiario

    def agregar_sueldo(self, s):
        self.sueldo = s

    def obtener_sueldo(self):
        return self.sueldo

    def agregar_monto_prestamo(self, mp):
        self.monto_prestamo = mp

    def obtener_monto_prestamo(self):
        return self.monto_prestamo

    def agregar_interes(self, i):
        self.interes = i

    def obtener_interes(self):
        return self.interes

    def agregar_tiempo_prestamo_anios(self, tpa):
        self.tiempo_prestamo_anios = tpa

    def obtener_tiempo_prestamo_anios(self):
        return self.tiempo_prestamo_anios

    def agregar_garante(self, g1):
        self.garante = g1

    def obtener_garante(self):
        return self.garante

    def presentar_datos(self):
        cadena = "Nombre: %s \nSueldo %d \nMonto del prestamo: %d \nInteres: %s \nTiempo del prestamo en años: %d \nGarante: " % (self.obtener_nombre_beneficiario(), self.obtener_sueldo(), self.obtener_monto_prestamo(), self.obtener_interes(), self.obtener_tiempo_prestamo_anios())
        return cadena

class PrestamosAutomovil(Prestamo):
    def __init__(self):
        super(PrestamosAutomovil, self).__init__()
        self.tipo_vehiculo = ""
        self.marca_vehiculo = ""
        self.garante2 = ""

    def agregar_tipo_vehiculo(self, tv):
        self.tipo_vehiculo = tv

    def obtener_tipo_vehiculo(self):
        return self.tipo_vehiculo

    def agregar_marca_vehiculo(self, mv):
        self.marca_vehiculo = mv

    def obtener_marca_vehiculo(self):
        return self.marca_vehiculo

    def agregar_garante2(self, g2):
        self.garante2 = g2

    def obtener_garante2(self):
        return self.garante2

    def presentar_datos(self):
        cadena = "\n\tPrestamo Vehiculo: \n %s\n\t %s \nTipo de vehiculo: %s\n Marca de Vehiculo: %s\n Segundo Garante:\n " % (super(PrestamosAutomovil, self).presentar_datos(), self.obtener_garante().presentar_datos(), self.obtener_tipo_vehiculo(), self.obtener_marca_vehiculo())
        return cadena
