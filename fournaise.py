import os

sauver = open("messagePourSauverLeMonde.txt", "r")

# Affiche une message une fois le mot trouvé, le volcan se met en éruption !
for line in sauver:
    if 'volcan' in line:
        print ("A l'aide, tous aux abris!")
sauver.close()

print()

# Affiche une message une fois le mot trouvé, chercher un abri !
nature = open("livreDeLaNatureEtDesLacs.txt", "r")
compteur = 0
for ligne in nature:
    if 'arbre suspendu' in ligne:
        print(f"Nous pouvons nous abriter à {compteur} pas d'ici, dans cet arbre suspendu!\nOh, le GPS vient de s'activer.\n")
    # Compte la position de la ligne
    compteur += 1
nature.close()

# Compte du nombre de pas pour se sauver
projectile = open("desProjectilesEtDesDodos.txt", "r")
# Initialisation des pas
pas_total = 0
pas_gauche = 0
pas_droite = 0
pas_avant = 0

print('Ahhh! Des projectiles, partons chercher un autre repère!\n')

for ligne in projectile:
    if 'rocher' in ligne:
        pas_gauche += 5
        pas_total += 5
    if 'arbre' in ligne:
        pas_avant += 10
        pas_total += 10
    if 'dodo' in ligne:
        pas_droite += 6
        pas_total += 6
    
    if pas_total >= 100:
        if 'lac' in ligne:
            print("Ok, on a fait", pas_total, " pas en tout et on a trouvé le lac.")
            if pas_gauche > pas_droite and pas_gauche > pas_avant:
                print('On a surtout marcher vers la gauche.')
            elif pas_droite > pas_gauche and pas_droite > pas_avant:
                print('On a surtout marcher vers la gauche.')
            else:
                print("On a surtout marcher vers l'avant.\n")
            break
projectile.close()


# Organiser la famille dodo
dodo = open('lafamilleDodo.txt', "r")
x = dodo.readline()
nombre = x.split(", ")
famille = []

for i in range (len(nombre)):
    a = int(nombre[i])
    famille.append(a)
    #print(nombre[i])

famille.sort()
print(len(famille))

x = 6

# Enlève les doublons de la liste
for i in range(len(famille)-x):
    if famille[i] == famille[i+1]:
        del famille[i]
        x -= 1

#print(famille)
dodo.close()

# Tri les dodos mineurs et les majeurs
age = open('ageDodo.txt', "r")
x = age.readline()
separate = x.split(', ')

majeur = 0
mineur = 0

print(separate)
age_list = []
for i in range (len(separate)):
    a = int(separate[i])
    age_list.append(a)

print(age_list)

for i in range(len(age_list)):
    if age_list[i] < 5:
        mineur += 1
    else:
        majeur += 1
    
print(f'Il y a {mineur} dodos mineurs.\nIl y a {majeur} dodos majeurs.')








