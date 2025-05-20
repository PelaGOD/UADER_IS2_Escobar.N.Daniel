from __future__ import annotations
from ast import Lambda
from collections.abc import Iterable, Iterator

class HistorialIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: Historial, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value
    
    def len(self):
        return len(self._collection)
    
    def ordenarMemorMayor(self):
        self._collection.sort(key=lambda c: c['fecha'])
    
class Historial(Iterable):
    def __init__(self) -> None:
        self._historial = []
    
    def add(self, historia):
        self._historial.append(historia)

    def mostrarHistorial(self, historialIterable):
        historialIterable.ordenarMemorMayor()
        while(historialIterable._position < historialIterable.len()):
            print(historialIterable.__next__())

    def __iter__(self) -> HistorialIterator:
        return HistorialIterator(self._historial)
    
    def getReverseIterator(self) -> HistorialIterator:
        return HistorialIterator(self._historial, True)
