def calcular_media_5_notas():
    notas = []
    for i in range(1, 6):
        while True:
            entrada = input(f"Digite a nota {i} (0 a 10): ").replace(",", ".")
            try:
                nota = float(entrada)
                if 0.0 <= nota <= 10.0:
                    notas.append(nota)
                    break
                else:
                    print("Nota fora do intervalo. Digite um valor entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Digite um número (ex: 7.5).")
    media = sum(notas) / len(notas)
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")

if __name__ == "__main__":
    calcular_media_5_notas() 
