def tabuada_completa():
    while True:
        entrada = input("Digite um número inteiro para ver sua tabuada: ")
        if entrada.lstrip("-").isdigit():  # Permite número negativo também
            numero = int(entrada)
            break
        else:
            print("Entrada inválida. Por favor, digite um número inteiro válido.")

    print(f"\n=== Tabuada do {numero} ===")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

if __name__ == "__main__":
    tabuada_completa()
    
