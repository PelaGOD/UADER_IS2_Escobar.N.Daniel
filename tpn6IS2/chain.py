from abc import ABC, abstractmethod
from datetime import datetime
from SingletonGetJson import SingletonGetJson
from historial import Historial


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class AbstractHandler(Handler):
    s = SingletonGetJson()
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


class Token1Handler(AbstractHandler):
    saldo = 1000
    
    def handle(self, request):
        if (request["tk"] == self.s.getToken("token1")
            and request["monto"] <= self.saldo):

            self.saldo -= request["monto"]
            return {"nroPedido": request["nroPedido"],
                    "fecha": datetime.today().strftime('%Y-%m-%d %H:%M'),
                    "cuenta": "cuenta1",
                    "monto": request["monto"]}
        else:
            return super().handle(request)

class Token2Handler(AbstractHandler):
    saldo = 2000
    
    def handle(self, request):
        if (request["tk"] == self.s.getToken("token2")
            and request["monto"] <= self.saldo):

            self.saldo -= request["monto"]
            return {"nroPedido": request["nroPedido"],
                    "fecha": datetime.today().strftime('%Y-%m-%d %H:%M'),
                    "cuenta": "cuenta2",
                    "monto": request["monto"]}
        else:
            return super().handle(request)