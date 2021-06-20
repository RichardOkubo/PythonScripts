class Descritor:
    """Implementa um descritor para a classe ItemPedido."""

    __contador = 0

    def __init__(self):
        prefixo = self.__class__.__name__
        chave = self.__class__.__contador
        self.descritor = f"_{prefixo}_{chave}"
        self.__class__.__contador += 1

    def __get__(self, instancia, proprio):
        return getattr(instancia, self.descritor)

    def __set__(self, instancia, valor):
        if valor > 0:
            setattr(instancia, self.descritor, valor)
        else:
            raise ValueError("O valor deve ser > 0")


class ItemPedido:

    peso = Descritor()
    preco = Descritor()

    def __init__(self, descricao, peso, preco):
        self.descricao = descricao
        self.peso = peso
        self.preco = preco

    def valor_total(self):
        return self.peso * self.preco
