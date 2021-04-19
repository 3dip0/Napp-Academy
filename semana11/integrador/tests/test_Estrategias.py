from integrador.classes.Estrategias import Estrategia
from integrador.classes.Estrategias import Estrategia_SQLite
from integrador.classes.Estrategias import Estrategia_CSV
import pytest


class TestEstrategias:
    def test_instanciar_classe_abstrata(self):
        msg_erro = "Can't instantiate abstract class Estrategia with abstract"
        msg_erro = msg_erro + " methods execute, nome, parametros_necessarios"
        with pytest.raises(Exception) as error:
            Estrategia()
        assert str(error.value) == msg_erro

class TestEstrategia_Texto_1:
    def test_instanciar_classe(self):
        objeto = Estrategia_Texto_1()
        assert isinstance(objeto, Estrategia)
        assert isinstance(objeto, Estrategia_Texto_1)

    def test_metodo_parametros_necessarios(self):
        objeto = Estrategia_Texto_1()
        dados_retornados = objeto.parametros_necessarios()
        assert type(dados_retornados) is tuple
        assert dados_retornados == ('algoritmo', 'arquivo')

    def test_metodo_executar(self):
        dados = {'algoritmo': 'txt',
                 'arquivo': 'integrador/dados/arquivo_texto1_modelo1.txt'}
        objeto = Estrategia_Texto_1()
        dados_retornados = objeto.execute(dados)
        assert type(dados_retornados) is list

class TestEstrategia_Texto_2:
    def test_instanciar_classe(self):
        objeto = Estrategia_Texto_2()
        assert isinstance(objeto, Estrategia)
        assert isinstance(objeto, Estrategia_Texto_2)

    def test_metodo_parametros_necessarios(self):
        objeto = Estrategia_Texto_2()
        dados_retornados = objeto.parametros_necessarios()
        assert type(dados_retornados) is tuple
        assert dados_retornados == ('algoritmo', 'arquivo')

    def test_metodo_executar(self):
        dados = {'algoritmo': 'txt',
                 'arquivo': 'integrador/dados/arquivo_texto1_modelo2.txt'}
        objeto = Estrategia_Texto_2()
        dados_retornados = objeto.execute(dados)
        assert type(dados_retornados) is list


