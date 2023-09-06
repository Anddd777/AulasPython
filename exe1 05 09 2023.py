# Criar uma função que cadastre uma lista de produtos, onde cada produto vai ter:
# Tipo
# Descrição
# Quantidade
# Você deve validar o campo quantidade para ser um int

("""   
def produto(tipo, descricao, quantidade):
    tipo = tipo.strip()
    descricao = descricao.strip()
    quantidade = quantidade.strip()

    if len(tipo)!=0 and tipo.isalpha():
        if descricao.isdigit():
            if len(quantidade)>=1:

                    return {"tipo": tipo, "descricao": descricao, "quantidade": quantidade}

            else:
                print("Quantidade invalida")
        else:
            print("Descricao incorreta")
    else:
        print("O valor da quantidade deve ser int")


print("Cadastro de Produtos".center(30,"#"))

x=0
produtos=list()
while True:
    tipo=input("Digite o tipo: ")
    descricao=input("Digite a descricao: ")
    quantidade=input("Digite a quantidade: ")
    if isinstance(produto(tipo,descricao,quantidade),dict):
        produtos.append(produto(tipo,descricao,quantidade))
    #print(produtos(tipo,descricao,quantidade))
    x+=1
    if x==2:
        break

print(produtos)

""")


def produto(tipo, descricao, quantidade):
    tipo = tipo.strip()
    descricao = descricao.strip()
    quantidade = quantidade.strip()
    if quantidade.isdigit():
        return {"descricao":descricao, "tipo":tipo, "quantidade":int(quantidade)}
    else:
        print("O valor da quantidade não é valido")

produtos=list()

while True:
    descricao=input("Digite a descricao do produto: ")
    tipo=input("Digite o tipo do produto: ")
    quantidad=input("Digite a descricao do produto: ")
    if isinstance((produto(descricao=descricao, tipo=tipo, quantidade=quantidade),dict):
         produtos.append(produto(descricao=descricao, tipo=tipo, quantidade=quantidade))
    else:
        print("Não foi possivel cadastrar")

    resp=input("Deseja sair sim ou não").strip()[0].upper()

    if resp=="S":
        break

print(produtos)



