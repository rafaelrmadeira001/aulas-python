def repetir_palavra():
    palavra = input("Digite uma palavra: ")
    while True:
        vezes_str = input("Quantas vezes deseja imprimir essa palavra? ")
        if vezes_str.isdigit() and int(vezes_str) >= 0:
            vezes = int(vezes_str)
            break
        print("Entrada inválida. Digite um número inteiro não-negativo.")
    for _ in range(vezes):
        print(palavra)

if __name__ == "__main__":
    repetir_palavra()
  
