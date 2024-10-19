usuarios = []
contas = []
proximo_numero_conta = 1
agencia = "0001"
saldo = 0.0
limite_saque = 500.00
limite_saques_diarios = 3
saques_realizados = 0
depositos = []
saques = []

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    cpf = input("Digite o CPF (somente números): ")
    endereco = input("Digite o endereço (Formato: rua, número, bairro - cidade/sigla do estado): ")

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("CPF já cadastrado. Não é possível registrar outro usuário com o mesmo CPF.")
            return
    
    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(novo_usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")

def criar_conta():
    cpf = input("Digite o CPF do usuário para criar a conta: ")
    
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuario_encontrado = usuario
            break
    
    if not usuario_encontrado:
        print("Usuário não encontrado. Verifique o CPF e tente novamente.")
        return

    global proximo_numero_conta
    nova_conta = {
        "agencia": agencia,
        "numero_conta": proximo_numero_conta,
        "usuario": usuario_encontrado
    }
    contas.append(nova_conta)
    print(f"Conta criada com sucesso! Agência: {agencia}, Conta: {proximo_numero_conta}")
    proximo_numero_conta += 1

def depositar(valor, /):
    global saldo
    if valor > 0:
        depositos.append(valor)
        saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")

def sacar(*, valor):
    global saldo, saques_realizados
    if saques_realizados >= limite_saques_diarios:
        print("Limite diário de saques atingido.")
    elif valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
    elif valor > limite_saque:
        print(f"Valor máximo por saque é R$ {limite_saque:.2f}.")
    else:
        saques.append(valor)
        saldo -= valor
        saques_realizados += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

def exibir_extrato(saldo_atual, /, *, extrato):
    print("\n===== EXTRATO =====")
    print("Depósitos:")
    if len(extrato['depositos']) > 0:
        for deposito in extrato['depositos']:
            print(f"R$ {deposito:.2f}")
    else:
        print("Nenhum depósito realizado.")
    
    print("\nSaques:")
    if len(extrato['saques']) > 0:
        for saque in extrato['saques']:
            print(f"R$ {saque:.2f}")
    else:
        print("Nenhum saque realizado.")
    
    print(f"\nSaldo atual: R$ {saldo_atual:.2f}")
    print("====================\n")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}, CPF: {usuario['cpf']}")

def listar_contas():
    if not contas:
        print("Nenhuma conta criada.")
        return
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, Usuário: {conta['usuario']['nome']}")

def main():
    while True:
        print("\n===== MENU =====")
        print("[1] Cadastrar Usuário")
        print("[2] Criar Conta")
        print("[3] Depósito")
        print("[4] Saque")
        print("[5] Extrato")
        print("[6] Listar Usuários")
        print("[7] Listar Contas")
        print("[8] Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()

        elif opcao == "2":
            criar_conta()

        elif opcao == "3":
            valor_deposito = float(input("Digite o valor do depósito: "))
            depositar(valor_deposito)

        elif opcao == "4":
            valor_saque = float(input("Digite o valor do saque: "))
            sacar(valor=valor_saque)

        elif opcao == "5":
            extrato_dados = {
                "depositos": depositos,
                "saques": saques
            }
            exibir_extrato(saldo, extrato=extrato_dados)

        elif opcao == "6":
            listar_usuarios()

        elif opcao == "7":
            listar_contas()

        elif opcao == "8":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

main()