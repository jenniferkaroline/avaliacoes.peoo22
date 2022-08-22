def contagemPalavras(texto):
    contC = 0
    contBlank = 0
    for caracter in texto:
        contC = contC + 1
        if caracter == ' ':
            contBlank = contBlank + 1
    print('Caracteres: ', contC)
    print('Caracteres sem espaços: ', contC-contBlank)
    print('Palavras: ', contBlank + 1)
  

def inverter(lista):
    novaLista = []
    for elemento in lista:
        novaLista.insert(0, elemento)

texto = input()
x = contagemPalavras(texto)   
print(x)

lista = [1, 2, 3, 4, 5]
z = inverter(lista)
print(z)

