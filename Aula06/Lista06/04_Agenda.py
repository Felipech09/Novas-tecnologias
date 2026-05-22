class Agenda:

    __contatos = []
    __eventos = []

    def __init__(self, dado=None):

        if dado is not None:

            nome_classe = type(dado).__name__

            if nome_classe in ["Contato", "ContatoEmergencia"]:
                Agenda.__contatos.append(dado)

            elif nome_classe == "Evento":
                Agenda.__eventos.append(dado)

    @staticmethod
    def adicionar_contato(contato):
        Agenda.__contatos.append(contato)

    @staticmethod
    def adicionar_evento(evento):
        Agenda.__eventos.append(evento)

    @staticmethod
    def contatos():
        return Agenda.__contatos

    @staticmethod
    def eventos():
        return Agenda.__eventos