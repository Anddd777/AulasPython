#Strings

#vetor
texto="Andrea" # é um objeto -Atributos e -metodos

#index   0 1 2 3 4 5 6

# input | converter/processar | output
print(texto.upper())
texto= texto.upper()
print(texto)
print(texto.lower())

#texto=input("Digite o seu nome completo: ")
texto=texto.lower()
print(texto.title())
print("#"¨*30)

texto="  andrea novaes  "
print(texto.strip())

resposta=input("Deseja mostrar no sistema sim ou não").strip()[0].upper()

if resposta=="S":
    print("entrou")

print(texto.count( "a"))
print(texto.strip().index("n"))
lista=texto.split(" ") # fatia por / ou letra 'a'
print(lista)