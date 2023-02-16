class Persona:
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""

    def verNombre(self):
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verGenero(self):
        return self.__genero
    def asignarNombre(self, rol):
        self.__nombre = input('Ingrese el nombre del '+ rol +': ')
    def asignarCedula(self, rol):
        self.__cedula = int(input("Ingrese la cedula del " + rol +": "))
    def asignarGenero(self, rol):
        self.__genero = input("Ingrese el genero del " + rol +": ")


class Paciente(Persona):
    def __init__(self):
        self.__servicio = ""
    def asignarServicio(self,rol):
        self.__servicio = input('Ingrese el servicio del '+ rol +': ')
    def verServicio(self):
        return self.__servicio

class Sistema(Paciente):
    def __init__(self):
        self.__lista_pacientes = []      

    def numPacientes(self):
        self.__numero_paciente = len(self.__lista_pacientes)
        return self.__numero_paciente


    def ingresarPaciente(self, rol):
        p = Paciente()
        p.asignarNombre(rol)
        p.asignarCedula(rol)
        p.asignarGenero(rol)
        p.asignarServicio(rol)

        self.__lista_pacientes.append(p)
        print ("el numero de pacientes es: "+ str(self.numPacientes()))

class Empleado_Hospital(Persona):
    def __init__(self):
        self.__turno = ""
    def asignarTurno(self, turno):
        self.__turno = turno
    def verTurno(self):
        return self.__turno

class Enfermera(Empleado_Hospital):
    def __init__(self):
        self.__rango = ""
    def asignarRango(self,rango):
        self.__rango = rango
    def verRango(self):
        return self.__rango

class Medico(Empleado_Hospital):
    def __init__(self):
        self.__especialidad = ""
    def asignarEspecialidad(self, especialidad):
        self.__especialidad = especialidad
    def verEspecialidad(self):
        return self.__especialidad

p1 = sistema()
p2 = Paciente()
p1.ingresarPaciente('Paciente')
#p1.asignarNombre("Pepe")
#p1.asignarCedula(123456)
#p1.asignarGenero("Hombre")
#print (p1.verNombre())