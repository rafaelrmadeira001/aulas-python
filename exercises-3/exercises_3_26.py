def calculadora():
    print("\n===  CALCULADORA ===")
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print("Operações: +  -  *  /")
    op = input("Escolha a operação: ")
    
    if op == '+':
        print(f"Resultado: {n1 + n2}")
    elif op == '-':
        print(f"Resultado: {n1 - n2}")
    elif op == '*':
        print(f"Resultado: {n1 * n2}")
    elif op == '/':
        if n2 != 0:
            print(f"Resultado: {n1 / n2}")
        else:
            print(" Erro: divisão por zero!")
    else:
        print(" Operação inválida!")

def conversor_temperatura():
    print("\n=== 🌡️ CONVERSOR DE TEMPERATURA ===")
    c = float(input("Digite a temperatura em °C: "))
    f = (c * 9/5) + 32
    print(f"{c}°C equivalem a {f}°F")

while True:
    print("\n=== MENU INTERATIVO ===")
    print("1. Calculadora")
    print("2. Conversor de temperatura")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        calculadora()
    elif opcao == '2':
      
        conversor_temperatura()
    elif opcao == '3':
        print(" Encerrando o programa... Até logo!")
        break
    else:
        print(" Opção inválida! Tente novamente.")
