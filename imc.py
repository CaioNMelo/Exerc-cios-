peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: Ex: 1.70"))

imc = peso / (altura ** 2)

print("Seu IMC é:", imc)

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 35:
    print("Obesidade grau 1")
elif 35 <= imc < 40:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")



