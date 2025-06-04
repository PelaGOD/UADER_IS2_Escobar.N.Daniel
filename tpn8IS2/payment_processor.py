"""
Módulo de procesamiento de pagos - versión 1.2
Patrones utilizados: Singleton, Chain of Responsibility, Iterator
"""

from getJason import SiteData


class Payment:
    def __init__(self, order_number, token, amount):
        self.order_number = order_number
        self.token = token
        self.amount = amount

    def __str__(self):
        return f"Pedido #{self.order_number} | Token: {self.token} | Monto: ${self.amount}"


class PaymentIterator:
    def __init__(self, payments):
        self._payments = payments
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._payments):
            result = self._payments[self._index]
            self._index += 1
            return result
        raise StopIteration


class BankAccount:
    def __init__(self, token, initial_balance):
        self.token = token
        self.balance = initial_balance
        self.key = SiteData().get_key(token)

    def can_process(self, amount):
        return self.balance >= amount

    def process(self, amount):
        self.balance -= amount


class PaymentHandler:
    def __init__(self, account):
        self.account = account
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, order_number, amount):
        if self.account.can_process(amount):
            self.account.process(amount)
            return Payment(order_number, self.account.token, amount)
        if self.next_handler:
            return self.next_handler.handle(order_number, amount)
        raise Exception("Saldo insuficiente en todas las cuentas.")


class PaymentSystem:
    def __init__(self):
        self.token1 = BankAccount("token1", 1000)
        self.token2 = BankAccount("token2", 2000)

        self.handler1 = PaymentHandler(self.token1)
        self.handler2 = PaymentHandler(self.token2)

        self.handler1.set_next(self.handler2)
        self.handler2.set_next(self.handler1)

        self.current_handler = self.handler1
        self.payments = []

    def request_payment(self, order_number, amount):
        payment = self.current_handler.handle(order_number, amount)
        self.payments.append(payment)
        self.current_handler = (
            self.handler2 if self.current_handler == self.handler1 else self.handler1
        )
        return payment

    def list_payments(self):
        return PaymentIterator(self.payments)

