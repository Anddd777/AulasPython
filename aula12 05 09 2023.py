# Funções v. 2

from datetime import datetime
datetime.today().year


print("""
Para imprimir digite -> 1
Para salvar digite -> 2
Para sair digite -> 3

""")

#def mensagem(resposta):
#    if resposta=="1":
#        print("Você pediu para Imprimir")
#    elif resposta=="2":
#        print("Você pediu para Salvar")
#    elif resposta=="3":
#        print("Você pediu para Sair")
#    else:
#    print("digite um valor valido")



#while True:
#    print("""
#    Para imprimir digite -> 1
#    Para salvar digite -> 2
#    Para sair digite -> 3
#   """)
#    resposta = input("Qual opção deseja: ")
#    mensagem(resposta)
#    if resposta=="3":
#        break


#mensagem("Sei la essa é a primeira mensagem")
#mensagem("Sei la essa é a segunda mensagem")
#mensagem("Sei la essa é a terceira mensagem")


#Funções Nomeadas e posicionais


def pessoa(nome, idade, rg):
    nome=nome.strip()
    idade=idade.strip()
    rg=rg.strip()

    if len(nome)!=0 and nome.isalpha():
        if idade.isdigit() and len(idade)<3:
            if int(idade)<=120:
                if len(rg)>=9 and len(rg)<11:

                    return {"nome": nome, "idade": idade, "rg": rg}

            else:
                print("A idade deve ser menor do que 120 anos")
        else:
            print("O valor da idade deve ser Numerico")
    else:
        print("Nome digitado não é válido:")


print("Cadastro de Pessoa".center(30,"#"))

x=0
pessoas=list()
while True:
    nome=input("Digite o seu nome: ")
    idade=input("Digite a sua idade: ")
    rg=input("Digite o seu rg: ")
    if isinstance(pessoa(nome,idade,rg),dict):
        pessoas.append(pessoa(nome,idade,rg))
    #print(pessoa(nome,idade,rg))
    x+=1
    if x==2:
        break

print(pessoas)


#f __name__ =="__main__":

#Função args kargs

# vou entrar com a possibilidade de varios parametros, e nao quero limitar minha funcao com uma quantidade
# de parametros
#new*
#def calculadora(*args):
#    for parametro in args:
#        print(parametro)

#calculadora("Primeiro Argumento",34,[1,2,3,4])