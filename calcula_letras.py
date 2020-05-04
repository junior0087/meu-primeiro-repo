
# programa que diz quantas letras tem seu nome

nome = input('insira seu nome: ')
nome = nome.lower()
tamanho = len(nome)

print('o seu nome tem ', tamanho, 'caracteres.')

lista = list(nome)
nvogais = lista.count('a') + lista.count('e') + lista.count('i') + lista.count('o') + lista.count('u')
print('O seu nome tem ', nvogais, 'vogais')
