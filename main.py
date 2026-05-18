# =============================================================
#  FluxoNorte - Operação Turno Crítico
#  Disciplina: APPC (Prática) - PUC Campinas 2026
# =============================================================


# ── Estruturas principais ────────────────────────────────────
# Dicionário de pedidos: chave = ID do pedido
pedidos = {}

# Dicionário de entregadores: chave = ID do entregador
entregadores = {}


# ── Funções auxiliares ───────────────────────────────────────

def separador(titulo=""):
    print("\n" + "=" * 50)
    if titulo != "":
        print("  " + titulo)
        print("=" * 50)


def id_pedido_valido(id_pedido):
    # Deve ter 5 caracteres: 1 letra + 4 números (ex: A1234)
    if len(id_pedido) != 5:
        return False
    if id_pedido[0].isalpha() == False:
        return False
    if id_pedido[1:].isdigit() == False:
        return False
    return True


def id_entregador_valido(id_ent):
    # Deve ter exatamente 4 dígitos numéricos
    if len(id_ent) != 4:
        return False
    if id_ent.isdigit() == False:
        return False
    return True


def exibir_pedido(p):
    print("  -------------------------------------------")
    print("  Pedido     :", p["id"])
    print("  Cliente    :", p["cliente"])
    print("  Endereço   :", p["endereco"])
    print("  Prioridade :", p["prioridade"])
    print("  Status     :", p["status"])
    print("  Descrição  :", p["descricao"])
    if p["id_entregador"] != None:
        print("  Entregador :", p["id_entregador"])
    else:
        print("  Entregador : Não associado")
    print("  -------------------------------------------")


def ordenar_fila_entregador(id_ent):
    # Alta prioridade vai pra frente da fila, Normal fica depois
    fila = entregadores[id_ent]["pedidos"]
    alta   = []
    normal = []
    for pid in fila:
        if pedidos[pid]["prioridade"] == "Alta":
            alta.append(pid)
        else:
            normal.append(pid)
    entregadores[id_ent]["pedidos"] = alta + normal


# ── 1. Cadastro de Pedido ────────────────────────────────────

def cadastrar_pedido():
    separador("CADASTRO DE PEDIDO")

    id_pedido = input("  ID do Pedido (ex: A1234): ").strip().upper()
    if id_pedido_valido(id_pedido) == False:
        print("  [!] ID inválido. Use: 1 letra + 4 números (ex: A1234).")
        return
    if id_pedido in pedidos:
        print("  [!] Já existe um pedido com esse ID.")
        return

    nome = input("  Nome do Cliente: ").strip()
    if nome == "":
        print("  [!] Nome não pode ser vazio.")
        return

    endereco = input("  Endereço de Entrega: ").strip()
    if endereco == "":
        print("  [!] Endereço não pode ser vazio.")
        return

    prioridade = input("  Prioridade (Alta / Normal): ").strip().capitalize()
    if prioridade != "Alta" and prioridade != "Normal":
        print("  [!] Prioridade inválida. Use Alta ou Normal.")
        return

    descricao = input("  Descrição do Pedido: ").strip()
    if descricao == "":
        print("  [!] Descrição não pode ser vazia.")
        return

    pedidos[id_pedido] = {
        "id"           : id_pedido,
        "cliente"      : nome,
        "endereco"     : endereco,
        "prioridade"   : prioridade,
        "descricao"    : descricao,
        "status"       : "Pendente",
        "id_entregador": None
    }

    print("  Pedido", id_pedido, "cadastrado com sucesso!")


# ── 2. Cadastro de Entregador ────────────────────────────────

def cadastrar_entregador():
    separador("CADASTRO DE ENTREGADOR")

    id_ent = input("  ID do Entregador (4 dígitos): ").strip()
    if id_entregador_valido(id_ent) == False:
        print("  [!] ID inválido. Use exatamente 4 dígitos (ex: 0012).")
        return
    if id_ent in entregadores:
        print("  [!] Já existe um entregador com esse ID.")
        return

    nome = input("  Nome do Entregador: ").strip()
    if nome == "":
        print("  [!] Nome não pode ser vazio.")
        return

    veiculo = input("  Veículo (carro / van / moto): ").strip().lower()
    if veiculo != "carro" and veiculo != "van" and veiculo != "moto":
        print("  [!] Veículo inválido. Use: carro, van ou moto.")
        return

    entregadores[id_ent] = {
        "id"             : id_ent,
        "nome"           : nome,
        "veiculo"        : veiculo.capitalize(),
        "pedidos"        : [],
        "disponibilidade": True
    }

    print("  Entregador", id_ent, "-", nome, "cadastrado com sucesso!")


# ── 3. Atualização de Pedido ─────────────────────────────────

def atualizar_pedido():
    separador("ATUALIZAÇÃO DE PEDIDO")

    id_pedido = input("  ID do Pedido: ").strip().upper()
    if id_pedido not in pedidos:
        print("  [!] Pedido não encontrado.")
        return

    pedido = pedidos[id_pedido]

    if pedido["status"] == "Cancelado":
        print("  [!] Este pedido foi cancelado e não pode ser alterado.")
        return

    print("\n  Pedido:", id_pedido, "| Status:", pedido["status"], "| Prioridade:", pedido["prioridade"])
    print("\n  O que deseja fazer?")
    print("  1 - Alterar Status")
    print("  2 - Cancelar Pedido")
    print("  3 - Associar Entregador")
    print("  4 - Remover Entregador")
    print("  0 - Voltar")

    opcao = input("  Opção: ").strip()

    if opcao == "1":
        novo_status = input("  Novo status (Pendente / Em Rota / Entregue): ").strip().capitalize()
        if novo_status == "Em rota":
            novo_status = "Em Rota"
        if novo_status != "Pendente" and novo_status != "Em Rota" and novo_status != "Entregue":
            print("  [!] Status inválido.")
            return
        pedido["status"] = novo_status
        print("  Status atualizado para:", novo_status)

        if novo_status == "Entregue" and pedido["id_entregador"] != None:
            id_ent = pedido["id_entregador"]
            if id_pedido in entregadores[id_ent]["pedidos"]:
                entregadores[id_ent]["pedidos"].remove(id_pedido)
            entregadores[id_ent]["disponibilidade"] = len(entregadores[id_ent]["pedidos"]) < 3
            pedido["id_entregador"] = None

    elif opcao == "2":
        confirmacao = input("  Confirmar cancelamento? (s/n): ").strip().lower()
        if confirmacao == "s":
            if pedido["id_entregador"] != None:
                id_ent = pedido["id_entregador"]
                if id_pedido in entregadores[id_ent]["pedidos"]:
                    entregadores[id_ent]["pedidos"].remove(id_pedido)
                entregadores[id_ent]["disponibilidade"] = len(entregadores[id_ent]["pedidos"]) < 3
                pedido["id_entregador"] = None
            pedido["status"] = "Cancelado"
            print("  Pedido cancelado. Esta ação não pode ser desfeita.")

    elif opcao == "3":
        id_ent = input("  ID do Entregador: ").strip()
        if id_ent not in entregadores:
            print("  [!] Entregador não encontrado.")
            return
        ent = entregadores[id_ent]
        if ent["disponibilidade"] == False:
            print("  [!] Entregador indisponível. Limite de 3 pedidos atingido.")
            return
        if pedido["id_entregador"] != None and pedido["id_entregador"] != id_ent:
            id_ant = pedido["id_entregador"]
            if id_pedido in entregadores[id_ant]["pedidos"]:
                entregadores[id_ant]["pedidos"].remove(id_pedido)
            entregadores[id_ant]["disponibilidade"] = True
        if id_pedido not in ent["pedidos"]:
            ent["pedidos"].append(id_pedido)
        pedido["id_entregador"] = id_ent
        pedido["status"] = "Em Rota"
        ordenar_fila_entregador(id_ent)
        ent["disponibilidade"] = len(ent["pedidos"]) < 3
        print("  Pedido", id_pedido, "associado ao entregador", ent["nome"])

    elif opcao == "4":
        if pedido["id_entregador"] == None:
            print("  [!] Nenhum entregador associado a este pedido.")
            return
        id_ent = pedido["id_entregador"]
        if id_pedido in entregadores[id_ent]["pedidos"]:
            entregadores[id_ent]["pedidos"].remove(id_pedido)
        entregadores[id_ent]["disponibilidade"] = len(entregadores[id_ent]["pedidos"]) < 3
        pedido["id_entregador"] = None
        print("  Associação removida com sucesso.")

    elif opcao == "0":
        return

    else:
        print("  [!] Opção inválida.")


# ── 4. Consultas ─────────────────────────────────────────────

def consultar():
    separador("CONSULTAS")
    print("  1 - Pedidos Pendentes")
    print("  2 - Pedidos Entregues")
    print("  3 - Buscar Pedido por ID")
    print("  4 - Entregadores Disponíveis")
    print("  5 - Entregas de um Entregador")
    print("  0 - Voltar")

    opcao = input("  Opção: ").strip()

    if opcao == "1":
        separador("PEDIDOS PENDENTES")
        encontrou = False
        for p in pedidos.values():
            if p["status"] == "Pendente" and p["prioridade"] == "Alta":
                exibir_pedido(p)
                encontrou = True
        for p in pedidos.values():
            if p["status"] == "Pendente" and p["prioridade"] == "Normal":
                exibir_pedido(p)
                encontrou = True
        if encontrou == False:
            print("  Nenhum pedido pendente.")

    elif opcao == "2":
        separador("PEDIDOS ENTREGUES")
        encontrou = False
        for p in pedidos.values():
            if p["status"] == "Entregue":
                exibir_pedido(p)
                encontrou = True
        if encontrou == False:
            print("  Nenhum pedido entregue ainda.")

    elif opcao == "3":
        id_pedido = input("  ID do Pedido: ").strip().upper()
        if id_pedido in pedidos:
            exibir_pedido(pedidos[id_pedido])
        else:
            print("  [!] Pedido não encontrado.")

    elif opcao == "4":
        separador("ENTREGADORES DISPONÍVEIS")
        encontrou = False
        for e in entregadores.values():
            if e["disponibilidade"] == True:
                print("  ID:", e["id"], "| Nome:", e["nome"], "| Veículo:", e["veiculo"], "| Pedidos:", len(e["pedidos"]), "/ 3")
                encontrou = True
        if encontrou == False:
            print("  Nenhum entregador disponível no momento.")

    elif opcao == "5":
        id_ent = input("  ID do Entregador: ").strip()
        if id_ent not in entregadores:
            print("  [!] Entregador não encontrado.")
            return
        ent = entregadores[id_ent]
        separador("ENTREGAS DE " + ent["nome"].upper())
        encontrou = False
        for p in pedidos.values():
            if p["id_entregador"] == id_ent:
                exibir_pedido(p)
                encontrou = True
        if encontrou == False:
            print("  Nenhuma entrega ativa para este entregador.")

    elif opcao == "0":
        return

    else:
        print("  [!] Opção inválida.")


# ── 5. Relatório Operacional ─────────────────────────────────

def gerar_relatorio():
    separador("RELATÓRIO OPERACIONAL")

    total = len(pedidos)
    print("\n  Total de pedidos cadastrados:", total)

    if total == 0:
        print("  Nenhum dado para exibir.")
        return

    pendentes  = 0
    em_rota    = 0
    entregues  = 0
    cancelados = 0

    for p in pedidos.values():
        if p["status"] == "Pendente":
            pendentes += 1
        elif p["status"] == "Em Rota":
            em_rota += 1
        elif p["status"] == "Entregue":
            entregues += 1
        elif p["status"] == "Cancelado":
            cancelados += 1

    print("\n  Pedidos por status:")
    print("    Pendente  :", pendentes)
    print("    Em Rota   :", em_rota)
    print("    Entregue  :", entregues)
    print("    Cancelado :", cancelados)

    print("\n  Pedidos com Alta Prioridade (não cancelados):")
    tem_alta = False
    for p in pedidos.values():
        if p["prioridade"] == "Alta" and p["status"] != "Cancelado":
            print("    -", p["id"], "|", p["cliente"], "|", p["status"])
            tem_alta = True
    if tem_alta == False:
        print("    Nenhum.")

    print("\n  Entregadores e quantidade de pedidos:")
    if len(entregadores) == 0:
        print("    Nenhum entregador cadastrado.")
        return

    maior_nome = ""
    maior_qtd  = -1

    for e in entregadores.values():
        qtd = len(e["pedidos"])
        print("    -", e["id"], e["nome"], ":", qtd, "pedido(s)")
        if qtd > maior_qtd:
            maior_qtd  = qtd
            maior_nome = e["nome"]

    if maior_qtd > 0:
        print("\n  Entregador com mais pedidos:", maior_nome, "(", maior_qtd, "pedido(s) )")
    else:
        print("\n  Nenhum entregador com pedidos associados no momento.")


# ── Menu Principal ───────────────────────────────────────────

def menu():
    separador("FLUXONORTE - OPERAÇÃO TURNO CRÍTICO")
    print("  1 - Cadastrar Pedido")
    print("  2 - Cadastrar Entregador")
    print("  3 - Atualizar Pedido")
    print("  4 - Consultas")
    print("  5 - Relatório Operacional")
    print("  0 - Encerrar Sistema")
    print("=" * 50)
    opcao = input("  Escolha uma opção: ").strip()
    return opcao


# ── Execução principal ───────────────────────────────────────

opcao_escolhida = menu()

rodando = opcao_escolhida != "0"

while rodando:
    if opcao_escolhida == "1":
        cadastrar_pedido()
    elif opcao_escolhida == "2":
        cadastrar_entregador()
    elif opcao_escolhida == "3":
        atualizar_pedido()
    elif opcao_escolhida == "4":
        consultar()
    elif opcao_escolhida == "5":
        gerar_relatorio()
    else:
        print("  [!] Opção inválida.")

    opcao_escolhida = menu()
    rodando = opcao_escolhida != "0"

print("\n  Sistema encerrado. Até logo!\n")