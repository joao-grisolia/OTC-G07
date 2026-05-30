import os

listaPedidos = []
listaEntregadores = []

def limparTela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def cadastrarPedido():
    limparTela()
    idValido = 0
    idPedido = input('ID do pedido (ex:B2345): ')
    while idValido == 0:
        if not (len(idPedido) == 5 and idPedido[0].isalpha() and idPedido[1:].isdigit()):
            print('-> ID INVALIDO <- Digite um id valido (1 letra + 4 numeros)')
            idPedido = input('ID do pedido (ex:B2345): ')
        elif idPedido in [p['idPedido'] for p in listaPedidos]:
            print('-> ID JA CADASTRADO <- Digite outro id')
            idPedido = input('ID do pedido (ex:B2345): ')
        else:
            idValido = 1

    nomeCliente = str(input('Nome do cliente: '))
    endereco = str(input('Digite o endereco: '))
    print('''
          PRIORIDADE DO PEDIDO
          1 - Alta
          2 - Normal
          ''')
    entrada = input('->')
    while (not entrada.isdigit()) or (int(entrada) != 1 and int(entrada) != 2):
        print('-> PRIORIDADE INVALIDA <- Digite 1 ou 2')
        entrada = input('->')
    prioridade = int(entrada)
    if prioridade == 1:
        prioridade = 'Alta'
    else:
        prioridade = 'Normal'

    descricao = input('Descrição do pedido: ')

    listaPedidos.append({
        'idPedido': idPedido,
        'cliente': nomeCliente,
        'endereco': endereco,
        'prioridade': prioridade,
        'descricao': descricao,
        'status': 'Pendente',
        'idEntregador': None
    })
    print(listaPedidos)
    print('Pedido cadastrado com sucesso')
    input('Pressione ENTER para continuar')
    
def cadastrarEntregador():
    limparTela()
    idValido = 0
    idEntregador = input('ID do entregador (4 digitos): ')
    while idValido == 0:
        if not (len(idEntregador) == 4 and idEntregador.isdigit()):
            print('-> ID INVALIDO <- Digite um id valido (4 digitos)')
            idEntregador = input('ID do entregador (4 digitos): ')
        elif idEntregador in [e['idEntregador'] for e in listaEntregadores]:
            print('-> ID JA CADASTRADO <- Digite outro id')
            idEntregador = input('ID do entregador (4 digitos): ')
        else:
            idValido = 1

    nomeEntregador = str(input('Nome do entregador: '))

    veiculo = input('Veiculo (carro, van, moto): ').lower()
    while veiculo not in ('carro', 'van', 'moto'):
        print('-> VEICULO INVALIDO <- Escolha entre carro, van ou moto')
        veiculo = input('Veiculo (carro, van, moto): ').lower()

    idsPedidos = []
    id_pedido = input('ID do pedido associado (deixe em branco para nenhum): ')
    while id_pedido:
        if id_pedido not in [pedido['idPedido'] for pedido in listaPedidos]:
            print('ID do pedido nao encontrado.')
        elif id_pedido in idsPedidos:
            print('Pedido ja adicionado a este entregador.')
        else:
            idsPedidos.append(id_pedido)
            print(f'Pedido {id_pedido} adicionado.')
        id_pedido = input('Outro ID de pedido (deixe em branco para finalizar): ')

    listaEntregadores.append({
        'idEntregador': idEntregador,
        'nome': nomeEntregador,
        'veiculo': veiculo,
        'idsPedidos': idsPedidos,
        'disponibilidade': len(idsPedidos) == 0
    })
    for idp in idsPedidos:
        for pedido in listaPedidos:
            if pedido['idPedido'] == idp:
                pedido['idEntregador'] = idEntregador
    print('Entregador cadastrado com sucesso')
    input('Pressione ENTER para continuar')

def atualizarPedido():
    n = -1
    while n != 0:
        limparTela()
        print('''
        1. Alterar o status do pedido
        2. Cancelar Pedido
        3. Associar entregador a pedido
        4. Remover associação de entregador
        5. Voltar
        ''')
        entrada = input("-> ")
        while not entrada.isdigit():
            print('Opcao invalida, digite um numero')
            entrada = input("-> ")
        n = int(entrada)

        if n == 1:
            limparTela()
            idPedido = input('ID do pedido a ser atualizado: ')
            while idPedido not in [pedido['idPedido'] for pedido in listaPedidos]:
                limparTela()
                print('ID do pedido nao encontrado. Digite um ID valido.')
                idPedido = input('ID do pedido a ser atualizado: ')

            print('''
                1. Pendente
                2. Em Rota
                3. Entregue
                4. Cancelado
            ''')
            entradaStatus = input('Novo status do pedido: ')
            while not entradaStatus.isdigit():
                print('Opcao invalida, digite um numero')
                entradaStatus = input('Novo status do pedido: ')
            status = int(entradaStatus)
            statusMap = {1: 'Pendente', 2: 'Em Rota', 3: 'Entregue', 4: 'Cancelado'}
            if status in statusMap:
                for pedido in listaPedidos:
                    if pedido['idPedido'] == idPedido:
                        if pedido['status'] == 'Cancelado' and statusMap[status] != 'Cancelado':
                            print('Pedido cancelado nao pode ser reativado.')
                        else:
                            pedido['status'] = statusMap[status]
                            print(f'Status atualizado para {statusMap[status]}')
            else:
                print('Opcao invalida.')
            input('Pressione ENTER para continuar')

        elif n == 2:
            limparTela()
            idPedido = input('ID do pedido a ser cancelado: ')
            while idPedido not in [pedido['idPedido'] for pedido in listaPedidos]:
                print('ID do pedido nao encontrado. Digite um ID valido.')
                idPedido = input('ID do pedido a ser cancelado: ')

            for pedido in listaPedidos:
                if pedido['idPedido'] == idPedido:
                    print(f'Pedido encontrado: {pedido}')
                    confirmacao = input("Deseja mesmo cancelar esse pedido? (s/n) -> ")
                    while confirmacao.lower() not in ('s', 'n'):
                        print('Opcao invalida.')
                        confirmacao = input("Deseja mesmo cancelar esse pedido? (s/n) -> ")
                    if confirmacao.lower() == 's':
                        pedido['status'] = 'Cancelado'
                        print('Pedido cancelado com sucesso.')
                    else:
                        print('Cancelamento abortado.')
                    break
            input('Pressione ENTER para continuar')

        elif n == 3:
            limparTela()
            idPedido = input('ID do pedido: ')
            pedidoAlvo = None
            for pedido in listaPedidos:
                if pedido['idPedido'] == idPedido:
                    pedidoAlvo = pedido
                    break
            if not pedidoAlvo:
                print('Pedido nao encontrado.')
                input('Pressione ENTER para continuar')
                continue

            if pedidoAlvo['status'] == 'Cancelado':
                print('Pedido cancelado nao pode ser associado.')
                input('Pressione ENTER para continuar')
                continue
            idEntregador = input('ID do entregador: ')
            entregadorAlvo = None
            for entregador in listaEntregadores:
                if entregador['idEntregador'] == idEntregador:
                    entregadorAlvo = entregador
                    break
            if not entregadorAlvo:
                print('Entregador nao encontrado.')
            elif len(entregadorAlvo['idsPedidos']) >= 3:
                print('Entregador ja possui 3 pedidos (limite maximo).')
            elif idPedido in entregadorAlvo['idsPedidos']:
                print('Pedido ja associado a este entregador.')
            else:
                pedidoAlvo['idEntregador'] = idEntregador
                pedidoAlvo['status'] = 'Em Rota'
                entregadorAlvo['idsPedidos'].append(idPedido)
                entregadorAlvo['disponibilidade'] = False
                print(f'Pedido {idPedido} associado ao entregador {entregadorAlvo["nome"]}.')
            input('Pressione ENTER para continuar')

        elif n == 4:
            limparTela()
            idPedido = input('ID do pedido: ')
            pedidoAlvo = None
            for pedido in listaPedidos:
                if pedido['idPedido'] == idPedido:
                    pedidoAlvo = pedido
                    break
            if not pedidoAlvo:
                print('Pedido nao encontrado.')
            elif pedidoAlvo.get('idEntregador') is None:
                print('Nenhum entregador associado a este pedido.')
            else:
                idEntregador = pedidoAlvo['idEntregador']
                for entregador in listaEntregadores:
                    if entregador['idEntregador'] == idEntregador:
                        if idPedido in entregador['idsPedidos']:
                            entregador['idsPedidos'].remove(idPedido)
                        if len(entregador['idsPedidos']) == 0:
                            entregador['disponibilidade'] = True
                        break
                pedidoAlvo['idEntregador'] = None
                if pedidoAlvo['status'] == 'Em Rota':
                    pedidoAlvo['status'] = 'Pendente'
                print('Associacao removida com sucesso.')
            input('Pressione ENTER para continuar')

        elif n == 5:
            return
        
def consultarInformacoes():
    n = -1
    while n != 0:
        limparTela()
        print('''
        1. Pedidos pendentes
        2. Pedidos entregues
        3. Buscar pedido por ID
        4. Entregadores disponiveis
        5. Entregas de um entregador
        0. Voltar
        ''')
        entrada = input('-> ')
        while not entrada.isdigit():
            print('Opcao invalida, digite um numero')
            entrada = input('-> ')
        n = int(entrada)

        if n == 1:
            limparTela()
            print('--- PEDIDOS PENDENTES ---')
            encontrados = 0
            for pedido in listaPedidos:
                if pedido['status'] == 'Pendente':
                    print(pedido)
                    encontrados += 1
            if encontrados == 0:
                print('Nenhum pedido pendente encontrado.')
            input('Pressione ENTER para continuar')

        elif n == 2:
            limparTela()
            print('--- PEDIDOS ENTREGUES ---')
            encontrados = 0
            for pedido in listaPedidos:
                if pedido['status'] == 'Entregue':
                    print(pedido)
                    encontrados += 1
            if encontrados == 0:
                print('Nenhum pedido entregue encontrado.')
            input('Pressione ENTER para continuar')

        elif n == 3:
            limparTela()
            idPedido = input('ID do pedido a buscar: ')
            encontrado = 0
            for pedido in listaPedidos:
                if pedido['idPedido'] == idPedido:
                    print(f'Pedido encontrado: {pedido}')
                    encontrado += 1
                    break
            if not encontrado:
                print('Pedido nao encontrado.')
            input('Pressione ENTER para continuar')

        elif n == 4:
            limparTela()
            print('--- ENTREGADORES DISPONIVEIS ---')
            encontrados = 0
            for entregador in listaEntregadores:
                if entregador.get('disponibilidade'):
                    print(entregador)
                    encontrados += 1
            if encontrados == 0:
                print('Nenhum entregador disponivel.')
            input('Pressione ENTER para continuar')

        elif n == 5:
            limparTela()
            idEntregador = input('ID do entregador: ')
            encontrado = 0
            for entregador in listaEntregadores:
                if entregador['idEntregador'] == idEntregador:
                    encontrado += 1
                    break
            if not encontrado:
                print('Entregador nao encontrado.')
            else:
                print(f'--- ENTREGAS DO ENTREGADOR {idEntregador} ---')
                entregas = 0
                for pedido in listaPedidos:
                    if pedido.get('idEntregador') == idEntregador:
                        print(pedido)
                        entregas += 1
                if entregas == 0:
                    print('Nenhuma entrega associada a esse entregador.')
            input('Pressione ENTER para continuar')

        elif n == 0:
            return

        else:
            print('Opcao invalida.')
            input('Pressione ENTER para continuar')

def RelatoriosOperacionais():
    limparTela()
    print('--- RELATORIOS OPERACIONAIS ---')
    print('''
     1. Total de pedidos
     2. Pedidos por status
     3. Pedidos de alta prioridade
     4. Entregador com maior numero de entregas
     0. Voltar
    ''')
    entrada = input('-> ')
    while not entrada.isdigit():
        print('Opcao invalida, digite um numero')
        entrada = input('-> ')
    opc = int(entrada)

    if opc == 1:
        totalPedidos = len(listaPedidos)
        print(f'Total de pedidos: {totalPedidos}')

    elif opc == 2:
        pedidos_por_status = {'Pendente': 0, 'Em Rota': 0, 'Entregue': 0, 'Cancelado': 0}
        for pedido in listaPedidos:
            pedidos_por_status[pedido['status']] += 1
        print('--- PEDIDOS POR STATUS ---')
        for status, quantidade in pedidos_por_status.items():
            print(f'{status}: {quantidade}')

    elif opc == 3:
        pedidos_alta_prioridade = []
        for pedido in listaPedidos:
            if pedido['prioridade'] == 'Alta':
                pedidos_alta_prioridade.append(pedido)
        print('--- PEDIDOS DE ALTA PRIORIDADE ---')
        if not pedidos_alta_prioridade:
            print('Nenhum pedido de alta prioridade.')
        for pedido in pedidos_alta_prioridade:
            print(pedido)

    elif opc == 4:
        entregas_por_entregador = {}
        for pedido in listaPedidos:
            id_entregador = pedido['idEntregador']
            if id_entregador is not None:
                if id_entregador not in entregas_por_entregador:
                    entregas_por_entregador[id_entregador] = 0
                entregas_por_entregador[id_entregador] += 1

        entregador_maximo = None
        maximo_entregas = 0

        for id_entregador in entregas_por_entregador:
            quantidade = entregas_por_entregador[id_entregador]
            if quantidade > maximo_entregas:
                maximo_entregas = quantidade
                entregador_maximo = id_entregador
        if entregador_maximo is not None:
            print(f'Entregador com maior numero de entregas: {entregador_maximo} ({maximo_entregas} entregas)')
        else:
            print('Nenhum entregador com entregas registradas.')
    elif opc == 0:
        return
    else:
        print('Opcao invalida.')
    input('Pressione ENTER para continuar')

def menu():
    print('FLUXO NORTE')
    print('''
          1 - Cadastrar pedido
          2 - Cadastrar entregador
          3 - Atualizar pedido
          4 - Consultar informacoes
          5 - Relatorios operacionais
          0 - Sair

          Escolha uma opção
          ''')

def main():
    opcao = -1
    while opcao != 0:
        limparTela()
        menu()
        entrada = input('-> ')
        while not entrada.isdigit():
            print('Opcao invalida, digite um numero')
            entrada = input('-> ')
        opcao = int(entrada)

        if opcao == 1:
            cadastrarPedido()
        elif opcao == 2:
            cadastrarEntregador()
        elif opcao == 3:
            atualizarPedido()
        elif opcao == 4:
            consultarInformacoes()
        elif opcao == 5:
            RelatoriosOperacionais()
        elif opcao == 0:
            print('Encerrando...')
        else:
            input('Opção invalida, PRESSIONE ENTER')

main()