# Criar um sistema que cadastra receitas financeiras
# descricao
# valor (validar o valor)
# data
# classes
# categoria
# salvar como um dicionario cada receita
# salvar dentro de uma lista de receitas
# mostrar na tela

new
 def verificarValor(valor)
      valor=valor.strip()
      if valor.isdigit() or str.isdigit(Valor.replace(".","")) or str.isdigit(valor.replace(",","" )):
          valor=valor.replace)(",",".")
          return float(valor)



new
def receita(descricao, valor, data, categoria):
    descricao=descricao.strip()
   # valor=valor.strip()
    data=data.strip()
    categoria=categoria.strip()
    # eu vou criar uma função para validar meu valor
    if isinstance(_verificarValor(valor), float)
        return {"descricao":descricao, "data":data, "categoria":categoria, "valor":verificarValor(valor)}
    else:
        Print("Não foi possível cadastrar")

while True:
    descricao = input("Digite a descricao da receita: ")
    valor = input("Digite o valor da receita: ")
    data = datetime.today()
    categoria = input("Digite a categoria da receita: ")
    if isinstance(receita(descricao,valor,data,categoria),dict):
        receitas.append(produto(descricao,valor,data,categoria))
    else:
        print("Não foi possivel cadastrar")

    resp=input("Deseja sair sim ou não").strip()[0].upper()

    if resp=="S":
        break

# vamos imprimir as receitas de modo organizado

print(receitas)


#  if quantidade.isdigit():
#      return {}
# else:
#    print("O valor da quantidade não é válido")

