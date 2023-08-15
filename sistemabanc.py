#criando um menu de opções para o sistem
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

#definindo os valores das variáveis e criando um 
saldo = 0
limite = 500 
extrato = [] #lista vazai
numero_saques = 0
LIMITE_SAQUES = 3 #definindo número de saques

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Valor do Depósito:")) #permitindo operaçoes em float
        if deposito <= 0:
            print("Não é possível depositar esse valor")
        else:
            saldo += deposito
            print("O valor depositado foi: {:.2f}".format(deposito)) 
            extrato.append({"tipo": "Depósito", "valor": deposito}) #adicionado atividade no extrato

    elif opcao == "s":
        saque = float(input("Qual valor será sacado?:"))
        if saque > saldo:
            print("Saldo insuficiente.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Limite diário de saques atingidos.")
        else:
            saldo -= saque
            numero_saques += 1
            print("Saque Autorizado")
            extrato.append({"tipo": "Saque", "valor": saque})

    elif opcao == "e":
        print("Extrato:")
        for transacao in extrato:
            print(transacao["tipo"], transacao["valor"])

        print("Seu saldo é:", saldo)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
