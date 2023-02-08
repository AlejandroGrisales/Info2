class ave:
    # Constructor de ave en su forma abstracta o basica
    def __init__(self, tipo, vuela):
        self.ave = tipo  # referente a si es carnivora, insectivora, omnivora, carroñera, etc
        self.vuelo = vuela
        self.oviparos = True
        self.pico= True

    def comer(self, comida):
        print("Este tipo de ave come usualmente: ", comida)

    def volar(self):
        print("Este tipo de ave puede volar: ", self.vuelo)

class ganso(ave):
    def __init__(self, tipo, vuela, accion, pata):
        # Invoca al constructor de clase ave
        ave.__init__(self, tipo, vuela)
        # Nuevos atributos
        self.habilidad = accion #puede volar y/o nadar
        self.patas = pata

    def destreza(self):
        print("Esta ave puede: ", self.habilidad)

class pato(ganso):
    pass

class gallina(ave):
    pass

p = ave("gallina", False)
p.volar()
p.comer("maiz")

g=ganso("carnivoro",True,"nadar","4")
g.destreza