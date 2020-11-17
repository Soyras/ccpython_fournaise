import os

fichier = open("messagePourSauverLeMonde.txt", "r")
for mot in fichier:
    if 'volcan' in mot:
        print ("A l'aide, tous aux abris!")
