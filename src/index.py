from models.contato import Contato
from models.mensagem import Mensagem
from ui.menu import imprimirMenuPrincipal, imprimirTitulo, limparTela
from time import sleep
from datetime import datetime
from queue import Queue


data = datetime.now().date()
# print(data)
contatos = []
fila_mensagem = Queue()

# FUNÇÕES
def AdicionarContato():
    imprimirTitulo("Criar Novo Contato")

    (nome, numero) = ObterDadosParaCadastroUsuario()

    novoContato = Contato(nome, numero)
    contatos.append(novoContato)

    print("\n\033[32mContato Criado com Sucesso!\033[0m")
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()


def ImprimirListaDeContatos():
    imprimirTitulo("Meus Contatos")

    if not any(contatos):
        print("\nSua lista de contatos está vazia!")
    else:
        ListarContatos()


    # for i in range(len(contatos)):
    #     print(contatos[i].nome)

    input("\n[APERTE ENTER PARA CONTINUAR]")
    limparTela()


def EditarContato():
    print()
    if not any(contatos):
        print("\nVocê não possui nenhum contato para alterar")
        return

    ListarContatos()
    idxUsuario = int(input("Escolha um contato para alterar pelo número(#): ")) - 1
   
    try:
        (nome, numero) = ObterDadosParaCadastroUsuario(True)
        contatos[idxUsuario].nome = nome
        contatos[idxUsuario].numero = numero
    except:
        sleep(.7)
        print("\n\033[1;31mErro! Não conseguimos editar o contato...\033[0m")
        sleep(1.8)
        return

    print("\n\033[32mContato Atualizado com Sucesso\033[0m")
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()


def EscreverMensagem():
    imprimirTitulo("Mensagens Diretas")

    ListarContatos(); print()
    msg_dest1 = input("Nome do contato: ").strip()
    msg_dest2 = input("Número do contato: ").strip()

    #verifica se o nome e o numero existem
    contato_existente = False
    for i in range(len(contatos)):
        if (msg_dest1.upper() == contatos[i].nome.upper()) and (msg_dest2==contatos[i].numero):
            contato_existente = True
            break

    #se contato nao existir, encerra a ação e volta ao menu
    if contato_existente==False:
        print("\n\033[31mDestinatário não existente!\033[0m")
        sleep(1.8)
        limparTela()
        sleep(0.4)
        return
    
    # instancia nome e nmr no objeto destinatario
    destinatario = Contato(msg_dest1, msg_dest2); sleep(0.4)
    msg = input("\nDigite a mensagem: ")
    
    #instancia destinatario, msg e data no objeto Mensagem()
    mensagem = Mensagem(destinatario, msg, data)
    
    # destinatario = Contato("Contato para envio", "Numero para envio")
    # mensagem = Mensagem(destinatario, "Mensagem", "01/01/2024")
    
    # adc o objeto mensagem na fila_mensagem
    fila_mensagem.put(mensagem)
    print("\033[32m\nMensagem Criada com Sucesso!\033[0m")
    print(f"A fila tem {fila_mensagem.qsize()} mensagens\n")  

    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()


def MostrarMensagem():
    imprimirTitulo("Próxima Mensagem")
    if (fila_mensagem.empty()):
        print("\033[31mNão há mais mensagens!\033[0m")
        sleep(1.8)
        return

    ExibicaoMensagem();
   
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()


def EnviarMensagem():
    imprimirTitulo("Enviar Mensagem")
    sleep(0.8)

    if (fila_mensagem.empty()):
        print("\033[31mNão há mais mensagens!\033[0m")
        sleep(1.8)
        return

    #pega a 1° msg da fila e passa cada elemento em uma lista. assim, quando apagar o 1° elemento da fila, os valores estarão guardados na lista para aparecer depois
    
    # prox_msg = fila_mensagem.queue[0]
    # lista_mensagem = [prox_msg.destinatario.nome, prox_msg.mensagem, prox_msg.dataCriacao]

    # print(f"Enviando mensagem para {lista_mensagem[0]}...")
    # fila_mensagem.get()
    # sleep(1.3)
    # print(f"\n\033[4mSobraram {fila_mensagem.qsize()} mensagens na lista.\033[0m")
    # print(f"""\n\033[32mMensagem enviada:\033[0m
    #     \033[3;90mDestinatário\033[0m: {lista_mensagem[0]}.
    #     \033[3;90mConteúdo\033[0m: ''{lista_mensagem[1]}''.
    #     \033[3;90mData\033[0m: {lista_mensagem[2]}.
    #       """)
    

    mensagem_enviada = fila_mensagem.get()
    print(f"\033[3mSobraram {fila_mensagem.qsize()} mensagens na lista.\033[0m\n"); sleep(0.8)
    print(f"A mensagem: '\033[4m{mensagem_enviada.mensagem}\033[0m' foi enviada com \033[32msucesso\033[0m para o contato \033[1m{mensagem_enviada.destinatario.nome.capitalize()}.\033[0m")


    input("\n[APERTE ENTER PARA CONTINUAR]")
    limparTela()


def ExcluirMensagem():
    if (fila_mensagem.empty() == False):
        fila_mensagem.get()
        print("\033[31m\nMensagem excluida\033[0m"); sleep(0.9)
        print(f"Agora você tem {fila_mensagem.qsize()} mensagens na fila.")
        sleep(1.4)
    else:
        print("\033[3;33m\nNenhuma mensagem encontrada ...\033[0m")
        sleep(1.4)
        return
        
    limparTela()




###################################



#FUNÇÕES SECUNDÁRIAS
def ObterDadosParaCadastroUsuario(paraEdicao = False):
    contatoValido = False
    mensagemNome = "Digite o nome do contato: " if not paraEdicao else "Digite o novo nome do contato: "
    mensagemNumero = "Digite o numero de telefone do contato: " if not paraEdicao else "Digite o novo numero de telefone do contato: "

    while not contatoValido:
        nome = input(mensagemNome)
        numero = input(mensagemNumero)

        contatoExiste = any(contato.nome == nome and contato.numero == numero for contato in contatos)

        if nome == "" and numero == "":
            print("\nNome ou Numero de Telefone estão inválidos! Favor digite novamente!\n")
        elif contatoExiste:
            print("\nContato Já Existe na Base! Favor incluir outro!\n")
        else:
            contatoValido = True

    return (nome, numero)

def ListarContatos():
    for i in range(0, len(contatos)):
        print(f"#{i + 1} | \033[1m{contatos[i].nome}\033[0m | {contatos[i].numero}")

def ExibicaoMensagem():
    prox_msg = fila_mensagem.queue[0]
    print(f"Destinatário: {prox_msg.destinatario.nome}")
    print(f"\n\033[3m{prox_msg.mensagem}\033[0m")
    print(f"\n\033[90m{prox_msg.dataCriacao}\033[0m")


# PROGRAMA PRINCIPAL

fimPrograma = False

while not fimPrograma:
    imprimirTitulo("SISTEMA DE MENSAGENS")
    imprimirMenuPrincipal()
    opcao = input("Escolha uma das opções: ")

    if int(opcao) == 1:
        AdicionarContato()
    elif int(opcao) == 2:
        ImprimirListaDeContatos()
    elif int(opcao) == 3:
        EditarContato()
    elif int(opcao) == 4:
        EscreverMensagem()
    elif int(opcao) == 7:
        EnviarMensagem()
    elif int(opcao) == 5:
        MostrarMensagem()
    elif int(opcao) == 6:
        ExcluirMensagem()
    elif int(opcao) == 0:
        fimPrograma = True
    else:
        print("Opção Errada! Favor escolha uma opção válida")
        input("[APERTE ENTER PARA CONTINUAR]")
        limparTela()

print("===== FIM DO PROGRAMA =====\n")