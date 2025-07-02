from correction import exos_c
###############################
#                             #
#          Les boucles        #
#                             #
###############################

# Les boucles permettent de répéter une série d’instructions plusieurs fois sans avoir à les réécrire.

# Il existe deux types principaux de boucles en Python :
# - la boucle 'for' (pour un nombre défini d'itérations)
# - la boucle 'while' (tant qu’une condition est vraie)

#===========================================
# La boucle 'for'

# Elle sert à parcourir des éléments d’une liste, une chaîne de caractères, ou toute autre collection.

# Exemple : afficher les chiffres de 0 à 4

for i in range(5):
    print(i)

# range(5) génère une séquence de nombres de 0 à 4 inclus.

# On peut aussi parcourir une liste de noms :

noms = ["Alice", "Bob", "Charlie"]

for nom in noms:
    print("Bonjour", nom)

#===========================================
# La boucle 'while'

# Elle exécute le bloc tant qu’une condition est vraie.

# Exemple : afficher les nombres de 0 à 4

i = 0
while i < 5:
    print(i)
    i += 1  # on incrémente i pour éviter la boucle infinie

#===========================================
# Instructions utiles dans les boucles

# 'break' : interrompt la boucle immédiatement

for i in range(10):
    if i == 5:
        break   # arrêt quand i vaut 5
    print(i)

# 'continue' : saute à l’itération suivante

for i in range(10):
    if i % 2 == 0:
        continue  # saute les nombres pairs
    print(i)  # affiche uniquement les nombres impairs

#===========================================
# Attention aux boucles infinies !

# Exemple dangereux :

# while True:
#     print("Boucle infinie !")

# Ce code tourne sans fin, pensez toujours à prévoir une condition d'arrêt.

#===========================================
# Exercices simples

# 1) Afficher les nombres de 10 à 15 avec une boucle for
#    - Pense à stocker le dernier nombre affiché dans une variable nommée 'dernier_nombre'
# 2) Afficher les lettres de la chaîne "Python" avec une boucle while
#    - Pense à stocker la dernière lettre affichée dans une variable nommée 'derniere_lettre'

# Ton code ici :




























# correction (à ne pas toucher)
exos_c(globals())