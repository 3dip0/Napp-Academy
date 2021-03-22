from mercado.classes.Cliente import Cliente


class TestCliente:
    def test_class_declared(self):
        objeto = Cliente('Édipo Ap. Moreira')
        assert isinstance(objeto, Cliente)

    def test_instanciar_objeto(self):
        objeto = Cliente('Édipo Moreira')
        assert objeto.nome, 'Édipo Moreira'

    def test_setter(self):
        objeto = Cliente('Édipo Moreira')
        assert objeto.nome == 'Édipo Moreira'
        objeto.nome = 'Édipo Ap Moreira'
        assert objeto.nome == 'Édipo Ap Moreira'

    def test_str_repr(self):
        cliente = Cliente('Édipo Moreira')
        assert str(cliente) == 'Édipo Moreira'
        assert repr(cliente) == 'Cliente => Édipo Moreira'
