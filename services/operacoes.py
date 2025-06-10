from datetime import datetime

def depositar(conta, valor: float) -> bool:
    """Realiza depósito na conta se o valor for válido."""
    if valor <= 0:
        print("Valor inválido para depósito.")
        return False
    conta._saldo += valor
    conta._registrar_transacao("Depósito", valor)
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    return True

def sacar(conta, valor: float) -> bool:
    """Realiza saque na conta respeitando limites e saldo."""
    hoje = datetime.now().date()

    if conta._data_ultimo_saque != hoje:
        conta._saques_realizados_hoje = 0
        conta._data_ultimo_saque = hoje

    if valor <= 0:
        print("Valor de saque inválido.")
        return False
    if valor > conta._saldo:
        print("Saldo insuficiente.")
        return False
    if valor > conta._limite_saque:
        print(f"O valor excede o limite de R$ {conta._limite_saque:.2f}.")
        return False
    if conta._saques_realizados_hoje >= conta._limite_saques_diario:
        print("Limite diário de saques atingido.")
        return False

    conta._saldo -= valor
    conta._saques_realizados_hoje += 1
    conta._registrar_transacao("Saque", -valor)
    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    return True

def mostrar_extrato(conta):
    """Exibe o extrato da conta."""
    print("\n========= EXTRATO =========")
    if not conta._historico:
        print("Nenhuma movimentação realizada.")
    else:
        for operacao in conta._historico:
            print(f"{operacao['tipo']}: R$ {operacao['valor']:.2f} em {operacao['data']}")
    print(f"\nSaldo atual: R$ {conta._saldo:.2f}")
    print("============================")
