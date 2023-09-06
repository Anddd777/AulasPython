# VAMOS PRATICAR - PRIMEIRA PARTE
# Vamos criar um programa de cadastro de usuários
# Vamos cadastrar: Nome | RG | CPF | Ano_nasc
# O nosso sistema vai estar dentro de um loop
# Cadastrando vários usuários
# Só vamos sair do cadastro quando estivermos prontos

print("#"*30)

print("Seja Bem Vindo ao Sistema!")
print("Você precisa logar para entrar no sistema:")
nome:str=  input("Digite seu nome: ")
senha:str = input("Senha: ")

clientes=list()

# validando a entrada no sistema

if nome in  ["pedro", "maria", "santos", "josé"] and senha =="1234"

      while True: # vou fazer um loop para poder ficar cadastrando pessoas
        print("Tela Cadastrando Cliente")

        nome: str = input("Digite seu nome: ")
        RG: str = input("Digite seu RG: ")
        CPF: str = input("Digite seu CPF: ")
        Ano_nasc: int = int(input("Digite o seu Ano de Nascimento: "))

        cliente=list()
        cliente.append(nome)
        cliente.append(RG)
        cliente.append(CPF)
        cliente.append(Ano_nasc)

        cliente=[nome,RG,CPF,Ano_nasc]

        clientes.append(cliente)

        resposta=input("Deseja continuar cadastrando").strip()[0].upper()
        if resposta=="S":
            break


else:
    print("Nome ou senha não existe no sistema")

print(clientes)

#listas=[
#        ["Pedro", ""]


