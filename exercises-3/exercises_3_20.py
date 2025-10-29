def verificar_sinal():
    num = float(input("Digite um número: ").replace(",", "."))
    if num > 0:
        print("O número é positivo.")
    elif num < 0:
        print("O número é negativo.")
    else:
        print("O número é zero.")

if __name__ == "__main__":
    verificar_sinal()
  
