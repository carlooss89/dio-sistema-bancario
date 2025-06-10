## 💰 Sistema Bancário em Python - Bootcamp DIO 🟡🔵🐍

Este é um sistema bancário simples e funcional desenvolvido em Python como parte do **desafio prático do Bootcamp Backend com Python da DIO**.
O projeto aplica **boas práticas de programação**, como **orientação a objetos (POO)**, **modularização** e uma **interface via terminal (CLI)** para facilitar o uso e a organização do código.

---

## ✅ Funcionalidades
- 👤 Criação de clientes com validação de CPF e endereço
- 🏦 Criação de contas bancárias para clientes existentes
- ➕ Depósitos em conta
- ➖ Saques com:
- Limite de 3 saques por dia
- Valor máximo de R$ 500,00 por saque
- 📄 Emissão de extrato com histórico de transações
- 🖥️ Interface via terminal com menu interativo


---
## 🚀 Como executar
## 1. Clone este repositório:

```git clone https://github.com/carlooss89/dio-sistema-bancario.git```

## 2. Navegue até a pasta do projeto:
````cd dio-sistema-bancario````

## 3. Execute o sistema:
````python main.py````

---

📌 Pré-requisitos:
**Python 3.10** ou superior instalado na sua máquina

---

## 4.  📁 Estrutura do Projeto
├── main.py                  # Arquivo principal para execução <br>
├── menu.py                  # Menu de opções via terminal <br>
├── models/ <br>
│   ├── cliente.py           # Classe Cliente <br>
│   ├── conta.py             # Classe ContaCorrente <br>
│   ├── historico.py         # Registro de transações <br>
│   └── transacoes.py        # Saque, Depósito, Transação base <br>
├── services/ <br>
│   ├── operacoes.py         # Regras de negócio para operações bancárias <br>
│   └── utils.py             # Validações e utilitários <br>

---

## 5. 🛠️ Tecnologias Utilizadas
- Python 3.10+
- Programação Orientada a Objetos
- Interface via Terminal (CLI)
  
---

## 6. 👨‍💻 Autor
**Carlos Eduardo**
🔗 [GitHub](https://github.com/carlooss89)
