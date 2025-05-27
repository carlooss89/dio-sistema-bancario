# sistema_bancario.py

def main():
    # Variáveis principais
    saldo = 0.0
    limite_saque = 500.0
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        print("""
        ======== MENU ========
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
        ======================
        """)
        
        opcao = input("Escolha uma opção: ").lower()

        # Início da função de depósito
        if opcao == "d":
            try:
                valor = float(input("Digite o valor do depósito: "))
            except ValueError:
                print("Valor inválido! Tente novamente.")
                continue

            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito: R$ {valor:.2f}")
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("O valor do depósito deve ser positivo.")
        # Fim da função de depósito

        # Início da função de saque
        elif opcao == "s":
            if numero_saques >= LIMITE_SAQUES:
                print("Limite diário de saques atingido.")
                continue

            try:
                valor = float(input("Digite o valor do saque: "))
                
                if valor <= 0:
                    print("O valor do saque deve ser positivo.")
                    
                elif valor > saldo:
                    print("Saldo insuficiente para saque.")
                    
                elif valor > limite_saque:
                    print(f"O valor do saque excede o limite de R$ {limite_saque:.2f}.")
                    
                else:
                    saldo -= valor
                    extrato.append(f"Saque: R$ {valor:.2f}")
                    numero_saques += 1
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
                    
            except ValueError:
                print("Valor inválido! Tente novamente.")
        # Fim da função de saque

        # Início da função de extrato
        elif opcao == "e":
            print("\n========== EXTRATO ==========")
        
            if not extrato:
                print("Não foram realizadas movimentações.")
            else:
                for movimento in extrato:
                    print(movimento)
        
            print(f"\nSaldo atual: R$ {saldo:.2f}")
            print("==============================")
        # Fim da função de extrato

        # Início da opção de sair
        elif opcao == "q":
            print("Saindo... Obrigado por utilizar nosso sistema bancário!")
            break
        # Fim da opção de sair
            
if __name__ == "__main__":
    main()