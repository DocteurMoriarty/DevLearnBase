from correction import exos_d
###############################
#                             #
#         Les fonctions       #
#                             #
###############################

# Les fonctions sont des morceaux de code que l'on peut "appeler" plusieurs fois,
# sans avoir besoin de réécrire tout le code.
# Cela permet de simplifier, organiser et rendre le code plus clair.

#===========================================
# 1) Définir une fonction simple

# Pour définir une fonction, on utilise le mot-clé 'def', suivi du nom de la fonction,
# puis des parenthèses () et un deux-points :
def dire_bonjour():
    # Tout ce qui est indenté en dessous fait partie de la fonction
    print("Bonjour !")  # Cette fonction affiche juste "Bonjour !"

# La fonction est juste définie ici, elle ne fait rien tant qu'on ne l'appelle pas.

# Appeler une fonction, c'est écrire son nom suivi de parenthèses.
# Cela exécute le code à l'intérieur de la fonction.
dire_bonjour()

#===========================================
# 2) Fonction avec un paramètre

# On peut donner des informations à la fonction via des "paramètres".
# Par exemple, la fonction peut saluer une personne dont on donne le nom :

def dire_bonjour_a(nom):
    # Ici 'nom' est un paramètre, une variable locale à la fonction
    print(f"Bonjour {nom} !")

# Maintenant on peut appeler la fonction avec différents noms :
dire_bonjour_a("Alice")  # Affiche "Bonjour Alice !"
dire_bonjour_a("Bob")    # Affiche "Bonjour Bob !"

# Si on oublie de donner le paramètre, Python donne une erreur.

#===========================================
# 3) Fonction qui retourne une valeur

# Parfois, une fonction doit nous "rendre" un résultat,
# on utilise alors 'return' pour renvoyer une valeur au code appelant.

def addition(a, b):
    # 'a' et 'b' sont les paramètres, ici deux nombres
    somme = a + b
    return somme   # On renvoie la somme des deux nombres

# Quand on appelle la fonction, on peut stocker le résultat dans une variable
resultat = addition(3, 7)
print("3 + 7 =", resultat)  # Affiche 3 + 7 = 10

#===========================================
# 4) Paramètres avec valeur par défaut

# On peut donner une valeur par défaut à un paramètre,
# ce qui rend ce paramètre optionnel à l'appel.

def saluer(nom="ami"):
    print(f"Salut {nom} !")

saluer()         # Affiche "Salut ami !" car on n'a rien donné
saluer("Marie")  # Affiche "Salut Marie !" avec un nom personnalisé

#===========================================
# 5) Fonction avec plusieurs instructions

# Une fonction peut faire plusieurs actions à la suite.
# On peut aussi retourner plusieurs valeurs en les regroupant dans un tuple.

def calculer_somme_et_produit(x, y):
    somme = x + y        # Addition
    produit = x * y      # Multiplication
    print(f"La somme est {somme} et le produit est {produit}")
    return somme, produit  # On renvoie les deux résultats ensemble

# Quand on récupère plusieurs valeurs, on peut les stocker dans plusieurs variables :
s, p = calculer_somme_et_produit(4, 5)
print("Somme:", s)
print("Produit:", p)

#===========================================
# 6) Exercice

# 1) Écrire une fonction 'derniere_lettre' qui prend une chaîne de caractères
#    et retourne sa dernière lettre.

# 2) Écrire une fonction 'dernier_nombre' qui prend deux entiers 'debut' et 'fin',
#    affiche tous les nombres de 'debut' à 'fin' inclus avec une boucle for,
#    et retourne le dernier nombre affiché.

# Pense bien à utiliser 'return' pour renvoyer la valeur demandée.

# Ton code ici :

















# correction (à ne pas toucher)
exos_d(globals())


