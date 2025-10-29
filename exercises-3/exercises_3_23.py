import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    tentativas = 0

    print("=== JOGO DE ADIVINHAÇÃO ===")
    print("Tente adivinhar o número que estou pensando (entre 1 e 10)!\n")

    while True:
        palpite = input("Seu palpite: ")

        if not palpite.isdigit():
            print("❌ Por favor, digite um número inteiro entre 1 e 10.")
            continue

        palpite = int(palpite)
        tentativas += 1

        if palpite < 1 or palpite > 10:
            print("⚠️ O número deve estar entre 1 e 10.")
        elif palpite < numero_secreto:
            print("🔼 Tente um número maior!")
        elif palpite > numero_secreto:
            print("🔽 Tente um número menor!")
        else:
            print(f"🎉 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")
            break

if __name__ == "__main__":
    jogo_adivinhacao()
    
