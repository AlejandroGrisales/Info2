import pymongo

# Nota para la profe: Tecnicamente todo el codigo funciona tal como esta, lo unico que no pude resolver es como guardar los 
#                     multiples medicamentos y que se viera bonito cuando la selecciona la opcion 3 del menu "ver la informacio de una mascota". 
#                     


class Medicamento:
    def __init__(self,client):
        mydb = client["sistema_Veterinaria"]
        self.__medicamentos = mydb["medicamentos"]
        self.__lista_medicamentos = {}
    
    def verNombreMed(self):
        Nombre=list(self.__medicamentos.find())
        return Nombre[-1]['Nombre']
    
    def verListaMed(self):
        lista = self.__lista_medicamentos
        return lista
    
    def verDosis(self):
        Dosis=list(self.__medicamentos.find())
        print('La dosis suministrada es: ' + str(Dosis[-1]['Dosis']))

    def asignarMed(self):
        client = pymongo.MongoClient("mongodb+srv://AlejandroGrisalesP:alejandroinfo2@clustera.mmuq0jw.mongodb.net/?retryWrites=true&w=majority")
        db = client.test
        nm = int (input("\nIngrese la cantidad de medicamentos de la mascota: "))
        n = 0
        while n<nm:
            nombre_medicamento = input("Ingrese el nombre del medicamento #"+str(n+1)+": ")
            dosis = 0
            while True:
                valido = False
                while valido == False:
                    try:
                        m = int(input("ingrese la dosis #"+str(n+1)+": "))
                        valido = True
                    except ValueError:
                        print("ingrese un dato numerico ...")
                        continue
                if m>0:
                    dosis = m
                    break
                else:
                    print("Ingrese un valor valido (Mayor a 0)")
                    continue
            
            self.__lista_medicamentos = ({"Nombre_Medicamento"+str(n+1):nombre_medicamento,"Dosis"+str(n+1):dosis})
            n+=1       

class Mascota(Medicamento):
    def __init__(self,client):
        mydb = client["sistema_Veterinaria"]
        self.__Pacientes = mydb["Pacientes"]
        self.__nombre = ""
        self.__tipo = ""
        self.__num_historia = 0
        self.__peso = 0
        self.__fecha_ingreso = ""
        
    # Guardo toda la informacion como variable privadas, y luego las llamo y las guardo en la base de datos de atlas a la vez con una sola funcion
    def verNombre(self):
        return (self.__nombre) 
    def asignarNombre(self):
        nom = input("Ingrese el nombre de la mascota: ")
        self.__nombre =  nom
    
    def verTipo(self,tipo):
        for x in self.__Pacientes.find({'Tipo': tipo }):
            return print(x)
    def asignarTipo(self):
        tip = input("Ingrese el tipo de mascota: ")
        self.__tipo = tip 
    
    def verHistoria(self,historia):
        for x in self.__Pacientes.find({'Historia_Medica': historia }):
            return x   
    def asignarHistoria(self,his):
        self.__num_historia = his 
    
    def verPeso(self,peso):
        for x in self.__Pacientes.find({'Peso': peso }):
            return print(x)        
    def asignarPeso(self,pes):
        self.__peso = pes
        
    def verFechaIngreso(self,ingreso):
        for x in self.__Pacientes.find({'Fecha_Ingreso': ingreso }):
            return print(x)
    def asignarFechaIngreso(self):
        dia = 0
        while True:
            valido = False
            while valido == False:
                try:
                    d = int(input("Ingrese el Dia de ingreso de la mascota: "))
                    valido = True
                except ValueError:
                    print("ingrese un dato numerico ...")
            
            if d<=31 and d>=1:
                dia = d
                break
            else:
                print("Ingrese un valor valido (1-31)")
                continue

        mes = 0
        while True:
            valido = False
            while valido == False:
                try:
                    m = int(input("Ingrese el Mes de ingreso de la mascota: "))
                    valido = True
                except ValueError:
                    print("ingrese un dato numerico ...")
                    continue
            if m<=12 and m>=1:
                mes = m
                break
            else:
                print("Ingrese un valor valido (1-12)")
                continue
        
        año = 0
        while True:
            valido = False
            while valido == False:
                try:
                    a = int(input("Ingrese el Año de ingreso de la mascota: "))
                    valido = True
                except ValueError:
                    print("ingrese un dato numerico ...")
                    continue
            if a<=2023 and a>=1:
                año = a
                break
            else:
                print("Ingrese un valor valido (hasta 2023).")
                continue

        ing = str(dia)+"/"+str(mes)+"/"+str(año)
        self.__fecha_ingreso = ing 

    def ingresarInfo(self):
        client = pymongo.MongoClient("mongodb+srv://AlejandroGrisalesP:alejandroinfo2@clustera.mmuq0jw.mongodb.net/?retryWrites=true&w=majority")
        db = client.test
        med = Medicamento(client)
        info = {"Nombre":self.__nombre, "Tipo":self.__tipo, "Historia_Medica":self.__num_historia, "Peso":self.__peso, "Fecha_Ingreso":self.__fecha_ingreso, "Medicamentos": med.verListaMed()}
        self.__Pacientes.insert_one(info)
    
    def asignarMedicamentos(self):
        client = pymongo.MongoClient("mongodb+srv://AlejandroGrisalesP:alejandroinfo2@clustera.mmuq0jw.mongodb.net/?retryWrites=true&w=majority")
        db = client.test
        med = Medicamento(client)
        med.asignarMed()

class Sistema:
    def __init__(self):
        self.__lista_mascotas = []
    
    def verificarMascota(self,nhc):
        encontrado = False
        client = pymongo.MongoClient("mongodb+srv://AlejandroGrisalesP:alejandroinfo2@clustera.mmuq0jw.mongodb.net/?retryWrites=true&w=majority")
        db = client.test
        mydb = client["sistema_Veterinaria"]
        mycol = mydb["Pacientes"]
        ms = Mascota(client)
        
        valido = False
        try:
            for x in mycol.find({"Historia_Medica":nhc}):
                valido = True
        
        except ValueError:
            valido = False
            
        return valido
    
    def ingresarMascota(self,m):
        self.__lista_mascotas.append(m)
    
    def verNumeroMascotas(self):
        client = pymongo.MongoClient("mongodb+srv://AlejandroGrisalesP:alejandroinfo2@clustera.mmuq0jw.mongodb.net/?retryWrites=true&w=majority")
        db = client.test
        mydb = client["sistema_Veterinaria"]
        mycol = mydb["Pacientes"]
        n = 0
        for x in mycol.find():
            n+=1
        return(n)

    def eliminarMascota(self,nhc):
        client = pymongo.MongoClient("mongodb+srv://AlejandroGrisalesP:alejandroinfo2@clustera.mmuq0jw.mongodb.net/?retryWrites=true&w=majority")
        db = client.test
        mydb = client["sistema_Veterinaria"]
        mycol = mydb["Pacientes"]
        mycol.delete_one ( { "Historia_Medica":nhc } )
        if self.verificarMascota(nhc)== True:
            return False
        else:
            return True

    def recuperarMascota(self,nhc):
        #puedo mezclar metodos que ya he construido
        #1 buscar la posicion de la mascota
        client = pymongo.MongoClient("mongodb+srv://AlejandroGrisalesP:alejandroinfo2@clustera.mmuq0jw.mongodb.net/?retryWrites=true&w=majority")
        db = client.test
        mydb = client["sistema_Veterinaria"]
        mycol = mydb["Pacientes"]
        for x in mycol.find ( { "Historia_Medica":nhc } ):
            print (x)
    
    def verFechaIngresoMascota(self,nhc):
        m = self.recuperarMascota(nhc)
        ms = Mascota()
        if m == None:
            return "La mascota no está en el sistema"
        return ms.verFechaIngreso()

#funciones         
def ingresoNumerico(mensaje):
    valido = False
    while valido == False:
        try:
            valor = int(input(mensaje))
            valido = True
        except ValueError:
            print("ingrese un dato numerico ...")
    return valor

def main():
    #creamos el sistema
    sistema = Sistema()

    client = pymongo.MongoClient("mongodb+srv://AlejandroGrisalesP:alejandroinfo2@clustera.mmuq0jw.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    while True:
        opcion = ingresoNumerico("\nIngrese un numero:\n0 -- salir\n1 -- ingresar mascota\n2 -- eliminar\n3 -- Ver la informacion de una mascota\n4 -- ver numero de mascotas\n----> ")
        if opcion == 0:
            print("Fin del programa ...")
            break
        elif opcion == 4:
            print("El sistema tiene " + str(sistema.verNumeroMascotas()) + " mascotas")
        elif opcion == 3:
            #1. solicitar numero de historia clinica y ver que no este
            nhc = int(input("Ingrese Numero de Historia Clinica: "))
            if sistema.verificarMascota(nhc) == False:
                print("La mascota no esta en el sistema ...")
                continue
            #recupero la mascota de la base de datos
            else:
                sistema.recuperarMascota(nhc)
                

        elif opcion == 2:
            #1. solicitar numero de historia clinica y ver que no este
            nhc = int(input("Ingrese Numero de Historia Clinica: "))
            resultado = sistema.eliminarMascota(nhc)
            if resultado == True:
                print("Se elimino exitosamente la mascota del sistema ...")
            else:
                print("No se elimino la mascota del sistema, posiblemente no exista ...")
        elif opcion == 1:
            ms = Mascota(client)
            #1. debo verificar que haya espacio en el servicio
            if sistema.verNumeroMascotas() >= 10:
                print("No hay espacio ...")
                continue
            #2. solicitar numero de historia clinica y ver que no este
            nhc = ingresoNumerico("Ingrese Numero de Historia Clinica: ")
            if sistema.verificarMascota(nhc) == True:
                print("La mascota ya esta en el sistema ...")
                continue

            #3. Si la historia no esta pido los datos restantes
            
            # Ingresar el nombre de la mascota
            n = ms.asignarNombre()
            n2 = ms.verNombre()
            # Asignamos la historia ya comprobada
            h = ms.asignarHistoria(nhc)
            # Ingrese el tipo de animal
            t = ms.asignarTipo()
            # Ingresar el pesos de la mascota en kilogramos
            p2 = ingresoNumerico("Ingrese el pesos de la mascota en kilogramos: ")
            p = ms.asignarPeso(p2)
            # Ingresar la fecha dd/mm/aaaa
            f = ms.asignarFechaIngreso()
            lista_medicamentos = []

            #4. por cada medicamento solicito los datos
            ms.asignarMedicamentos()
            ms.ingresarInfo()
            
            #5. Ingresar la mascota al sistema
            sistema.ingresarMascota(ms)
            print("Mascota " + n2 + " ingresada ...")
        else:
            print("Opcion no valida: ")


if __name__ == '__main__':
    main()