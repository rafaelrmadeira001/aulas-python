produto = 'Livro'
preco = 35.50
desconto = 0.10
preco_com_desconto = preco * (1 - desconto)
print(f'O {produto} custa R${preco:.2f} e, com {int(desconto * 100)}% de desconto fica por R${preco_com_desconto:.2f}.')
