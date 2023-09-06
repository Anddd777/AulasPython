# Criar um sistema que vai pegar o nome e a idade e só vai parar de pedir para cadastrar quando for maior de 18


while True:

    nome = input("Digite o seu nome: ")
    idade = input("Digite a sua idade: ")

    if idade>18:

        break

print("Acabou o sistema!")


