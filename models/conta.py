from datetime import datetime

class Conta:
    def __init__(self, numero: int, cliente):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = []
        self._limite_saque = 500.0
        self._limite_saques_diario = 3
        self._saques_realizados_hoje = 0
        self._data_ultimo_saque = None

    def depositar(self, valor: float):
        if valor <= 0:
            print("Valor inválido para depósito.")
            return False

        self._saldo += valor
        self._registrar_transacao("Depósito", valor)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        return True

    def sacar(self, valor: float):
        hoje = datetime.now().date()

        if self._data_ultimo_saque != hoje:
            self._saques_realizados_hoje = 0
            self._data_ultimo_saque = hoje

        if valor <= 0:
            print("Valor de saque inválido.")
            return False
        if valor > self._saldo:
            print("Saldo insuficiente.")
            return False
        if valor > self._limite_saque:
            print(f"O valor excede o limite de R$ {self._limite_saque:.2f}.")
            return False
        if self._saques_realizados_hoje >= self._limite_saques_diario:
            print("Limite diário de saques atingido.")
            return False

        self._saldo -= valor
        self._saques_realizados_hoje += 1
        self._registrar_transacao("Saque", -valor)
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        return True

    def mostrar_extrato(self):
        print("\n========= EXTRATO =========")
        if not self._historico:
            print("Nenhuma movimentação realizada.")
        else:
            for operacao in self._historico:
                print(f"{operacao['tipo']}: R$ {operacao['valor']:.2f} em {operacao['data']}")
        print(f"\nSaldo atual: R$ {self._saldo:.2f}")
        print("============================")

    def _registrar_transacao(self, tipo: str, valor: float):
        transacao = {
            "tipo": tipo,
            "valor": valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        self._historico.append(transacao)

class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente):
        super().__init__(numero, cliente)



""" from models.historico import Historico

class Conta:
    def __init__(self, cliente, numero_conta: int, limite_saque=500.0, limite_saques_diarios=3):
        self.cliente = cliente
        self.numero_conta = numero_conta
        self.saldo = 0.0
        self.limite_saque = limite_saque
        self.limite_saques_diarios = limite_saques_diarios
        self.saques_realizados = 0
        self.historico = Historico()

    def pode_sacar(self, valor):
        if valor > self.saldo:
            return False, "Saldo insuficiente."
        if valor > self.limite_saque:
            return False, f"Valor excede limite de saque de R$ {self.limite_saque:.2f}."
        if self.saques_realizados >= self.limite_saques_diarios:
            return False, "Limite diário de saques atingido."
        if valor <= 0:
            return False, "Valor de saque deve ser positivo."
        return True, ""

    def sacar(self, valor):
        pode, msg = self.pode_sacar(valor)
        if pode:
            self.saldo -= valor
            self.saques_realizados += 1
            self.historico.adicionar_transacao(f"Saque: R$ {valor:.2f}")
            return True, f"Saque de R$ {valor:.2f} realizado com sucesso."
        return False, msg

    def depositar(self, valor):
        if valor <= 0:
            return False, "Valor de depósito deve ser positivo."
        self.saldo += valor
        self.historico.adicionar_transacao(f"Depósito: R$ {valor:.2f}")
        return True, f"Depósito de R$ {valor:.2f} realizado com sucesso."

    def extrato(self):
        return self.historico.transacoes, self.saldo

    def resetar_saques(self):
        self.saques_realizados = 0 """