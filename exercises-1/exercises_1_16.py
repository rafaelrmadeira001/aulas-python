print('Olá, digite as notas das diciplinas: ')
nota_1 = float(input('Redação de texto: '))
nota_2 = float(input('Gramatica '))
nota_3 = float(input('Interpretação de texo: '))
nota_total = ((nota_1 + nota_2 + nota_3) / 3)
print(f'A média è: {nota_total:.2f}.')

