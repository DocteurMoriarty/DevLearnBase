#fichier à ne pas toucher
import io
import sys


def exos_a(age, refus):
    try:
        assert isinstance(age, float) and age >= 18, "age doit être un float ou supérieur à 18"
        assert isinstance(refus, str) and refus == "aaaaaaaaah", "refus n'est pas une string ou n'est pas le meme string que demander dans l'exercice"
        return True
    except AssertionError as e:
        print(e) 
        return False


def exos_b(verifier_entree):
    tests = [
        (15, "sobre", "Trop jeune"),
        (17, "sobre", "Entrée limitée, mais sobre"),
        (17, "bourré", "Accès refusé"),
        (20, "sobre", "Bienvenue en boîte !"),
        (20, "bourré", "Accès refusé, trop bourré"),
    ]
    for age, etat, attendu in tests:
        try:
            resultat = verifier_entree(age, etat)
            assert resultat == attendu, f"Test failed: verifier_entree({age}, '{etat}') returned '{resultat}', expected '{attendu}'"
        except Exception as e:
            print(f"Erreur sur verifier_entree({age}, '{etat}'): {e}")
            return False
    return True



def exos_c(namespace):
    if 'dernier_nombre' not in namespace:
        print("Erreur : variable 'dernier_nombre' non définie.")
        return False
    if 'derniere_lettre' not in namespace:
        print("Erreur : variable 'derniere_lettre' non définie.")
        return False
    if namespace['dernier_nombre'] != 15:
        print(f"Erreur : 'dernier_nombre' doit valoir 15, trouvé {namespace['dernier_nombre']}")
        return False
    if namespace['derniere_lettre'] != 'n':
        print(f"Erreur : 'derniere_lettre' doit valoir 'n', trouvé '{namespace['derniere_lettre']}'")
        return False

    print("VOUS AVEZ REUSSI L'EXERCICE !")
    return True



def exos_d(env):
    if "derniere_lettre" not in env:
        print("Erreur : la fonction 'derniere_lettre' n'est pas définie.")
        return False
    if "dernier_nombre" not in env:
        print("Erreur : la fonction 'dernier_nombre' n'est pas définie.")
        return False

    dl = env["derniere_lettre"]
    dn = env["dernier_nombre"]
    try:
        res1 = dl("Python")
        if res1 != "n":
            print(f"Erreur dans 'derniere_lettre': attendu 'n', obtenu '{res1}'")
            return False
        res2 = dl("chat")
        if res2 != "t":
            print(f"Erreur dans 'derniere_lettre': attendu 't', obtenu '{res2}'")
            return False
    except Exception as e:
        print(f"Exception lors du test de 'derniere_lettre': {e}")
        return False

    try:
        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()

        ret = dn(10, 15)

        sys.stdout = old_stdout
        sortie = mystdout.getvalue()
        expected_output = "\n".join(str(i) for i in range(10, 16)) + "\n"
        if sortie != expected_output:
            print(f"Erreur dans l'affichage de 'dernier_nombre'.\nAttendu :\n{expected_output}\nObtenu :\n{sortie}")
            return False

        if ret != 15:
            print(f"Erreur dans la valeur retournée par 'dernier_nombre'. Attendu : 15, obtenu : {ret}")
            return False
    except Exception as e:
        print(f"Exception lors du test de 'dernier_nombre': {e}")
        return False

    print("VOUS AVEZ REUSSI L'EXERCICE !")
    return True





def correction_fibonacci(fib_func):
    correct = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    try:
        for i, val in enumerate(correct):
            if fib_func(i) != val:
                print(f"Erreur à fibonacci({i}): attendu {val}, obtenu {fib_func(i)}")
                return False
    except Exception as e:
        print(f"Erreur lors de l'exécution de fibonacci: {e}")
        return False
    print("Fonction fibonacci correcte !")
    return True


def correction_hanoi(hanoi_func):
    expected_moves = [
        "Déplacer un disque de A vers C",
        "Déplacer un disque de A vers B",
        "Déplacer un disque de C vers B",
        "Déplacer un disque de A vers C",
        "Déplacer un disque de B vers A",
        "Déplacer un disque de B vers C",
        "Déplacer un disque de A vers C"
    ]
    captured_output = io.StringIO()
    sys.stdout = captured_output
    try:
        hanoi_func(3, "A", "C", "B")
    except Exception as e:
        sys.stdout = sys.__stdout__
        print(f"Erreur lors de l'exécution de hanoi: {e}")
        return False
    sys.stdout = sys.__stdout__
    output_lines = captured_output.getvalue().strip().split('\n')
    output_lines = [line.strip() for line in output_lines if line.strip() != '']

    if output_lines != expected_moves:
        print("Erreur dans les déplacements hanoi :")
        print("Sortie obtenue :")
        for line in output_lines:
            print(line)
        print("\nSortie attendue :")
        for line in expected_moves:
            print(line)
        return False
    print("Fonction hanoi correcte !")
    return True


def exos_e(globals_dict):
    fib_ok = correction_fibonacci(globals_dict.get("fibonacci"))
    hanoi_ok = correction_hanoi(globals_dict.get("hanoi"))
    if fib_ok and hanoi_ok:
        print("\nVOUS AVEZ REUSSI LES EXERCICES !")
    else:
        print("\nExercices échoués. Revois tes fonctions.")
