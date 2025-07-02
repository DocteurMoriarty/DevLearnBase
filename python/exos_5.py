from correction import exos_e
###############################
#                             #
#       La récursivité        #
#                             #
###############################

# La récursivité, c’est quand une fonction s’appelle elle-même.
# C’est utile pour résoudre un problème en le divisant en sous-problèmes plus petits.

#===========================================
# Exemple simple : compte à rebours

def compte_a_rebours(n):
    if n <= 0:  # condition d'arrêt : on arrête la récursion ici
        print("Terminé !")
    else:
        print(n)
        compte_a_rebours(n - 1)  # on rappelle la fonction avec un nombre plus petit

# Test
compte_a_rebours(5)

#===========================================
# Exemple classique : calcul du factoriel

def factoriel(n):
    if n == 0:
        return 1  
    else:
        return n * factoriel(n - 1)  

print("5! =", factoriel(5))

#affiche 120

#===========================================
# Exercice 1 : La suite de Fibonacci récursive

# Rappel : La suite commence par 0, 1 puis chaque terme est la somme des deux précédents.
# fibonacci(0) = 0
# fibonacci(1) = 1
# fibonacci(n) = fibonacci(n-1) + fibonacci(n-2) pour n >= 2

# Consignes :
# - Implémente la fonction récursive fibonacci(n)
# - Affiche les 10 premiers termes de la suite

def fibonacci(a):
    pass


print("Suite de Fibonacci :")
for i in range(10):
    print(f"F({i}) =", fibonacci(i))


#===========================================
# Exercice 2 : Les tours de Hanoï

# Problème classique où il faut déplacer n disques d'un piquet A vers un piquet C,
# en respectant ces règles :
# 1) On déplace un disque à la fois
# 2) On ne peut pas poser un disque plus grand sur un plus petit

# Consignes :
# - Complète la fonction hanoi(n, source, cible, auxiliaire)
# - Chaque déplacement doit s'afficher sous la forme :
#   "Déplacer un disque de {source} vers {cible}"
# - Teste ta fonction avec 3 disques (n=3)


def hanoi(n, source, cible, auxiliaire):
    pass



hanoi(3, "A", "C", "B")





























# correction (à ne pas toucher)
exos_e(globals())