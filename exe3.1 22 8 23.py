
# Criar uma aplicação que pega o nome e a idade do aluno
# verificando se a idade é realmente um int,
# verificar se o nome  é um str
# Faça um loop que force o aluno a capacidade de cadastrar 4 notas e verificar se a notas são do tipo float
# e se for float converter elas para esse tipo, depois faça a média delas
# se a media for maior que 8 ele sai do loop e manda a msg "VOCÊ FOI APROVADO!"

nome = input("Digite o seu nome: ") # Alpha
idade = input("Digite a sua idade: ") # Digito

# se o nome for diferente de "alpha" e a idade diferente de "digital", vai dar uma resposta "falsa"
# sendo assim eu nego a resposta "falsa" e converto ela para verdadeira "True" colocando no começo o "not"
# Olhar na planilha de AND

while not (nome.isalpha() and idade.isdigit()):
    print("Você digitou o nome ou a idade errado")
    nome = input("Digite o seu nome: ")
    idade = input("Digite a sua idade: ")


# vou criar um loop que vai ficar verificando ate ele digitar as notas corretamente
while True:

    # bandeira é uma variável temporária local
    b1 = False
    b2 = False
    b3 = False
    b4 = False

    # nota 1
    nota1 = input("Digite a primeira nota: ")    # pegando a primeira nota
    # 1) Testar se a nota1 tem um caracter do tipo "." ou "," SE TIVER VAMOS REMOVER USANDO O REPLACE
    # 2) vamos verificar se o que restou é um digito

         if str.isdigit(nota1.replace(".", "")) or str.isdigit(nota1.replace(".", "")):

        # 3) se ela tiver "," eu retiro a virgula e coloco um "." no lugar usando o replace
        # 4) vou pegar o valor que é uma String e converter ele para um float
                nota1 = float(nota1.replace(",","."))

        # se tudo deu certo eu converto minha bandeira para verdadeiro
        b1 = True
    else:
        # se tudo deu certo eu converto minha bandeira para falsa
        b1 = False

    # nota 2
        nota2 = input("Digite a segunda nota: ")
        if str.isdigit(nota2.replace(".", "")) or str.isdigit(nota2.replace(".", "")):
        nota2 = float(nota2.replace(",", "."))
        b2 = True
    else:

        b2 = False

    # nota 3
    nota3 = input("Digite a terceira nota: ")

        if str.isdigit(nota3.replace(".", "")) or str.isdigit(nota3.replace(".", "")):

    nota1 = float(nota3.replace(",", "."))

        b3 = True
    else:

        b3 = False


    # nota 4
    nota4 = input("Digite a quarta nota: ")

    if str.isdigit(nota4.replace(".", "")) or str.isdigit(nota4.replace(".", "")):

        nota4 = float(nota4.replace(",", "."))

        b4 = True
    else:

        b4 = False

    if b1 and b2 and b3 and b4:
        media = (nota1 + nota2 + nota3 + nota4)/4
        print(media)
        break

p














