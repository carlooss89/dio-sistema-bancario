class Cliente:
    def __init__(self, nome: str, cpf: str, data_nascimento: str, endereco: str):
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        self._endereco = endereco
        self._contas = []

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    @property
    def endereco(self):
        return self._endereco

    @property
    def contas(self):
        return self._contas

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def obter_conta_ativa(self):
        return self._contas[-1] if self._contas else None

    def __str__(self):
        return f"Cliente: {self._nome} | CPF: {self._cpf} | Nascimento: {self._data_nascimento} | Endereço: {self._endereco}"
