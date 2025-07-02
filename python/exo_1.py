from correction import exos_a

###############################
#                             #
#        Les variables        #
#                             #
###############################

# Cours

# les types (un type est une forme de données, nous allons voir les différents types en python )

# WARNING
# Le python est un langage non typé contrairement à des langages tels que le C/C++, Rust ...
# Les variables ne sont pas obligatoirement typées.

# PRINT
# print n'est pas une variable c'est la méthode (fonction) pour afficher un résultat dans la console
print("Ce texte s'affichera dans la console")

# ===========================================
# Les string et char (string et caractère)
a = 'a'

# affichage du char et du type
print(a)
print(type(a))

# Les int (integer)
rire = "ahahaha"

# affichage du string et du type
print(rire)
print(type(rire))

# les strings se trouvent toujours entre "" ou ''

# NOTE:
# Vous allez me dire mais Docteur c'est la même chose ?
# - Oui exactement en python on ne fait pas de différence entre le char et le string les deux sont identiques

# ===========================================

# ===========================================
# Les float (flottant)
age_test = 17.5

# affichage du float et du type
print(age_test)
print(type(age_test))

# ===========================================

# ===========================================
# Les bool (boolean)
# Les mathématiques booléennes sont binaires, ça signifie qu'il y a seulement 2 types dans le cas du python : True = vrai et False = faux

valid = True
invalid = False
# affichage du bool et du type
print(valid)
print(type(valid))

# ===========================================

# ===========================================
# Les lists (list)
# Les listes sont des sortes de coffres dans lesquels nous allons insérer des données pour les réutiliser de différentes manières
# Tous les types de données peuvent être stockés dans une liste
amis = [16, 17.9, 18]

# affichage de la liste et du type
print(amis)
print(type(amis))

# ===========================================

# ===========================================
# Les tuples (tuple)
# ===========================================

amis_name = ("sandra", "jessica", "marine")
# affichage du tuple et du type
print(amis_name)
print(type(amis_name))

# ===========================================
# Les dicts (dictionnaire)
# ===========================================

repliques = {"Daniel": "Non vous êtes pas assez grande !", "Jamal": "Seulement", "Laurent": "Allez y !"}
# affichage du dict et du type
print(repliques)
print(type(repliques))

# Tips : si dans un programme que vous développez vous êtes perdus n'hésitez pas à utiliser 
# la fonction type()
# cette dernière vous retournera le type de l'objet

###############################
#                             #
#        Les exercices        #
#                             #
###############################

# WARNING : les variables doivent être respectées à la lettre près

# CONSIGNES
# Déclarer une variable string "aaaaaaaaah" nommée refus
# Déclarer une variable float supérieur à 18 nommée age

#votre code















# correction (à ne pas toucher)
try:
    age
except NameError:
    print("Erreur : la variable 'age' n'est pas définie.")
    age = None

try:
    refus
except NameError:
    print("Erreur : la variable 'refus' n'est pas définie.")
    refus = None

if age is None or refus is None:
    print("Impossible de tester exos_a : variable(s) manquante(s).")
else:
    print(exos_a(age, refus))
    if exos_a(age, refus):
        print("VOUS AVEZ REUSSI L'EXERCICE!")
