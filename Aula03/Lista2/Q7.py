estado = "fechado"

while True:
    cmd = input("Digite comando (A/T/E/F/S): ").upper()

    match cmd:
        case "A":
            if estado == "fechado":
                estado = "aberto"
                print("Atendimento aberto.")
            else:
                print("Erro: já está aberto.")
        case "T":
            if estado == "aberto":
                estado = "triado"
                print("Triagem realizada.")
            else:
                print("Erro: só pode triagem se aberto.")
        case "E":
            if estado == "triado":
                estado = "encaminhado"
                print("Encaminhado.")
            else:
                print("Erro: só pode encaminhar se triado.")
        case "F":
            if estado == "encaminhado":
                estado = "finalizado"
                print("Atendimento finalizado.")
            else:
                print("Erro: só pode finalizar se encaminhado.")
        case "S":
            print("Saindo...")
            break
        case _:
            print("Comando inválido.")
