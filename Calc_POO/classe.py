class Forma():
    def _init_(self):
        self.area=0.0
        self.perimetro=0.0

class Retangulo(Forma):
    def _init_(self):
        super()._init_()
    def calculoArea(self, base, altura):
        self.area = base * altura
        print(f"A aréa do retângulo é: {self.area}")

    def calculoPerimetro(self, base, altura):
        self.perimetro = 2*(base * altura)
        print(f"O perimetro do retângulo é: {self.perimetro}")

class Triangulo(Forma):
    def _init_(self):
        super()._init_()
    def calculoArea(self, base, altura):
        self.area = (base * altura)/2
        print(f"A aréa do triângulo é: {self.area}")

    def calculoPerimetro(self, l1, l2, l3):
        self.perimetro = l1+l2+l3
        print(f"O perimetro do triângulo é: {self.perimetro}")