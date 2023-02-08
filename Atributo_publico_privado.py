class Ejemplo:
    __atributo_privado = "soy un atributo privado"

    def __metodo_privado(self):
        print("soy un metodo privado")
    def atributo_publico(self):
        return self.__atributo_privado
    def metodo_publico(self):
        return self.__metodo_privado()

e = Ejemplo()
print(e.atributo_publico())
e.metodo_publico()