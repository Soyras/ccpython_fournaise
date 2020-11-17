import os

sauver = open("messagePourSauverLeMonde.txt", "r")

# Affiche une message une fois le mot trouvé
for line in sauver:
    if 'volcan' in line:
        print ("A l'aide, tous aux abris!")
sauver.close()

# Affiche une message une fois le mot trouvé
nature = open("livreDeLaNatureEtDesLacs.txt", "r")
for ligne in nature:
    if 'arbre' in ligne:
        print(f"Nous pouvons nous abriter à {ligne} pas d'ici, dans cet arbre suspendu!")
nature.close()