# APLICAÇÃO
# USUÁRIO
# Criar um sistema que salve os dados de um usuário:
# Nome: str()
# RG: str()
# Telefones: list()
# Data_nasc: str()

# Vamos tb salvar despesas:
# Descrição
# Valor

# Criar uma lista com vários usuários



#Sistema de controle

# Primeira Versão
"""
usuarios=(list)
while True:

    #Pegando os dados do usuario
    nome=input("Digite o seu nome: ")
    rg=input("Digite o seu rg: ")
    ano_nasc=input("Digite o ano em que nasceu: ")

    tel1=input("Digite o seu primeiro telefone: ")
    tel2=input("Digite o seu segundo telefone: ")

    telefones = list() #criando uma lista e telefones desse usuario
    telefones.append(tel1) # add o tel1 dentro da lsita de telefones
    telefones.append(tel2) # add o tel2 dentro da lsita de telefones

    # vou começar a cadastrar uma despesa
    print("Cadastrando a despesa")
    # pegando os dados da despesa
    descricao=input("Descricao da Despesa: ")
    valor=float(input("Valor da Despesa: "))

    # criando um dicionario de um usuario
    dicionario={"nome":nome,"rg":rg,"ano":ano_nasc,"telefones":telefones,
            "despesas":{"descricao":descricao, "valor":valor}}


    usuarios.append(dicionario)

    resposta=input("Deseja continuar sim ou não").strip()[0].lower()
    if resposta=="n":
        break

print(usuarios)



#ESTUDAR



#dicionario2={"nome":nome,"rg":rg,"ano":ano_nasc,"telefones":["1145454545","1145454545"]}

#print(dicionario2)

"""
#Versão 2

import datetime as dt

usuarios=list()
print("Seja Bem Vindo!")
while True:
    print("#"*20,"Menu", "#"*20)
    print("""
    Para Cadastrar digite -> 1
    Para Sair digite -> 2
    Para listar usuarios -> 3
    """)
    btn = input("Digite a opção desejada: ")

    #cadastrar usuario
    if btn=="1":
        print("#" * 20, "Cadastro de Usuario", "#" * 20)
        nome: str = input("Nome: ")
        rg: str = input("RG: ")
        ano_nasc: str =input("Ano Nascimento: ")
        # tratar o ano de nascimento

        print("#" * 20, "Cadastro de Telefone", "#" * 20)
        tel1: str = input("Digite o seu telefone 1: ")
        tel2: str = input("Digite o seu telefone 2: ")
        telefones=[tel1,tel2] #add telefones

        print("#" * 20, "Cadastro de Despesas", "#" * 20)
        #Despesas
        despesas=list()
        while True:
            descricao:str=input("Descricao da despesa: ")
            valor=input("digite o valor: R$ ")
            # tratar o valor de entrada
            data_despesa=dt.date.today() # estou lançando a data da despesa como se fosse hoje
            despesa={"descricao":descricao, "valor":valor, "data_despesa":data_despesa}
            despesas.append(despesa)
            resposta=input("Deseja continuar cadastrando despesas Sim ou Não:").strip()[0].upper()
            #validar a resposta
            if resposta=="N":
                break

        #dicionario
        usuario={"nome":nome, "rg":rg, "ano_nasc":ano_nasc, "telefones":telefones, "despesas":despesas}
        usuarios.append(usuario)

    elif btn=="2":
        break

    elif btn=="3":
        if len(usuarios)<=0:
            print("Não tem nenhum usuario cadastrado")
        else:
            print("#" * 20, "Lista de Usuarios", "#" * 20)
            for usuario in usuarios:
                print("#" * 20, "Usuario", "#" * 20)
                print(f' Nome: {usuario["nome"]}')
                print(f' RG: {usuario["rg"]}')
                print(f' Idade: {dt.date.today().year - int(usuario["ano_nasc"])}')
                print("#" * 20, "Data de Contato", "#" * 20)
                print(f' Tel 1: {usuario ["telefones"] [0]} | Tel 1: {usuario["telefones"] [1]} ')
                print("#" * 20, "Despesas", "#" * 20)
                for despesa in usuario["despesas"]:
                    for key, value in despesa.items():

                        if key!="valor":
                            print(f'{key.upper()} = {value}')
                        else:
                            print(f'{key.upper()} = R$ {float(value)}')
                            print("*"*30)