def fibonacci(n):
    sequencia = [1, 1]
    while len(sequencia) < n:
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)
    return sequencia

print("=== 🔢 SEQUÊNCIA DE FIBONACCI ===")
quantidade = 10
resultado = fibonacci(quantidade)
print(f"Os {quantidade} primeiros números da sequência Fibonacci são:")
print(resultado)
