from datetime import datetime

from contato import Contato
from contato_emergencia import ContatoEmergencia
from evento import Evento
from agenda import Agenda


def ler_data(texto):

    while True:

        try:
            data_str = input(texto)
            return datetime.strptime(data_str, "%d/%m/%Y").date()

        except ValueError:
            print("Data inválida! Use dd/mm/aaaa.")


while True:

    print("\n===== MENU =====")
    print("1 - Criar contato")
    print("2 - Editar contato")
    print("3 - Listar contatos")
    print("4 - Criar contato emergência")
    print("5 - Criar evento")
    print("6 - Listar eventos")
    print("7 - Sair")

    try:
        opcao = int(input("Escolha: "))

    except ValueError:
        print("Digite um número válido.")
        continue

    match opcao:

        case 1:

            nome = input("Nome: ")
            telefone = input("Telefone: ")
            data = ler_data("Data nascimento: ")
            email = input("E-mail: ")

            c = Contato(nome, telefone, data, email)

            Agenda.adicionar_contato(c)

            print("Contato criado!")

        case 2:

            contatos = Agenda.contatos()

            if not contatos:
                print("Nenhum contato cadastrado.")
                continue

            for i, contato in enumerate(contatos):
                print(f"{i} - {contato.nome}")

            try:

                indice = int(input("Escolha o contato: "))

                contato = contatos[indice]

                contato.nome = input("Novo nome: ")
                contato.telefone = input("Novo telefone: ")
                contato.email = input("Novo email: ")

                print("Contato atualizado!")

            except:
                print("Índice inválido.")

        case 3:

            contatos = Agenda.contatos()

            if not contatos:
                print("Nenhum contato.")

            else:

                for contato in contatos:
                    print()
                    print(contato)

        case 4:

            nome = input("Nome: ")
            telefone = input("Telefone: ")
            data = ler_data("Data nascimento: ")
            email = input("E-mail: ")
            prioridade = input("Prioridade: ")

            c = ContatoEmergencia(
                nome,
                telefone,
                data,
                email,
                prioridade
            )

            Agenda.adicionar_contato(c)

            print("Contato emergência criado!")

        case 5:

            contatos = Agenda.contatos()

            if not contatos:
                print("Cadastre um contato primeiro.")
                continue

            descricao = input("Descrição do evento: ")

            data_inicio = ler_data("Data início: ")
            data_fim = ler_data("Data fim: ")

            print("\nContatos disponíveis:")

            for i, contato in enumerate(contatos):
                print(f"{i} - {contato.nome}")

            try:

                indice = int(input("Escolha o contato: "))

                contato = contatos[indice]

                evento = Evento(
                    descricao,
                    data_inicio,
                    data_fim,
                    contato
                )

                Agenda.adicionar_evento(evento)

                print("Evento criado!")

            except:
                print("Contato inválido.")

        case 6:

            eventos = Agenda.eventos()

            if not eventos:
                print("Nenhum evento.")

            else:

                for evento in eventos:
                    print()
                    print(evento.get_informacoes())

        case 7:

            print(
                f"Total de eventos: "
                f"{Evento.get_total_eventos()}"
            )

            print("Encerrando...")
            break

        case _:
            print("Opção inválida.")