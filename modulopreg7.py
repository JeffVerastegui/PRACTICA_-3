import random

def generar_numeros_aleatorios(cantidad, min_valor, max_valor):
    numeros = [random.randint(min_valor, max_valor) for _ in range(cantidad)]
    return numeros

numeros_aleatorios = generar_numeros_aleatorios(20, 0, 100)

print("Lista original de números aleatorios:")
print(numeros_aleatorios)

numeros_aleatorios.sort()

print("\nLista ordenada de números aleatorios:")
print(numeros_aleatorios)
