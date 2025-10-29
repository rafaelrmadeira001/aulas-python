def piramide_asteriscos():
    while True:
        entrada = input("Quantas linhas deseja na pirâmide? (ex: 5): ")
        if entrada.isdigit():
            linhas = int(entrada)
            break
        else:
            print("Por favor, digite um número inteiro válido.")

    print("\n=== Pirâmide de Asteriscos ===")
    for i in range(1, linhas + 1):
        print("*" * i)

if __name__ == "__main__":
    piramide_asteriscos()
    
