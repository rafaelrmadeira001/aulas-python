print("=== VALIDAÇÃO DE ENTRADA ===")

numero = int(input("Digite um número entre 1 e 100: "))

while numero < 1 or numero > 100:
    print(" Número inválido! Tente novamente.")
    numero = int(input("Digite um número entre 1 e 100: "))

print(f" Número válido: {numero}")
