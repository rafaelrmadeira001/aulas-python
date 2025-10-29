def tabuleiro_jogo_da_velha():
    tamanho = 3  
    print("=== TABULEIRO 3x3 ===")
    
    for linha in range(tamanho):
        for coluna in range(tamanho): 
            if coluna < tamanho - 1:
                print(" _ |", end="")
            else:
                print(" _ ") 
    print("\nTabuleiro criado com sucesso!")

if __name__ == "__main__":
    tabuleiro_jogo_da_velha()
