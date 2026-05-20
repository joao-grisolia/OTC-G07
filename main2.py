import os

listaPedidos = []
listaEntregadores = []
listaPrioridades = ['Alta', 'Normal']
listaStatusPedido = ['Pendente', 'Em Rota', 'Entregue', 'Cancelado']

def cadastrarPedido():
    os.system('cls');
    idPedido = input('ID do pedidto (ex:B2345): ');
    while not (len(idPedido) == 5 and idPedido[0].isalpha() and idPedido[1:].isdigit()):
        print('-> ID INVALIDO <- Digite um id valido')
        idPedido = input('ID do pedidto (ex:B2345): ');

    nomeCliente = str(input('Nome do cliente: '));
    endereco = str(input('Digite o endereco: '));
    prioridade = str(input('Prioridade (Alta/Normal): '));
    while prioridade.capitalize() not in listaPrioridades:
        print('Prioridade invalida, digite Alta/Normal/Baixa');
        prioridade = str(input('Prioridade (Alta/Normal/Baixa): '));
    descricao = input('Descrição do pedido: ')
    
    listaPedidos.append({
        'idPedido': idPedido,
        'cliente': nomeCliente,
        'endereco': endereco,
        'prioridade': prioridade,
        'status': 'Pendente',
        'idEntregador': None
    })
    print(listaPedidos)
    print('Pedido cadastrado com sucesso')
    input('Pressione ENTER para continuar')
    
def cadastrarEntregador():
    os.system('cls');
    idEntregador = input('ID do entregador (ex:E1234): ');
    while not (len(idEntregador) == 5 and idEntregador[0].isalpha() and idEntregador[1:].isdigit()):
        print('-> ID INVALIDO <- Digite um id valido')
        idEntregador = input('ID do entregador (ex:E1234): ');
    
    nomeEntregador = str(input('Nome do entregador: '));
    veiculo = str(input('Veiculo do entregador: '));
    id_pedido = input('ID do pedido associado: ')
    if id_pedido:
        while id_pedido not in [pedido['idPedido'] for pedido in listaPedidos]:
            print('ID do pedido nao encontrado. Digite um ID valido ou deixe em branco.')
            id_pedido = input('ID do pedido associado (deixe em branco se nao tiver): ')
    print(listaEntregadores)
    print('Entregador cadastrado com sucesso')
    input('Pressione ENTER para continuar')

def atualizarPedido():
    print('''
        1. Alterar o status do pedido
        2. Cancelar Pedido
        3. Associar entregadores a pedidos
        4. Remover associação de entregador
''')
    
    n = -1

    while n != 0:

        os.system('cls')
        atualizarPedido()
        n = int(input("-> "))

        if (n == 1):

            idPedido = input('ID do pedido a ser atualizado: ')
            while idPedido not in [pedido['idPedido'] for pedido in listaPedidos]:
                print('ID do pedido nao encontrado. Digite um ID valido.')
                idPedido = input('ID do pedido a ser atualizado: ')
            
            print('''
                1. Pendente
                2. Em Rota
                3. Entregue
                4. Cancelado
            ''')
            status = int(input('Novo status do pedido: '))

            if status == 1:
                for pedido in listaPedidos:
                    if pedido['idPedido'] == idPedido:
                        pedido['status'] = 'Pendente'
                        print('Status do pedido atualizado para Pendente')
                        menu()
            elif status == 2:
                for pedido in listaPedidos:
                    if pedido['idPedido'] == idPedido:
                        pedido['status'] = 'Em Rota'
                        print('Status do pedido atualizado para Em Rota')
                        menu()
            elif status == 3:
                for pedido in listaPedidos:
                    if pedido['idPedido'] == idPedido:
                        pedido['status'] = 'Entregue'
                        print('Status do pedido atualizado para Entregue')
                        menu()
            elif status == 4:
                for pedido in listaPedidos:
                    if pedido['idPedido'] == idPedido:
                        pedido['status'] = 'Cancelado'
                        print('Status do pedido atualizado para Cancelado')
                        menu()
            else:
                print('Opcao invalida. Status não será atualizado.')
            
            input('Pressione ENTER para continuar')

        if (n == 2):

            idPedido = input('ID do pedido a ser cancelado: ')
            while idPedido not in [pedido['idPedido'] for pedido in listaPedidos]:
                print('ID do pedido nao encontrado. Digite um ID valido.')
                idPedido = input('ID do pedido a ser cancelado: ')
            
            for pedido in listaPedidos:
                if pedido['idPedido'] == idPedido:
                    print(f'Pedido encontrado: {pedido}')
                    n = str(input("Deseja mesmo cancelar esse pedido? (s/n) -> "))

                    while n.lower() != 's' and n != 'n':
                        print('Opcao invalida. Digite s para sim ou n para nao.')
                        n = str(input("Deseja mesmo cancelar esse pedido? (s/n) -> "))
                    if n.lower() == 's':
                        listaPedidos.remove(pedido)
                        input('Pedido cancelado com sucesso. Pressione ENTER para continuar')

                    elif n.lower() == 'n':
                        print('Seu pedido não será cancelado. Pressione ENTER para continuar.')
                        menu()

                    
 

def consultarInformacoes():
    n = -1
    while n != 0:
        os.system('cls')
        print('''
        1. Pedidos pendentes
        2. Pedidos entregues
        3. Buscar pedido por ID
        4. Entregadores disponiveis
        5. Entregas de um entregador
        0. Voltar
        ''')
        n = int(input('-> '))

        if n == 1:
            os.system('cls')
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
            os.system('cls')
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
            os.system('cls')
            idPedido = input('ID do pedido a buscar: ')
            encontrado = False
            for pedido in listaPedidos:
                if pedido['idPedido'] == idPedido:
                    print(f'Pedido encontrado: {pedido}')
                    encontrado = True
                    break
            if not encontrado:
                print('Pedido nao encontrado.')
            input('Pressione ENTER para continuar')

        elif n == 4:
            os.system('cls')
            print('--- ENTREGADORES DISPONIVEIS ---')
            encontrados = 0
            for entregador in listaEntregadores:
                if entregador.get('idPedido') is None:
                    print(entregador)
                    encontrados += 1
            if encontrados == 0:
                print('Nenhum entregador disponivel.')
            input('Pressione ENTER para continuar')

        elif n == 5:
            os.system('cls')
            idEntregador = input('ID do entregador: ')
            encontrado = False
            for entregador in listaEntregadores:
                if entregador['idEntregador'] == idEntregador:
                    encontrado = True
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
    os.system('cls')
    print('--- RELATORIOS OPERACIONAIS ---')
    print('''
     1. Total de pedidos
     2. Pedidos por status
     3. Pedidos de alta prioridade
     4. Entregador com maior numero de entregas
     0. Voltar 
    ''')
    opc = int(input('-> '))

    if opc == 1:
        totalPedidos = len(listaPedidos)
        print(f'Total de pedidos: {totalPedidos}')

    elif opc == 2:
        pedidos_por_status = {}
        for status in listaStatusPedido:
            pedidos_por_status[status] = 0
        for pedido in listaPedidos:
            pedidos_por_status[pedido['status']] += 1
        for status, quantidade in pedidos_por_status.items():
            print(f'{status}: {quantidade}')

    elif opc == 3:
        pedidos_alta_prioridade = []
        for pedido in listaPedidos:
            if pedido['prioridade'] == 'Alta':
                pedidos_alta_prioridade.append(pedido)
        print('--- PEDIDOS DE ALTA PRIORIDADE ---')
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
            cadastrarPedido();
        elif opcao == 2:
            cadastrarEntregador();
        elif opcao == 3:
            atualizarPedido();
        elif opcao in (6, 7, 8, 9, 10):
            consultarInformacoes();
main()