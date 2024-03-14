numero1 = int(input("Qual o valor do primeiro lado do tringulo:") )
numero2 = int(input("Qual o valor do segundo lado do tringulo:") )
numero3 = int(input("Qual o valor do terceiro lado do tringulo:") )

if numero1 == numero2 == numero3:
    print("Triângulo equilátero")

elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
    print("Triâgulo isósceles")

else:
    print("Triâgulo escaleno")