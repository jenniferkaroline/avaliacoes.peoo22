def removeDuplicada(lista):
  listanew = []
  num = lista[0]
  listanew.append(num)

  for i in lista:
    if i == num:
      continue
    else:
      num = i
      listanew.append(num)
      
  return listanew

L = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4]
novaL = removeDuplicada(L)
print(novaL)

def checkVitoria(lista):
  resultado = ' '
  if lista[0] and lista[1] and lista[2] == "X":
    resultado = 'jogador1'
  elif lista[0] and lista[1] and lista[2] == "O":
    resultado = 'jogador2'
  else:
    resultado = 'nada'
  return resultado

L = ['X', 'X', 'X']
resultado = checkVitoria(L)
print(resultado)
