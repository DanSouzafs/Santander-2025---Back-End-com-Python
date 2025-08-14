import textwrap
<<<<<<< HEAD

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
=======
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
from pathlib import Path

ROOT_PATH = Path(__file__).parent

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    def __init__(self, contas):
        self.contas = contas
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            conta = self.contas[self._index]
            return f"""\
            Agência:\t{conta.agencia}
            Número:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t\tR$ {conta.saldo:.2f}
            """
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1
>>>>>>> 2bb4b59 (Refatorar sistema bancário: implementar classes de cliente, conta e transações)

def depositar(saldo, valor, extrato, /):
    clear()
    valor = float(input("Digite o valor do deposito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n^^^ Depósito realizado com sucesso! ^^^")
    else:
        print("\n--- Operação falhou! O valor informado é inválido. ---")

<<<<<<< HEAD
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
=======
class ContasIterador:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self._index]
            return f"""\
            Agência:\t{conta.agencia}
            Número:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t\tR$ {conta.saldo:.2f}
        """
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        self.indice_conta = 0

    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >= 10:
            print("\n--- Você exedeu o número de transações permitidas para hoje! ---")
            return

        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: ('{self.cpf}')>"

class Conta: 
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n--- Operação falhou! Saldo insuficiente. ---")

        elif valor > 0:
            self._saldo -= valor
            print("\n^^^ Saque realizado com sucesso! ^^^")
            return True

        else:
            print("\n--- Operação falhou! O valor informado é inválido. ---")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n^^^ Depósito realizado com sucesso! ^^^")
        else:
            print("\n--- Operação falhou! O valor informado é inválido. ---")
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n--- Operação falhou! O valor do saque excede o limite. ---")

        elif excedeu_saques:
            print("\n--- Operação falhou! Número máximo de saques excedido. ---")

        else:
            return super().sacar(valor)

        return False

    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.agencia}', '{self.numero}', '{self.cliente.nome}')>"

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if (
                tipo_transacao is None
                or transacao["tipo"].lower() == tipo_transacao.lower()
            ):
                yield transacao

    def transacoes_do_dia(self):
        data_atual = datetime.utcnow().date()
        transacoes = []
        
        print(f"\nVerificando transações do dia {data_atual}")
        
        for transacao in self._transacoes:
            try:
                data_transacao = datetime.strptime(transacao["data"], "%d-%m-%Y %H:%M:%S").date()
                print(f"Transação encontrada: {transacao['tipo']} - Data: {data_transacao}")
                
                if data_atual == data_transacao:
                    transacoes.append(transacao)
            except ValueError as e:
                print(f"Erro ao processar data da transação: {e}")
                print(f"Data problemática: {transacao['data']}")
        
        print(f"Total de transações do dia: {len(transacoes)}")
        return transacoes


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
    

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        data_hora = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        with open(ROOT_PATH / "log.txt", "a") as arquivo:
            arquivo.write(
                f"[{data_hora}] Função '{func.__name__}' executada com argumentos {args} e {kwargs}. "
                f"Retornou {resultado}\n"
            )
        return resultado

    return envelope

def menu():
    menu = """\n
    =======================Banco======================

                    Sistema de banco

                    Digite uma opição:

                [d] \tDepositar
                [s] \tSacar
                [e] \tExtrato
                [nc]\tNova conta
                [lc]\tListar contas
                [nu]\tNovo usuário
                [q] \tSair

    =====================Banco======================
    """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n--- Cliente não possui conta! ---")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]


@log_transacao
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n--- Cliente não encontrado! ---")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


@log_transacao
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n--- Cliente não encontrado! ---")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

@log_transacao
def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n--- Cliente não encontrado! ---")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    extrato = ""
    tem_transacao = False
    for transacao in conta.historico.gerar_relatorio():
        tem_transacao = True
        extrato += f"\n{transacao['data']}\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    if not tem_transacao:
        extrato = "Não foram realizadas movimentações"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    transacoes = conta.historico.transacoes
    print("==========================================")


@log_transacao
def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n--- Já existe cliente com esse CPF! ---")
>>>>>>> 2bb4b59 (Refatorar sistema bancário: implementar classes de cliente, conta e transações)
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

<<<<<<< HEAD
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
=======
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n^^^ Cliente criado com sucesso! ^^^")


@log_transacao
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n--- Cliente não encontrado, fluxo de criação de conta encerrado! ---")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n^^^ Conta criada com sucesso! ^^^")


def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            print("""
            TENHA UM BOM
                DIA!
            _________
           /        /\\
          / BANCO  /  \\
         /_______ /____\\
         | _   _| |    |
         ||_| |_| |    |
         |  | |   |    |
         |  | |   |    |
         |  | |   |    |
        /|__|_|___|____|\\
       /                 \\
      /___________________\\
           /        \\
          /          \\
         /            \\
         O
        /|\\
        / \\
            """)
            break
        else:
            print("\n--- Operação inválida, por favor selecione novamente a operação desejada. ---")


main()
>>>>>>> 2bb4b59 (Refatorar sistema bancário: implementar classes de cliente, conta e transações)
