def calcular_fatorial():
    while True:
        entrada = input("Digite um número inteiro positivo: ")
        if entrada.isdigit():
            numero = int(entrada)
            break
        else:
            print("Por favor, digite um número inteiro válido.")

    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i

    print(f"O fatorial de {numero} é {fatorial}")

if __name__ == "__main__":
    calcular_fatorial()
  
