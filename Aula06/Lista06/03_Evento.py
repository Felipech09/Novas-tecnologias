from datetime import date


class Evento:

    __slots__ = (
        "_descricao",
        "_data_inicio",
        "_data_fim",
        "_contato"
    )

    __total_eventos = 0

    def __init__(self, descricao, data_inicio, data_fim, contato):

        self.descricao = descricao
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.contato = contato

        Evento.__total_eventos += 1

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, valor):
        self._descricao = valor

    @property
    def data_inicio(self):
        return self._data_inicio

    @data_inicio.setter
    def data_inicio(self, valor):
        if isinstance(valor, date):
            self._data_inicio = valor
        else:
            raise TypeError("Data inválida")

    @property
    def data_fim(self):
        return self._data_fim

    @data_fim.setter
    def data_fim(self, valor):
        if isinstance(valor, date):
            self._data_fim = valor
        else:
            raise TypeError("Data inválida")

    @property
    def contato(self):
        return self._contato

    @contato.setter
    def contato(self, valor):
        self._contato = valor

    def get_informacoes(self):

        return (
            f"Descrição: {self._descricao}\n"
            f"Data início: {self._data_inicio.strftime('%d/%m/%Y')}\n"
            f"Data fim: {self._data_fim.strftime('%d/%m/%Y')}\n"
            f"Contato: {self._contato.nome}"
        )

    @staticmethod
    def get_total_eventos():
        return Evento.__total_eventos