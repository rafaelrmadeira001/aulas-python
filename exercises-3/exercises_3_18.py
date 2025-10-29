def contador_positivos():
    positivos = 0
    for i in range(1, 11):
        while True:
            entrada = input(f"Digite o {i}º número: ").replace(",", ".")
            try:
                num = float(entrada)
                break
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
        if num > 0:
            positivos += 1
    print(f"Quantidade de números positivos: {positivos}")

if __name__ == "__main__":
    contador_positivos()
