def comparar_numeros():
    a = float(input("Digite o primeiro número: ").replace(",", "."))
    b = float(input("Digite o segundo número: ").replace(",", "."))
    if a > b:
        print(f"{a} é maior que {b}")
    elif b > a:
        print(f"{b} é maior que {a}")
    else:
        print("Os dois números são iguais")

if __name__ == "__main__":
    comparar_numeros()
  
