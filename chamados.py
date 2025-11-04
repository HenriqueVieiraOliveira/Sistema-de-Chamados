import os
import time
import sys

def open_ticket(tickets_list):
    clear_terminal()
    print("--Abertura de chamado--")
    title_ticket = input("Insira o título do chamado: ")
    tickets_list.append(title_ticket)
    time.sleep(2)

def display_tickets(tickets_list):
    clear_terminal()
    print("--Lista de chamados--")
    for ticket in tickets_list:
        print(ticket)
    time.sleep(5)

def resolve_ticket(tickets_list):
    clear_terminal()
    print("--Resolução de chamado--")
    title_ticket = input("Insira o título do chamado que deseja concluir: ")
    if title_ticket in tickets_list:
        tickets_list.remove(title_ticket)
    else:
        print("Chamado não encontrado!")    
    time.sleep(2)

def edit_ticket(tickets_list):
    print("--Edição de chamado--")
    print("Olá")

def menu():
    print("""1 - Abrir chamado
2 - Exibir chamados
3 - Fechar chamado
4 - Atualizar chamado
5 - Sair
              """) 
    
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    tickets_list = []
    while True:
        clear_terminal()
        menu()
        
        try:
            choice = int(input("Escolha uma opção: "))
        except:
            print("Digite um número válido!")
            time.sleep(2)
            continue
        
        match choice:
            case 1:
                open_ticket(tickets_list)
            case 2:
                display_tickets(tickets_list)
            case 3:
                resolve_ticket(tickets_list)
            case 4:
                edit_ticket(tickets_list)
            case 5:
                sys.exit(0)
            case _:
                print("Insira uma opção válida!")
        
        time.sleep(2)

if __name__ == "__main__":
    main()