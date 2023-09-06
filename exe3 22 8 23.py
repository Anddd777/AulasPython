# Criar uma aplicação que pega o nome e a idade do aluno verificando se a idade é realmente um int, verificar se o nome
# é um str
# Faça um loop que force o aluno a capacidade de cadastrar 4 notas e verificar se a notas são do tipo float
# e se for float converter elas para esse tipo, depois faça a média delas
# se a media for maior que 8 ele sai do loop e manda a msg "VOCÊ FOI APROVADO!"

# Trabalhando a validação

n = "12"
print(n.isdigit())

idade = input("Digite a sua idade: ")

# valores inteiros

# print(idade.isdigit())

# print(idade.isnumeric())

#verificar se é uma letra
#nome = input("Digite o seu nome: ")
#print(nome.isalpha())

#Alpha Numeric
#numero_Letra="23a45AÇ"
#print(numero_Letra.isalnum())

#para trocar o valor de um caracter eu posso usar o metodo replace([vai procurar o valor que deseja mudar],
#[qual valor que colocar no local
decimal="12.45"
if str.isdigit(decimal.replace(".","")):
    decimal=float(decimal)
    print(type(decimal))
else:
    print(type(decimal))
