palavra = input("Digite uma palavra:")

def contar_vogais_consoantes(palavra):
    vogais = "aeiouAEIOU"
    contador_vogais = 0
    contador_consoantes = 0

    for letra in palavra:
        if letra in vogais:
            contador_vogais += 1
        else:
            contador_consoantes += 1

    return contador_vogais, contador_consoantes

num_vogais, num_consoantes = contar_vogais_consoantes(palavra)

print("Vogais:", num_vogais)
print("Consoantes:", num_consoantes)


