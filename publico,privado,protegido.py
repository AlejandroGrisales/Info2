class  Cosa:
    def __init__(self, publico:str = "publico", protegido: str = "protegido", privado:str = "privado"):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado

    def informacion(self):
        print(
            (
                f"Esta es una clase con un atributo publico: {self.publico}, "
                f"un atributo protegido: {self._protegido}, "
                f"y un atributo privado: {self.__privado}"
            )
        )
    #def revelar_privado(self):
     #   return f"El atributo privado es {self.__privado}"

a = Cosa()
#a.informacion()
print (a.publico)
print (a._protegido)
print (a.__privado)