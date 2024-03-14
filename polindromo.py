palavra = input("Digite uma palavra: ")

def verifica_palindromo(palavra):
    palavra = palavra.lower()  
    palavra = palavra.replace(" ", "")  
    inverso = palavra[::-1] 

    if palavra == inverso:
        return True
    else:
        return False

if verifica_palindromo(palavra):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
