def numeros_primos():
    print("=== Números primos entre 1 e 30 ===")

    # Percorre os números de 2 até 30 (1 não é primo)
    for numero in range(2, 31):
        eh_primo = True  # Assume que o número é primo

        # Testa divisores de 2 até a raiz quadrada do número
        for divisor in range(2, int(numero ** 0.5) + 1):
            if numero % divisor == 0:
                eh_primo = False
                break  # Não é primo, pode parar o teste

        # Se não encontrou divisores, imprime o número
        if eh_primo:
            print(numero)

if __name__ == "__main__":
    numeros_primos()
    
