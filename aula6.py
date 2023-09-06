x=3
# Quando eu tiver duas opções de valores que depende de uma condição
# Posso usar o operador ternario

media = 6.7
nome = "Aprovado" if media >=8 else "Reprovado"
print(nome)

print("#"¨*30)


nome1="Carlos"
idade1=45
nota1_aluno_1=7
nota2_aluno_1=6
nota3_aluno_1=8
media_a1=(nota1_aluno_1+nota2_aluno_1+nota3_aluno_1)/3
#Aluno2
nome2="Carlos"
idade2=45
nota1_aluno_2=9
nota2_aluno_2=9
nota3_aluno_2=7.9
media_a1=(nota1_aluno_2+nota2_aluno_2+nota3_aluno_2)/3
print(f"Aluno {nome1} tirou a média de: {média_a1}")
print(f"Aluno {nome2} tirou a média de: {média_a2}")

# Estudos de Listas
# Primeira versão
# index   0   1   2   3   4
#aluno1=["Carlos",45,7.7,6.5,8]
#print("Nome: ",aluno1[0])
#print("Idade: ",aluno1[1])
#print("Nota1: ",aluno1[2])
#print("Nota2: ",aluno1[3])
#print("Nota2: ",aluno1[4])

# quero somente usar as notas
#media=(aluno1[2]+aluno1[3]+aluno1[4]])/3
#print(f"Nome {aluno1[0]} tirou a media {media}")

# Métodos de uma lista

#print(len(aluno1))
#numeros=[3,5,67,100.89,67,100,45]
##sum(jogar a lista, apenas de números, aqui dentro) é a função que soma todos os valores dentro de uma lista
#print(sum(numeros)/len(numeros))

# Segunda versão
# estou criando uma lista so para notas e essa lista esta dentro da principal
# index lista interna   0   1   2
aluno1=["Carlos",45,[7.7,6.5,8]]
# index lista interna   0   1   2
print(Média: ",sum(aluno1[2])/len(aluno1[2])

# digamos que eu quero pegar um valor da nota sendo ela a primeira
print(aluno1[2][1])