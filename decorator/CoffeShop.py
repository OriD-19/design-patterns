class Bebida:
    precio = 1.0
    toppings = []

    def calcular_precio(self):
        return self.precio


class LecheDescremada(Bebida):

    def __init__(self, drink: Bebida):
        self.drink = drink

    def calcular_precio(self):
        self.toppings.append("Leche Descremada")
        return self.drink.calcular_precio() + 0.5


class LecheDeSoya(Bebida):

    def __init__(self, drink: Bebida):
        self.drink = drink

    def calcular_precio(self):
        self.toppings.append("Leche de Soya")
        return self.drink.calcular_precio() + 0.75


class LecheDeCoco(Bebida):

    def __init__(self, drink: Bebida):
        self.drink = drink

    def calcular_precio(self):
        self.toppings.append("Leche de Coco")
        return self.drink.calcular_precio() + 1.0


class Canela(Bebida):

    def __init__(self, drink: Bebida):
        self.drink = drink

    def calcular_precio(self):
        self.toppings.append("Canela")
        return self.drink.calcular_precio() + 0.25


class CremaBatida(Bebida):

    def __init__(self, drink: Bebida):
        self.drink = drink

    def calcular_precio(self):
        self.toppings.append("Crema Batida")
        return self.drink.calcular_precio() + 1.50


class Saborizante(Bebida):

    def __init__(self, drink: Bebida):
        self.drink = drink

    def calcular_precio(self):
        self.toppings.append("Saborizante")
        return self.drink.calcular_precio() + 1.25


class BebidaMediana(Bebida):

    def __init__(self, drink: Bebida):
        self.drink = drink

    def calcular_precio(self):
        self.toppings.append("Bebida Mediana")
        return self.drink.calcular_precio() + 1.0


class BebidaGrande(Bebida):

    def __init__(self, drink: Bebida):
        self.drink = drink

    def calcular_precio(self):
        self.toppings.append("Bebida Grande")
        return self.drink.calcular_precio() + 2.0


decorators = [LecheDescremada, Canela, CremaBatida, Saborizante, Saborizante, BebidaGrande]

my_drink = Bebida()

for decorator in decorators:
    my_drink = decorator(my_drink)

print(f"Precio total: ${my_drink.calcular_precio():.2f}")
print("Toppings:", ", ".join(my_drink.toppings))

