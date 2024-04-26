from models.contato import Contato
from models.mensagem import Mensagem
from ui.menu import imprimirMenuPrincipal, limparTela
import time

lista = []

# FUNÇÕES
def AdicionarContato():
    # ESCREVER LÓGICA AQUI!
    nome = input("Nome do contato: ")
    nmr = input("Numero do contato (só numeros, sem espaço): ")


    igual = 0
    for i in range(len(lista)):
        if nmr == lista[i].numero:
          igual+=1


    if igual >0:
        print("\033[1;31mContato duplicado! Não Permitido\033[0m")
        time.sleep(2)
        pass
    else:
        print("\n\033[1mUsuário Criado com Sucesso!\033[0m")
        contato = Contato(nome, nmr)
        lista.append(contato)

    
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

def MostrarContatos():
    # ESCREVER LÓGICA AQUI

    print("\n \033[1mMostrando lista de contatos\033[0m")
    for i in range(len(lista)):
        print(lista[i].nome, " | ", lista[i].numero)

    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

def EditarContato():
    time.sleep(1)
    print("\n \033[1mMostrando lista de contatos\033[0m")
    for i in range(len(lista)):
        print(lista[i].nome, " | ", lista[i].numero)
    print("\n")

    time.sleep(1.3)

    nomeEditar = input("\033[1mDigite o nome a ser editado: \033[0m").strip()
    
    for i in range(len(lista)):
        if nomeEditar == lista[i].nome:
            lista[i].nome = input("\nEscreva o nome: ").strip()
            lista[i].numero = input("Escreva o numero: ").strip()

            print(f"\nContato \033[1m{nomeEditar}\033[0m alterado para \033[1m{lista[i].nome}\033[0m!!!")
            time.sleep(1.3)
            limparTela()
            break

    else:
        print("\nNome não encontrado\n")
            
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

def EscreverMensagem():
    # Exemplo de criação de uma mensagem
    print("\nOpção em desenvolvimento\n")
    # destinatario = Contato("Contato para envio", "Numero para envio")
    # mensagem = Mensagem(destinatario, "Mensagem", "01/01/2024")

    # print("Mensagem Criada com Sucesso!")
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()


# PROGRAMA PRINCIPAL
print("===== SISTEMA DE MENSAGENS =====\n")

fimPrograma = False

while not fimPrograma:
    imprimirMenuPrincipal()
    opcao = input("Escolha uma das opções: ")

    if int(opcao) == 1:
        AdicionarContato()
    elif int(opcao) == 2:
        MostrarContatos()
    elif int(opcao) == 3:
        EditarContato()
    elif int(opcao) == 4:
        EscreverMensagem()
    elif int(opcao) == 0:
        fimPrograma = True
    else:
        print("Opção Errada! Favor escolha uma opção válida")
        input("[APERTE ENTER PARA CONTINUAR]")
        limparTela()

print("===== FIM DO PROGRAMA =====\n")