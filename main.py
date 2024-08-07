# lista de numeros aleatórios

numeros = [10, 5, 7, 4, 6, 3, 8]

# classifica em ordem descrescente
numeros.sort(reverse=True)

for numero in numeros:
    print(numero, end='. \n')
soma = sum(numeros)
print(f'A soma da lista é: {soma}.')

media = sum(numeros)/len(numeros)
print(f'\nResultado da média da lista: {media:,.2f}')



