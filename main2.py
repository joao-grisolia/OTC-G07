import os

listaPedidos = []
listaEntregadores = []
listaPrioridades = ['Alta', 'Normal']
listaStatusPedido = ['Pendente', 'Em Rota', 'Entregue', 'Cancelado']

def cadastrarPedido():
    os.system('cls');
    idPedido = input('ID do pedidto (ex:B2345): ');
    while not (len(idPedido) == 5 and idPedido[0].isalpha() and idPedido[1:].isdigit()):
        # ele so entra no while se as condicoes nao forem  True
        # por isso do not
        # as condicoes são o tamanho do idPedido tem que ser 5 (len(idPedido) == 5)
        # o primeiro indice tem que ser uma letra idPedido[0].isalpha()
        # o outros tem que que ser numero idPedido[1:].isdigit()
        # enquanto nao (while not) cumprir com nenhum desse requisitos entra aqui no while
        print('-> ID INVALIDO <- Digite um id valido')
        idPedido = input('ID do pedidto (ex:B2345): ');
    # aqui tem que fazer uma validacao pra ver se ja tem um
    # pedido com o idPedido ja cadastrado, idPedido duplicado
        
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
    #falta colocar disponibilidade do pedido!
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
main()