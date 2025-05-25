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

        # Aqui vamos implementar as operações

if __name__ == "__main__":
    main()
