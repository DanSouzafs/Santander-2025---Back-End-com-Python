import textwrap

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    menu = """\n
    =======================Banco======================

                    Sistema de banco

                    Digite uma opição:

        [d]\tDeposito
        [s]\tSaque
        [e]\tExtrato
        [nu]\tNova conta
        [lc]\tListar contas
        [nc]\tNovo usuário
        [q]\tSair

    =====================Banco======================
    """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    clear()
    valor = float(input("Digite o valor do deposito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n^^^ Depósito realizado com sucesso! ^^^")
    else:
        print("\n--- Operação falhou! O valor informado é inválido. ---")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_de_saques, limite_de_saques): 
        clear()
        exedeu_saldo = valor > saldo
        exedeu_limite = valor > limite
        exedeu_saques = numero_de_saques >= limite_de_saques

        if exedeu_saldo:
            print("\n--- Operação falhou! O valor do saque excede o limite. ---")

        elif exedeu_limite:
            print("\n--- Operação falhou! Saldo insuficiente. ---")

        elif exedeu_saques:
            print("\n--- Operação falhou! Número máximo de saques atingido. ---")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            numero_de_saques += 1
            print("\n^^^ Saque realizado com sucesso! ^^^")

        else:
            print("\n--- Operação falhou! O valor informado é inválido. ---")
        
        return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
        clear()
        print("\n================ EXTRATO ================")
        print("--- Não foram realizadas movimentações ---." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    clear()
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n^^^ Conta criada com sucesso! ^^^")
        return {"agencia": agencia, "numero": numero_conta, "titular": usuario}
    else:
        print("--- Usuário não encontrado. Conta não criada. ---")
        return None

def listar_contas(contas):
    clear()
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in contas:
            print(f"Agência: {conta['agencia']} | Conta: {conta['numero']} | Titular: {conta['titular']['nome']}")

def sair():
        print("Saindo do sistema. Obrigado por usar nosso banco!")


def main():
    LIMITE_DE_SAQUES = 3
    AGENCIA = "0001"

    saldo            = 0
    limite           = 500
    extrato          = ""
    numero_de_saques = 0
    usuarios = []
    contas = []

    while True:
        opicao = menu()

        if opicao == "d":
            valor = float(input("Digite o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opicao == "s":
            valor = float(input("Digite o valor do saque: "))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor, 
                extrato=extrato, 
                limite=limite, 
                numero_de_saques=numero_de_saques,
                limite_de_saques=LIMITE_DE_SAQUES,
            )

        elif opicao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opicao == "nu":
            criar_usuario(usuarios)

        elif opicao == "lc":
            listar_contas(contas)
        
        elif opicao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
             
        elif opicao == "q":
            break

        else:
            print("\n--- Operação inválida, por favor selecione novamente a operação desejada. ---")
main()
