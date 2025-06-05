from enum import Enum


class User:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return "Usuario: " + self.name


class PaymentMethod(Enum):
    CREDIT_CARD = 1
    PAY_PAL = 2
    CASH_ON_DELIVERY = 3  # forma rara de decir "contra-entrega"


def print_payment_method(pm: PaymentMethod) -> str:
    repr = ""

    if pm.value == 1:
        repr = "Tarjeta de credito"
    elif pm.value == 2:
        repr = "PayPal"
    elif pm.value == 3:
        repr = "Contra-entrega"
    
    return repr


class Product:
    name: str
    price: float

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"Producto {self.name}, ${self.price:.2f}"


class Order:

    user: User | None
    products: list[Product]
    addr: str
    payment_method: PaymentMethod | None
    discount: float
    total_cost: float

    def __init__(self) -> None:
        """
        Todos los valores inician como None o vacios por defecto
        """
        self.user = None
        self.products = []
        self.addr = ""
        self.payment_method = None
        self.discount = 0.0
        self.total_cost = 0.0

    def __str__(self) -> str:
        return f"""
        Orden de: {self.user.name if self.user else ""}
        Productos: {', '.join([f"{product.name} (${product.price:.2f})" for product in self.products])}
        Direccion: {self.addr}
        Pago: {print_payment_method(self.payment_method) if self.payment_method else "Contra-entrega"}
        Descuento: {(self.discount * 100):.2f}%
        Total a pagar: ${self.total_cost:.2f}
        """


class OrderBuilder:

    order: Order

    def __init__(self) -> None:
        self.order = Order()

    def add_user(self, user: User):
        self.order.user = user
        return self

    def add_product(self, product: Product):
        self.order.products.append(product)
        return self

    def add_delivery_address(self, addr: str):
        self.order.addr = addr
        return self

    def add_payment_method(self, payment_method: PaymentMethod):
        self.order.payment_method = payment_method
        return self

    def add_discount(self, discount: float):
        if discount >= 1.0:
            raise ValueError("El descuento no puede ser de mas del 100%")
        elif discount < 0:
            raise ValueError("El descuento no pude ser menor de 0%")

        self.order.discount = discount
        return self

    def build(self) -> Order:
        return self.order


class OrderCalculator:

    @staticmethod
    def calculate_total_order(order: Order) -> float:
        total_items = sum([product.price for product in order.products])
        return total_items * (1 - order.discount)


order_builder = OrderBuilder()
user = User("Carlitos Martinez")

order = (
    order_builder.add_user(user)
    .add_product(Product("Laptop", 1200))
    .add_product(Product("Mouse", 50))
    .add_delivery_address("Pesherman Calle Wallabi 2 Sidney")
    .add_payment_method(PaymentMethod.CASH_ON_DELIVERY)
    .add_discount(0.1)
    .build()
)

order.total_cost = OrderCalculator.calculate_total_order(order)

print(order)
