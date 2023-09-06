altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))
imc =(altura**2)/peso

if imc <= 18.5:
    print("Abaixo do peso")

elif imc >= 18.6 and imc <= 24.9:
    print("Peso ideal")

elif imc >= 25.0 and imc <= 29.9:
    print("Levemente  acima do peso")

elif imc >= 30.0 and imc <= 34.9:
    print("Obesidade grau I")

elif imc >= 35.0 and imc <= 39.9:
    print("Obesidade grau II")

elif imc >= 40:
    print("Obesidade grau III")


