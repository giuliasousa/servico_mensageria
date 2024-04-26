from models.contato import Contato
from models.mensagem import Mensagem
from ui.menu import imprimirMenuPrincipal, imprimirTitulo, limparTela
from datetime import datetime
from queue import Queue

data = datetime.now().date()
print(data)
contatos = []

minhaFila = Queue()

minhaFila.put(11)
minhaFila.put(22)
minhaFila.put(32)
minhaFila.put(42)
minhaFila.put(43)
minhaFila.put(44)

print("Minha fila está vazia?: " + str(minhaFila.empty()))

primeiroNumero = minhaFila.get()

print("Removido um item da Fila: " + str(primeiroNumero))
print(f"Faltam {minhaFila.qsize()} mensagens na Fila!\n\n")


# listaMsg = list(minhaFila.queue)
# print(listaMsg[0] , "\n\n")

# if not minhaFila.empty():
#     for msg in list(minhaFila.queue):
#         print(msg)


# Criando uma fila
# fila_mensagem = Queue()  
# dataCriacao = datetime.now().date()  

# # Obtendo a mensagem, destinatário e data do usuário
# destinatario = input("Pessoa para enviar: ")
# msgAAA = input("Digite a mensagem: ")

# # Criando um objeto Mensagem
# mensagem11 = Mensagem(destinatario, msgAAA, dataCriacao) 

# # Adicionando a mensagem à fila
# fila_mensagem.put(mensagem11)

# # Imprimindo o primeiro elemento da fila
# primeiro_elemento = fila_mensagem.queue[0]
# print("\n\nPrimeiro elemento da fila:")
# print("Destinatário:", primeiro_elemento.destinatario)
# print("Mensagem:", primeiro_elemento.mensagem)
# print("Data:", primeiro_elemento.dataCriacao)
