menu = """ 
Selecione a operação desejada: 
[d] Depositar
[s] Sacar 
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n" 
            # formatação para 2 casas decimais
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
            
    
    elif opcao == "s":
        print(f"Seu saldo atual é de: {saldo}")
        print(f"Seu limite atual é de: {limite}")
        print(f"Você pode sacar {LIMITE_SAQUES} vezes")
        
        valor = float(input("Informe o valor do saque: "))
        
        if valor <= saldo and valor <= limite and numero_saques < LIMITE_SAQUES:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            LIMITE_SAQUES -= 1
            print("Saque realizado com sucesso!")
        else:
            print(f"Operação falhou! O valor informado é inválido")
        
    elif opcao == "e":
        print('\n=========Extrato=========')
        if extrato:
            print(extrato)
            print(f"\nSaldo atual: R$ {saldo:.2f}")
        else:
            print("Sem operações até o momento.")
        print("=========================")
        
    elif opcao == "q":
        break
        
    else: 
        print('Opção inválida, selecione a opção desejada novamente.')    
        
        