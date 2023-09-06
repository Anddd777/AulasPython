# Criar uma lista que vai conter o nome do cliente
# Criar uma lista interna que vai ter o contato (tel, email)
# Criar uma lista interna que tenha 3 notas do cliente
# 1) Imprima o nome do cliente
# 2) Imprima somente o telefone do cliente
# 3) Imprima a soma das notas (SUM)
# 4) Imprima a contagem do número das notas (LEN)
# 5) Imprima a média das notas do cliente junto com o seu nome

#cliente1 = ["Carlos", ["(11) 9123-45678", "carlo@gmail"], [10, 8, 7]]

#print("Nome:", cliente1[0])
#print("Telefone:", cliente1[1][0])
#print("Soma das notas:", sum(cliente1[2]))
#print("Total de notas:", len(cliente1))
#print("Média:", sum(cliente1[2])/ len(cliente1[2]))

cliente = ["Carlos",["(11) 94545-4545", "meuemail@gmail.com"],[4,5,7,9]]

print(cliente[0]) # pegando o nome
print(cliente[1][0]) # pegando o telefone
print(sum(cliente[2]) # pegando e somar
print(len(cliente[2])) # contar os elementos
print(f"Nome:{} Média: {sum(cliente[2]/len(cliente[2])}")