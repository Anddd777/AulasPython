#Criar um sistema que salva login e senha.
#O Login não pode ser repetido
#A senha pode ser repetida
#O login deve estar associado a senha
# trabalhar com listas e set apenas para validação #

#print("#"*30)

#print("Você precisa logar para entrar no sistema:")
#login: str =  input("Digite o seu login: ")
#senha: str = input("Digite a sua senha: ")

#clientes = list()

#if nome in  ["pedro", "maria", "santos", "josé"] and senha =="1234"
 #     while True:

 #       nome: str = input("Digite o seu login: ")
 #       senha: str = input("Digite a sua senha: ")

  #      cliente=list()
  #      cliente.append(login)
  #      cliente.append(senha)

  #      cliente=[login,senha]

  #      clientes.append(cliente)

   #     resposta=input("Deseja continuar cadastrando").strip()[0].upper()
   #     if resposta=="S":
   #         break


#print(clientes)

#else:
   # print(" ")

#print(clientes)



# SEGUNDA VERSÃO

print("#"*30)

loguinhos = set()

usuarios = list()


while True:
    print("Cadastrando Usuário")
    login = input("Cadastre o seu login: ")
    senha = input("Cadastre a sua senha: ")
    usuario =[login,senha] # para ele ser cadastrado na minha lista de usuarios vou primeiro validar

    # validando o login

    if len(usuarios)!=0:
        #verificando todos existentes
        for user in usuarios: # gerar uma variavel local (user)
            # estou pegando cada (usuario) que tem cadastrado na minha lista (Usuarios)
            loguinhos.add(user[0])
        tamanho=len(loguinhos) # verifico o tamanho do meu login

        #tentando add mais um login (dentro dele)
        loguinhos.add(login)

        if len(loguinhos)==tamanho:
            print("Login já existe no sistema")
    else:
        usuarios.append(usuario)

    else:
    # vai entrar caso seja o primeiro usuario a ser cadastrado
         usuarios.append(usuario)


# Sair do loop
    resposta=input("Deseja continuar cadastrando: Sim ou Não").strip()[0].upper()

    if resposta=="N":
        print("Saindo do Sistema")
        break


# entre no sistema com os logins cadastrados e as senhas lembrando que eles tem vínculo
# caso ele entre, mande a msg "Você esta dentro do sistema"