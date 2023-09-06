# Criar uma aplicação que pega o nome e a idade do aluno
# Faça um loop que force o aluno a cadastrar 4 notas e fazer a media delas
# se a media for maior que 8 ele sai do loop e manda a msg "VOCÊ FOI APROVADO!"



nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

while True:

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))
    media = (nota1 + nota2 + nota3 + nota4)/4
    print(media)
    if media >= 8:

        break

print("Aprovado!")


if media>=8:
    print("Você foi Aprovado!!!")




