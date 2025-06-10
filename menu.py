import re
from models.cliente import Cliente
from models.conta import ContaCorrente
from services.operacoes import depositar, sacar, mostrar_extrato

def validar_endereco(endereco: str) -> bool:
    # Endereço esperado: logradouro, nro - bairro - cidade/sigla estado
    # Exemplo: Rua A, 123 - Centro - São Paulo/SP
    padrao = r"^[^,]+, \d+ - [^-]+ - [^/]+/[A-Z]{2}$"
    return bool(re.match(padrao, endereco))

def limpar_cpf(cpf: str) -> str:
    # Remove qualquer caractere que não seja número
    return re.sub(r'\D', '', cpf)

def criar_cliente(clientes: list):
    nome = input("Nome do cliente: ").strip()
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()
    
    while True:
        cpf = input("CPF (somente números, pode digitar com pontos/traço): ").strip()
        cpf_limpo = limpar_cpf(cpf)
        if len(cpf_limpo) != 11:
            print("CPF inválido! Deve conter 11 números.")
            continue
        # Verificar duplicidade
        if any(c.cpf == cpf_limpo for c in clientes):
            print("CPF já cadastrado! Tente outro.")
            continue
        break
    
    while True:
        endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ").strip()
        if not validar_endereco(endereco):
            print("Endereço inválido! Use o formato: logradouro, nro - bairro - cidade/sigla estado")
            continue
        break
    
    cliente = Cliente(nome, cpf_limpo, data_nascimento, endereco)
    clientes.append(cliente)
    print(f"Cliente {nome} criado com sucesso!")

def selecionar_conta(contas):
    print("Contas disponíveis:")
    for i, conta in enumerate(contas):
        print(f"{i}: Conta {conta._numero} - Cliente: {conta._cliente.nome}")
    try:
        idx = int(input("Escolha o número da conta: "))
        return contas[idx]
    except (ValueError, IndexError):
        print("Opção inválida.")
        return None

def menu(clientes, contas):
    while True:
        print("""
        ======== MENU ========
        [nu] Novo usuário (cliente)
        [nc] Nova conta
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
        ======================
        """)

        opcao = input("Escolha uma opção: ").lower()

        if opcao == 'nu':
            criar_cliente(clientes)

        elif opcao == 'nc':
            if not clientes:
                print("Nenhum cliente cadastrado. Crie um cliente primeiro.")
                continue
            print("Clientes disponíveis:")
            for i, c in enumerate(clientes):
                print(f"{i}: {c.nome} | CPF: {c.cpf}")
            try:
                idx = int(input("Escolha o número do cliente para criar conta: "))
                cliente_selecionado = clientes[idx]
            except (ValueError, IndexError):
                print("Opção inválida.")
                continue
            numero_conta = len(contas) + 1
            conta = ContaCorrente(numero_conta, cliente_selecionado)
            contas.append(conta)
            print(f"Conta número {numero_conta} criada para {cliente_selecionado.nome}.")

        elif opcao == 'd':
            if not contas:
                print("Nenhuma conta cadastrada. Crie uma conta primeiro.")
                continue
            conta = selecionar_conta(contas)
            if conta:
                try:
                    valor = float(input("Digite o valor do depósito: "))
                except ValueError:
                    print("Valor inválido! Tente novamente.")
                    continue
                depositar(conta, valor)

        elif opcao == 's':
            if not contas:
                print("Nenhuma conta cadastrada. Crie uma conta primeiro.")
                continue
            conta = selecionar_conta(contas)
            if conta:
                try:
                    valor = float(input("Digite o valor do saque: "))
                except ValueError:
                    print("Valor inválido! Tente novamente.")
                    continue
                sacar(conta, valor)

        elif opcao == 'e':
            if not contas:
                print("Nenhuma conta cadastrada. Crie uma conta primeiro.")
                continue
            conta = selecionar_conta(contas)
            if conta:
                mostrar_extrato(conta)

        elif opcao == 'q':
            print("Saindo... Obrigado por utilizar nosso sistema bancário!")
            break

        else:
            print("Opção inválida. Tente novamente.")
