from contato import Contato


class ContatoEmergencia(Contato):

    __slots__ = ("_prioridade",)

    def __init__(self, nome, telefone, datanasc, email, prioridade):
        super().__init__(nome, telefone, datanasc, email)
        self.prioridade = prioridade

    @property
    def prioridade(self):
        return self._prioridade

    @prioridade.setter
    def prioridade(self, valor):
        self._prioridade = valor

    def __str__(self):
        return (
            super().__str__()
            + f"\nPrioridade: {self._prioridade}"
        )