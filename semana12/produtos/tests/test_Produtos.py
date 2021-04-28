# -*- coding: utf-8 -*-
from produtos.classes.Produtos import Produto
from produtos.classes.Produtos import CocaCola
from produtos.classes.Produtos import Pepsi
from produtos.classes.Produtos import Dolly
from produtos.classes.Produtos import GuaranaAntartica
from produtos.classes.Caracteristicas import Tamanho600ml
from produtos.classes.Caracteristicas import Tamanho1litro
from produtos.classes.Caracteristicas import Tamanho2litros
from produtos.classes.Caracteristicas import Tamanho3litros
import pytest


class TestColaborador:
	def test_class_Pepsi(self):
		msg = 'Pepsi tamanho: 600ml.'
		objeto = Pepsi(Tamanho600ml())
		assert isinstance(objeto, Produto)
		assert isinstance(objeto, Pepsi)
		assert objeto.operation() == msg

	def test_class_CocaCola(self):
		msg = 'CocaCola tamanho: 600ml.'
		objeto = CocaCola(Tamanho600ml())
		assert isinstance(objeto, Produto)
		assert isinstance(objeto, CocaCola)
		assert objeto.operation() == msg

	def test_class_Dolly(self):
		msg = 'Dolly tamanho: 600ml.'
		objeto = Dolly(Tamanho600ml())
		assert isinstance(objeto, Produto)
		assert isinstance(objeto, Dolly)
		assert objeto.operation() == msg

	def test_class_CocaCola(self):
		msg = 'GuaranaAntartica tamanho: 600ml.'
		objeto = GuaranaAntartica(Tamanho600ml())
		assert isinstance(objeto, Produto)
		assert isinstance(objeto, GuaranaAntartica)
		assert objeto.operation() == msg

	def test_class_Pepsi_1litro(self):
		msg = 'Pepsi tamanho: 1 litro.'
		objeto = Pepsi(Tamanho1litro())
		assert isinstance(objeto, Produto)
		assert isinstance(objeto, Pepsi)
		assert objeto.operation() == msg

	def test_class_CocaCola_1litro(self):
		msg = 'CocaCola tamanho: 1 litro.'
		objeto = CocaCola(Tamanho1litro())
		assert isinstance(objeto, Produto)
		assert isinstance(objeto, CocaCola)
		assert objeto.operation() == msg

	def test_class_Dolly_1litro(self):
		msg = 'Dolly tamanho: 1 litro.'
		objeto = Dolly(Tamanho1litro())
		assert isinstance(objeto, Produto)
		assert isinstance(objeto, Dolly)
		assert objeto.operation() == msg

	def test_class_GuaranaAntartica_1litro(self):
		msg = 'GuaranaAntartica tamanho: 1 litro.'
		objeto = GuaranaAntartica(Tamanho1litro())
		assert isinstance(objeto, Produto)
		assert isinstance(objeto, GuaranaAntartica)
		assert objeto.operation() == msg

	def test_class_Pepsi_2litro(self):
		msg = 'Pepsi tamanho: 2 litros.'
		objeto = Pepsi(Tamanho2litros())
		assert isinstance(objeto, Produto)
		assert isinstance(objeto, Pepsi)
		assert objeto.operation() == msg
		
	def test_class_CocaCola_2litro(self):
		msg = 'CocaCola tamanho: 2 litros.'
		objeto = CocaCola(Tamanho2litros())
		assert isinstance(objeto, Produto)
		assert isinstance(objeto, CocaCola)
		assert objeto.operation() == msg

	def test_class_Dolly_2litro(self):
		msg = 'Dolly tamanho: 2 litros.'
		objeto = Dolly(Tamanho2litros())
		assert isinstance(objeto, Produto)
		assert isinstance(objeto, Dolly)
		assert objeto.operation() == msg

	def test_class_GuaranaAntartica_2litro(self):
		msg = 'GuaranaAntartica tamanho: 2 litros.'
		objeto = GuaranaAntartica(Tamanho2litros())
		assert isinstance(objeto, Produto)
		assert isinstance(objeto, GuaranaAntartica)
		assert objeto.operation() == msg

	def test_class_Pepsi_3litro(self):
		msg = 'Pepsi tamanho: 3 litros.'
		objeto = Pepsi(Tamanho3litros())
		assert isinstance(objeto, Produto)
		assert isinstance(objeto, Pepsi)
		assert objeto.operation() == msg
		
	def test_class_CocaCola_3litro(self):
		msg = 'CocaCola tamanho: 3 litros.'
		objeto = CocaCola(Tamanho3litros())
		assert isinstance(objeto, Produto)
		assert isinstance(objeto, CocaCola)
		assert objeto.operation() == msg

	def test_class_Dolly_3litro(self):
		msg = 'Dolly tamanho: 3 litros.'
		objeto = Dolly(Tamanho3litros())
		assert isinstance(objeto, Produto)
		assert isinstance(objeto, Dolly)
		assert objeto.operation() == msg

	def test_class_GuaranaAntartica_3litro(self):
		msg = 'GuaranaAntartica tamanho: 3 litros.'
		objeto = GuaranaAntartica(Tamanho3litros())
		assert isinstance(objeto, Produto)
		assert isinstance(objeto, GuaranaAntartica)
		assert objeto.operation() == msg

	def test_class_abstractClass(self):
		msg_erro = "Can't instantiate abstract class Produto "
		msg_erro = msg_erro + "with abstract methods operation"
		with pytest.raises(TypeError) as error:
			Produto()
		assert str(error.value) == msg_erro
