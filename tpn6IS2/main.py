from chain import Token1Handler, Token2Handler
from historial import Historial


def client_code(handler, requests):
    historial = Historial()
    
    for request in requests:
        result = handler.handle(request)
        if result is not None:
            historial.add(result)
        else:
            print("Error al realizar la transaccion")

    historial.mostrarHistorial(historial.__iter__())

if __name__ == "__main__":

    tk1 = Token1Handler()
    tk2 = Token2Handler()

    tk1.set_next(tk2)
    requests = [{"tk": "C598-ECF9-F0F7-881A", "nroPedido" : "0000A3", "monto": 500},
                {"tk": "C598-ECF9-F0F7-881B", "nroPedido" : "0000B1", "monto": 500},
                {"tk": "C598-ECF9-F0F7-881A", "nroPedido" : "0000A2", "monto": 500},
                {"tk": "C598-ECF9-F0F7-881B", "nroPedido" : "0000B2", "monto": 500},
                {"tk": "C598-ECF9-F0F7-881B", "nroPedido" : "0000B3", "monto": 500},
                {"tk": "C598-ECF9-F0F7-881A", "nroPedido" : "0000A1", "monto": 500}]
                
    client_code(tk1, requests)
