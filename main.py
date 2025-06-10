from menu import menu

def main():
    clientes = []  # Lista que armazenará os objetos Cliente
    contas = []    # Lista que armazenará os objetos ContaCorrente

    print("Bem-vindo ao sistema bancário!")
    menu(clientes, contas)  # Chama o menu principal, passando as listas para manipulação

if __name__ == "__main__":
    main()
