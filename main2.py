import os

lista_pedidos = []
lista_entregadores = []
lista_prioridades = ['Alta', 'Normal']
lista_status_pedido = ['Pendente', 'Em Rota', 'Entregue', 'Cancelado']

def cadastrar_pedido():
    os.system('cls');
    id_pedido = input('ID do pedidto (ex:B2345): ');
    while not (len(id_pedido) == 5 and id_pedido[0].isalpha() and id_pedido[1:].isdigit()):
        # ele so entra no while se as condicoes nao forem  True
        # por isso do not
        # as condicoes são o tamanho do id_pedido tem que ser 5 (len(id_pedido) == 5)
        # o primeiro indice tem que ser uma letra id_pedido[0].isalpha()
        # o outros tem que que ser numero id_pedido[1:].isdigit()
        # enquanto nao (while not) cumprir com nenhum desse requisitos entra aqui no while
        print('-> ID INVALIDO <- Digite um id valido')
        id_pedido = input('ID do pedidto (ex:B2345): ');
    # aqui tem que fazer uma validacao pra ver se ja tem um
    # pedido com o id_pedido ja cadastrado, id_pedido duplicado
        
    nome_cliente = str(input('Nome do cliente: '));
    endereco = str(input('Digite o endereco: '));
    prioridade = str(input('Prioridade (Alta/Normal): '));
    while prioridade.capitalize() not in lista_prioridades:
        print('Prioridade invalida, digite Alta/Normal/Baixa');
        prioridade = str(input('Prioridade (Alta/Normal/Baixa): '));
    descricao = input('Descrição do pedido: ')
    
    lista_pedidos.append({
        'id_pedido': id_pedido,
        'cliente': nome_cliente,
        'endereco': endereco,
        'prioridade': prioridade,
        'status': 'Pendente',
        'id_entregador': None
    })
    print(lista_pedidos)
    print('Pedido cadastrado com sucesso')
    input('Pressione ENTER para continuar')
    
def cadastrar_entregador():
    os.system('cls');
    id_entregador = input('ID do entregador (ex:E1234): ');
    while not (len(id_entregador) == 5 and id_entregador[0].isalpha() and id_entregador[1:].isdigit()):
        print('-> ID INVALIDO <- Digite um id valido')
        id_entregador = input('ID do entregador (ex:E1234): ');
    
    nome_entregador = str(input('Nome do entregador: '));
    veiculo = str(input('Veiculo do entregador: '));
    id_pedido = input('ID do pedido associado: ')
    if id_pedido:
        while id_pedido not in [pedido['id_pedido'] for pedido in lista_pedidos]:
            print('ID do pedido nao encontrado. Digite um ID valido ou deixe em branco.')
            id_pedido = input('ID do pedido associado (deixe em branco se nao tiver): ')
    #falta colocar disponibilidade do pedido!
    print(lista_entregadores)
    print('Entregador cadastrado com sucesso')
    input('Pressione ENTER para continuar')
 
def buscar_pedido_por_id(id_pedido):
    """Busca um pedido na lista pelo ID."""
    for pedido in lista_pedidos:
        if pedido['id_pedido'] == id_pedido:
            return pedido
    return None

def buscar_entregador_por_id(id_entregador):
    """Busca um entregador na lista pelo ID."""
    for entregador in lista_entregadores:
        if entregador['id_entregador'] == id_entregador:
            return entregador
    return None

def separador(titulo):
    """Exibe um separador com título."""
    print("\n" + "=" * 50)
    print(f"  {titulo}")
    print("=" * 50 + "\n")

def ordenar_fila_entregador(id_entregador):
    """Ordena a fila de pedidos do entregador por prioridade."""
    pass

def atualizar_pedido():
    separador("ATUALIZAÇÃO DE PEDIDO")

    id_pedido = input("  ID do Pedido: ").strip().upper()
    pedido = buscar_pedido_por_id(id_pedido)
    if pedido is None:
        print("  [!] Pedido não encontrado.")
        return

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
            ent = buscar_entregador_por_id(id_ent)
            if ent and id_pedido in ent["pedidos"]:
                ent["pedidos"].remove(id_pedido)
            if ent:
                ent["disponibilidade"] = len(ent["pedidos"]) < 3
            pedido["id_entregador"] = None

    elif opcao == "2":
        confirmacao = input("  Confirmar cancelamento? (s/n): ").strip().lower()
        if confirmacao == "s":
            if pedido["id_entregador"] != None:
                id_ent = pedido["id_entregador"]
                ent = buscar_entregador_por_id(id_ent)
                if ent and id_pedido in ent["pedidos"]:
                    ent["pedidos"].remove(id_pedido)
                if ent:
                    ent["disponibilidade"] = len(ent["pedidos"]) < 3
                pedido["id_entregador"] = None
            pedido["status"] = "Cancelado"
            print("  Pedido cancelado. Esta ação não pode ser desfeita.")

    elif opcao == "3":
        id_ent = input("  ID do Entregador: ").strip()
        ent = buscar_entregador_por_id(id_ent)
        if ent is None:
            print("  [!] Entregador não encontrado.")
            return
        if ent["disponibilidade"] == False:
            print("  [!] Entregador indisponível. Limite de 3 pedidos atingido.")
            return
        if pedido["id_entregador"] != None and pedido["id_entregador"] != id_ent:
            id_ant = pedido["id_entregador"]
            ent_ant = buscar_entregador_por_id(id_ant)
            if ent_ant and id_pedido in ent_ant["pedidos"]:
                ent_ant["pedidos"].remove(id_pedido)
            if ent_ant:
                ent_ant["disponibilidade"] = True
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
        ent = buscar_entregador_por_id(id_ent)
        if ent and id_pedido in ent["pedidos"]:
            ent["pedidos"].remove(id_pedido)
        if ent:
            ent["disponibilidade"] = len(ent["pedidos"]) < 3
        pedido["id_entregador"] = None
        print("  Associação removida com sucesso.")

    elif opcao == "0":
        return

    else:
        print("  [!] Opção inválida.")
    
def menu():
    print('FLUXO NORTE')
    print('''
          1 - Cadastrar pedido
          2 - Cadastrar entregador
          3 - Atualizar pedido
          4 - Associar entregador a pedido
          5 - Remover associacao de entregador
          6 - Pedidos pendentes
          7 - Pedidos entregues
          8 - Buscar pedido por ID
          9 - Entregadores disponíveis
          10 - Entregas de um entregador
          11 - Relatorios operacionais
          0 - Sair
          
          Escolha uma opção
          ''')

def main():
    opcao = -1
    while opcao != 0:
        os.system('cls')
        menu()
        opcao = int(input('-> '))

        if opcao == 1:
            cadastrar_pedido();
        elif opcao == 2:
            cadastrar_entregador();
main()