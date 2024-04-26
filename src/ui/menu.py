import os


def imprimirMenuPrincipal():
    print("1 - Adicionar Contato")
    print("2 - Listar Meus Contatos")
    print("3 - Editar Contato")
    print("4 - Escrever Mensagem")
    print("5 - Mostrar Mensagem")
    print("6 - Excluir Mensagem")
    print("7 - Enviar Mensagem")
    print("0 - Sair")

def limparTela():
    os.system('cls||clear')

def imprimirTitulo(titulo):
    limparTela()
    print(f"\033[1m===== {titulo} =====\033[0m\n")