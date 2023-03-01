import pymongo


class Medicamento:
    def __init__(self,client):
        mydb = client["sistVete"]
        self.__medicamentos = mydb["medicamento"]

    def verNombre(self,nombre):
        for x in self.__medicamentos.find({'Nombre': nombre }):
            return print(x)        
    def asignarNombreDosis(self, nombre_med, dosis):
        self.__medicamento = self.__medicamentos.insert_one({"Nombre":nombre_med, "Dosis":dosis})
        return self.__medicamento

def main():
    client = pymongo.MongoClient("mongodb+srv://AlejandroGrisalesP:alejandroinfo2@clustera.mmuq0jw.mongodb.net/?retryWrites=true&w=majority")
    db = client.test   
    nm = int (input("ingrese la cantidad de medicamento de la mascota"))
    n= 0
    while n<nm:
        nombre_medicamento = input("Ingrese el nombre del medicamento: ")
        dosis = int(input("ingrese la dosis: "))
        medicamento = Medicamento(client)
        medicamento.asignarNombreDosis(nombre_medicamento,dosis)
        medicamento.verNombre("Dolex")
        n+=1
if __name__=="__main__":
    main()

# class Mascota:
#     def __init__(self):
#         self.__nombre = ""
#         self.__historia = 0
#         self.__tipo = ""
#         self.__peso = 0
#         self.__fecha_ingreso = ""
#         self.__medicamento = ""
