# Set
# não aceita repetição
# ele organiza os dados de uma maneira que faça ficar rapido a busca

lista=[1,2,3,4,2,3]
tupla=(1,2,3,4,2,3)
dicionario={"um":1,"dois":2,"tres":3}
conjunto={2,2,3,4,2,3,2,3,4,3}

print(f"Lista: {lista[0]}")
print(f"Lista: {tupla[0]}")
print(f'Dicionario: {dicionario["dois"]}')
print(f"conjunto: {conjunto}")

tamanho=len(conjunto)

conjunto.add(4)
if len(conjunto)==tamanho:
    print("Login ja existe!")

print("#"*30)
# Criar um sistema que não permita repetição do login
lognhos={"admin", "maria_2022"} # ele já começa com um tamanho 1
print("#"*25, "Tela de Login", "#"*25)

while True:
    login=input("Cadastre o seu login: ")
    tamanho=len(lognhos)
    lognhos.add(login)
    if len(lognhos)!=tamanho:
        break
    else:
        print("Esse Login ja existe: ")

print(f"Login:{lognhos}")

print("#"*30)

conjunto2={23,45,67,80,80}

for valor in conjunto2:
    print(valor)

#Criar um sistema que salva login e senha.
#O Login não pode ser repetido
#A senha pode ser repetida
#O login deve estar associado a senha
# trabalhar com listas e set apenas para validação #