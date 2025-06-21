menu = """
======================👉Banco👈=====================

                 🏧Sistema de banco🏧

                  Digite uma opição:

      👉[1] Deposito

      👉[2] Saque

      👉[3] Extrato

      👉[4] Sair


======================👉Banco👈=====================
"""

saldo            = 0
limite           = 500
extrato          = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:

    opicao = input(menu)

    if opicao == "1":
        valor_deposito = float(input("Digite o valor do deposito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opicao == "2":
        valor_saque = float(input("Digite o valor do saque: "))
        if valor_saque > limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif valor_saque > saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif numero_de_saques >= LIMITE_DE_SAQUES:
            print("Operação falhou! Número máximo de saques atingido.")
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque:    R$ {valor_saque:.2f}\n"
            numero_de_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opicao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opicao == "4":
        print("Saindo do sistema. Obrigado por usar nosso banco!")
        break
