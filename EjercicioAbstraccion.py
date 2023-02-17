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
        self.__lista_nombre = []
        self.__lista_cedula = []
        self.__lista_genero = []
        self.__diccionario_pacientes = {}    

    def numPacientes(self):
        self.__numero_paciente = len(self.__lista_pacientes)
        return self.__numero_paciente

    def ingresarPaciente(self, rol):
        p = Paciente()
        p.asignarNombre(rol)
        p.asignarCedula(rol)
        p.asignarGenero(rol)
        p.asignarServicio(rol)
        #self.__lista_pacientes.append(p.guardarInfo())
        self.__lista_nombre.append(p.verNombre())
        self.__lista_cedula.append(p.verCedula())
        self.__lista_genero.append(p.verGenero())
        self.__diccionario_pacientes.update({'Nombre':self.__lista_nombre,'Cedula':self.__lista_cedula,'Genero':self.__lista_genero})
        #print(self.__lista_pacientes)
        print(self.__diccionario_pacientes)
        print(self.numPacientes())
        #print

    def verDatosPacientesLista(self):
        cedula = str(input('ingresar la cedula del paciente que busca en la lista: '))
        for c in self.__lista_pacientes:
            if cedula == c[1]:
                return print(c)

    def verDatosPacientesDiccionario(self):
        cedula == str(input('ingresar la cedula del paciente que busca en el diccionario: '))
        for p,c in enumerate(self.__diccionario_pacientes["cedula"]):
            if cedula == self.__diccionario_pacientes["cedula"]:
                return print(self.__diccionario_pacientes["cedula"][p])



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

def main():
    s = Sistema()

    while True:
        opcion = int(input("1. Nuevo Paciente\n2. Numero de Pacientes\n3. Datos Paciente\n4. Salir\n---> "))
        if opcion == 1:
            s.ingresarPaciente("Paciente")
        elif opcion == 2:
            print("Ahora hay: " + str(s.verNumeroPaciente() + " Pacientes"))
        elif opcion == 3:
            print(s.verDatosPaciente())
        elif opcion == 4:
            break
        else:
            print("Opcion Invalida")

if __name__ == '__main__':
    main()