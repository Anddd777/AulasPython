#Trabalhando com Listas 2
#Pegando data do sistema
#Importar uma lib
import datetime as dt
anoAtual=datetime as dt

anoAtual= dt.date.today().year

print(f"Data: {anoAtual}")




#vamos colocar todas com letras maiusculas

#nome="rogerio"
#nome="pedro"


#Inserindo valores na lista
listaTeste=["rua","tel"] # aqui eu estou iniciando a minha lista com 2 valores
print(listaTeste[0])
listaTeste["0"]="Pedro" # estou atualizando a minha lista com um novo valor
print(listaTeste[0])

print("#"*30)
# vamos colocar todas com letra maiusculas
lista = ["rogerio","pedro","maria","joão"]
print(lista)
for index in range(len(lista)):
# pos 0 = pos 0 transforma em title
    lista[i] = lista[i].title()

print(lista)



#outra maneira de girar lista
print("#"*30)
novaLista=list()
novaLista2=[]
print(type(novaLista))

#Add valores dentro de minha lista
novaLista.append("Rogério")
novaLista.append("Carlos")
novaLista.append(1)
novaLista.append(34.56)
print(novaLista)



#maneira diferente de criar lista
novaLista2=[]
novaLista2.append("T")
novaLista2.append("D")
novaLista2.append("A")
novaLista2.append("B")
novaLista2.append("A")
print(novaLista2)
#CONT() vai contar a ocorrencia do parametro
print(#Quantidade de A :", novaLista2.count("A")) # ele retorna a quantidade
novaLista2.remove("D") # ele remove o valor e atualiza a lista
print(novaLista2)

novaLista2.append("a")
novaLista2.sort() # organiza e não retorna nada, atualiza a lista
print(novaLista2)



