import random

class Customer:
    
    def __init__(self, name: str, active: bool, country: str, expenses: float):
        self.name = name
        self.active = active
        self.country = country
        self.expenses = expenses

    def __str__(self):
        return f"{self.name} - {self.country} - ${self.expenses:.2f}"

    def __repr__(self):
        return f"{self.name} - {self.country} - ${self.expenses:.2f}"

class CustomerQuery:

    def __init__(self, customer_repo: list[Customer]):
        self.customer_repo = customer_repo

    def active_clients(self):
        self.customer_repo = [customer for customer in self.customer_repo if customer.active]
        return self

    def from_country(self, country: str):
        self.customer_repo = [customer for customer in self.customer_repo if customer.country == country]
        return self

    def with_min_spent(self, limit: float):
        self.customer_repo = [customer for customer in self.customer_repo if customer.expenses > limit]
        return self

    def result(self):
        return self.customer_repo

nombres = [
    "María", "José", "Ana", "Juan", "Carmen", "Antonio", "Dolores", "Francisco",
    "Isabel", "Manuel", "Pilar", "David", "Josefa", "Jesús", "Teresa", "Javier",
    "Rosario", "Daniel", "Francisca", "Rafael", "Mercedes", "Miguel", "Antonia",
    "Alejandro", "Lucía", "Fernando", "Elena", "Carlos", "Rosa", "Diego"
]

apellidos = [
    "García", "Rodríguez", "González", "Fernández", "López", "Martínez", "Sánchez",
    "Pérez", "Gómez", "Martín", "Jiménez", "Ruiz", "Hernández", "Díaz", "Moreno",
    "Muñoz", "Álvarez", "Romero", "Alonso", "Gutiérrez", "Navarro", "Torres",
    "Domínguez", "Vázquez", "Ramos", "Gil", "Ramírez", "Serrano", "Blanco", "Molina"
]


def generar_nombre_completo():
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    return f"{nombre} {apellido}"

countries = ["USA", "SV", "GT", "HN"]

customers = []

for i in range(30):
    customers.append(Customer(generar_nombre_completo(), i % 2 == 1, random.choice(countries), random.random() * (i + 2000))) 

query = CustomerQuery(customers)

query.active_clients().from_country("USA").with_min_spent(20)

for customer in query.result():
    print(customer)
