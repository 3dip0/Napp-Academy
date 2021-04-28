# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from produtos.classes.Caracteristicas import Caracteristicas


class Produto(ABC):
    def __init__(self, implementation):
        try:
            if issubclass(type(implementation), Caracteristicas):
                self.implementation = implementation
        except Exception as e:
            print(e)

    @abstractmethod
    def operation(self):
        pass



class CocaCola(Produto):
    def operation(self):
        return "CocaCola tamanho:" + self.implementation.operation_implementation()


class Pepsi(Produto):
    def operation(self):
        return "Pepsi tamanho:" + self.implementation.operation_implementation()


class Dolly(Produto):
    def operation(self):
        return "Dolly tamanho:" + self.implementation.operation_implementation()


class GuaranaAntartica(Produto):
    def operation(self):
        return "GuaranaAntartica tamanho:" + self.implementation.operation_implementation()
