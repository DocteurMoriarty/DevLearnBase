from correction import exos_b
###############################
#                             #
#        Les conditions       #
#                             #
###############################

# Cours
# Les conditions sont des questions que l'on pose à la machine.
# Exemple :

martine = "chocolatine"

if martine == "croissant":
    print("Martine mange des croissants")
elif martine == "chocolatine":
    print("Martine mange des chocolatines")
else:
    print("Martine ne mange rien ?")

# Explications :
# Si martine est égale à "croissant" alors la machine affichera : Martine mange des croissants
# Sinon, si martine est égale à "chocolatine" alors la machine affichera : Martine mange des chocolatines
# Si martine ne correspond à aucune des deux, la machine affichera : Martine ne mange rien ?

# ===========================================
# À toi de jouer :
# Change la valeur de la variable martine pour afficher les 3 cas possibles !

# Cas 1 : Martine mange des croissants
martine = "croissant"
if martine == "croissant":
    print("Martine mange des croissants")
elif martine == "chocolatine":
    print("Martine mange des chocolatines")
else:
    print("Martine ne mange rien ?")

# Cas 2 : Martine mange des chocolatines
martine = "chocolatine"
if martine == "croissant":
    print("Martine mange des croissants")
elif martine == "chocolatine":
    print("Martine mange des chocolatines")
else:
    print("Martine ne mange rien ?")

# Cas 3 : Martine ne mange rien
martine = "pain au lait"
if martine == "croissant":
    print("Martine mange des croissants")
elif martine == "chocolatine":
    print("Martine mange des chocolatines")
else:
    print("Martine ne mange rien ?")

# ===========================================
# Tips :
# Les conditions se lisent toujours comme une question : "Est-ce que cette valeur est vraie ?"
# On peut combiner plusieurs conditions avec "and" ou "or" pour créer des choix plus complexes.


# Pour comprendre les conditions, il faut comprendre les opérateurs.
# Ce nom semble compliqué mais il n'en est rien.
# Les opérateurs sont les éléments qui vous serviront pour manipuler les variables et les comparer.

#===========================================
# Les opérateurs de base (mathématiques)
#===========================================

# Assignation
# =
# Sert à stocker une valeur dans une variable

a = 5  # ici on dit que a vaut 5

# Addition
# +

b = 3 + 2  # b vaut 5

# Soustraction
# -

c = 10 - 4  # c vaut 6

# Multiplication
# *

d = 7 * 2  # d vaut 14

# Division
# /

e = 10 / 2  # e vaut 5.0 (Attention : en Python une division retourne toujours un float)

# Division entière (sans virgule)
# //

f = 10 // 3  # f vaut 3 (le reste est ignoré)

# Modulo (reste de la division)
# %

g = 10 % 3  # g vaut 1 (car 10 = 3 * 3 + 1)

# Puissance
# **

h = 2 ** 3  # h vaut 8 (2 puissance 3)

# Affichons les résultats
print(a, b, c, d, e, f, g, h)

#===========================================
# Les opérateurs de comparaison
#===========================================

# Pour faire des conditions, on doit comparer des valeurs avec des opérateurs spécifiques

# Egalité
# ==

print(5 == 5)  # True

# Différent
# !=

print(5 != 3)  # True

# Plus grand
# >

print(7 > 2)  # True

# Plus petit
# <

print(4 < 9)  # True

# Plus grand ou égal
# >=

print(6 >= 6)  # True

# Plus petit ou égal
# <=

print(3 <= 8)  # True

#===========================================
# Les opérateurs logiques (pour les conditions combinées)
#===========================================

# ET logique
# and

print(5 > 2 and 6 < 9)  # True (les deux conditions doivent être vraies)

# OU logique
# or

print(5 > 10 or 6 < 9)  # True (au moins une des conditions doit être vraie)

# Négation
# not

print(not True)  # False
print(not False)  # True

#===========================================
# Les conditions (if)
#===========================================

# Exemple simple

age = 20

if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")



#===========================================
# Fin du chapitre sur les opérateurs et les conditions
#===========================================

# Tips :
# Quand vous ne savez pas pourquoi votre condition ne passe pas, vous pouvez toujours afficher la variable avec print() et vérifier son type avec type()




# EXERCICE - Boîte de nuit avancée

# Variables données (ne pas modifier)
age = 17       # float ou int
etat = "sobre" # string, soit "sobre" ou "bourré"

# Objectif :
# Ecris une fonction unique nommée 'verifier_entree' qui prend en paramètres `age` et `etat` et renvoie un string :
#   - Si la personne a moins de 16 ans, renvoyer "Trop jeune"
#   - Si la personne a entre 16 (inclus) et 18 ans (exclu), elle peut entrer uniquement si elle est sobre,
#     sinon accès refusé. 
#     Renvoie "Entrée limitée, mais sobre" ou "Accès refusé"
#   - Si la personne a 18 ans ou plus, elle peut entrer uniquement si elle est sobre,
#     sinon accès refusé. 
#     Renvoie "Bienvenue en boîte !" ou "Accès refusé, trop bourré"
# Tu dois gérer toute la logique avec un seul if/else (pas plusieurs elif)
# Exemple d’appel : verifier_entree(20, "bourré") doit retourner "Accès refusé, trop bourré"

def verifier_entree(age, etat):
    # Ton code ici
    pass















# correction (à ne pas toucher)
if exos_b(verifier_entree):
    print("VOUS AVEZ REUSSI L'EXERCICE!")
















