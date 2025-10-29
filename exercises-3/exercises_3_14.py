def contar_ate_usuario():
    while True:
        entrada = input("Digite um número inteiro >= 1 para contar até ele: ")
        try:
            limite = int(entrada)
            if limite >= 1:
                break
            else:
                print("Digite um número maior ou igual a 1.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
    n = 1
    while n <= limite:
        print(n)
        n += 1

if __name__ == "__main__":
    contar_ate_usuario()
  #Tive que pesquisar para conseguir fazer da maneira certa e achei bastante interessante a questao do except, entrada invalida.
