import pymongo


class Medicamento:
    def __init__(self,client):
        mydb = client["sistVete"]
        self.__medicamentos = mydb["medicamento"]

    def verNombre(self):
        return self.__nombre
    #def verDosis

class Mascota:
    def __init__(self):
        self.__nombre = ""
        self.__historia = 0
        self.__tipo = ""
        self.__peso = 0
        self.__fecha_ingreso = ""
        self.__medicamento = ""
