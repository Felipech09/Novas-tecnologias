from datetime import date

class Contato:
    __slots__ = ("_nome", "_telefone", "_datanasc", "_email")

    def __init__(self, nome, telefone, datanasc, email):
        self.nome = nome
        self.telefone = telefone
        self.datanasc = datanasc
        self.email = email

    # nome
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    # telefone
    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, valor):
        self._telefone = valor

    # data de nascimento
    @property
    def datanasc(self):
        return self._datanasc

    @datanasc.setter
    def datanasc(self, valor):
        self._datanasc = valor

    # email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        self._email = valor

    # método __str__
    def __str__(self):
        return "{0}\n{1}\n{2}\n{3}".format(
            self._nome,
            self._telefone,
            self._datanasc.strftime("%d/%m/%Y"),
            self._email
        )