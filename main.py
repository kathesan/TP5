def calcul(x):
  nb=''
  for y in range(1, 11):
    nb += str(y) + '*' + str(x) + '=' + str(x*y) + '|'
  return nb


fichier = open("fichier.txt", "w")

for i in range (2, 31):

    fichier.write(calcul(i) + '\n')

fichier.close()