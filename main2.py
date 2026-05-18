import os

listaPedidos = []
listaEntregadores = []
listaPrioridades = ['Alta', 'Normal', 'Baixa']
listaStatusPedido = ['PENdente', 'Em Rota', 'Entregue', 'Cancelado']

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
    prioridade = str(input('Prioridade (Alta/Normal/Baixa): '));
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
main()