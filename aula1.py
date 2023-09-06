#Aula 1 Variaveis
# nome

nome = "Andrea" # String
sobrenome = 'Novaes' # String
nomecompleto = nome+"/"+sobrenome
peso = 70.800  # float real
idade = 45  # int inteiro
rg = "XX.XXX.XXX-X"
cpf = "XXX.XXX.XXX-XX"

# FORMATAR
# o type é uma função que mostra o tipo do valor
print("nomecompleto: ", nomecompleto, "\nrg: ", rg, "\ncpf", cpf) # é para saída de dados, mandar dados para o terminal
print("="*30) # ele está multiplicando a quantidade de vezes que vai aparecer o =
print(f"nome: {nome} \nsobrenome: {sobrenome} \nidade: {idade}")

# Pegar valores do teclado
#rg = input("Digite o seu RG: ")
# todo valor do input vem como String

#idade=input("Digite sua idade: ")
#print(type(idade))

#valor = str(12)
#nota1 = float(input("Digite a primeira nota: "))
#nota2 = float(input("Digite a segunda nota: "))
#nota3 = float(input("Digite a terceira nota: "))
#nota4 = float(input("Digite a quarta nota: "))

#Operadores Math
# + soma
# - subtração
# / divisão
# // divisão inteira
# % modulo   (entrega o resto)
# * multiplicação

#print((nota1+nota2+nota3+nota4)/4)

#Pegar o (nome) (RG) (CPF) pelo teclado
#Imprimir na tela esses dados formatados

nome=input("Digite o seu nome: ")
rg=input("Digite o seu RG: ")
cpf=input("Digite o seu CPF: ")

print(f"nome: {nome}  \nrg: {rg}  \ncpf: {cpf}")
