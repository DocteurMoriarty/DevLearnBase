/*
 * Cours complémentaire : La fonction main et le compilateur gcc
 *
 * 1. La fonction main
 * 
 * En C, l'exécution du programme commence toujours par la fonction spéciale :
 * 
 * int main() { ... }
 *
 * La fonction main est le point d'entrée du programme. C'est la première fonction appelée
 * lorsque le programme démarre. Elle est obligatoire dans tout programme C.
 *
 * Syntaxe de base :
 * 
 * int main() {
 *     // Corps du programme
 *     return 0; // Indique que le programme s'est terminé correctement.
 * }
 *
 * Notes importantes :
 * - Le type de retour de la fonction main est "int", ce qui signifie qu'elle retourne un entier.
 * - La convention en C est de retourner 0 lorsque tout s'est bien passé.
 * - Un retour différent de 0 peut indiquer une erreur d'exécution.
 * 
 * Exemple :
 * 
 * int main() {
 *     printf("Bonjour !\n");
 *     return 0;
 * }
 *
 * Variante possible :
 * On peut aussi écrire :
 * int main(int argc, char *argv[]) { ... }
 * Cela permet de récupérer des arguments passés dans la ligne de commande.
 *
 * Exemple :
 * gcc mon_programme.c -o mon_programme
 * ./mon_programme arg1 arg2
 * Ici :
 * - argc contient le nombre d'arguments.
 * - argv est un tableau de chaînes représentant les arguments.
 * 
 * ---------------------------------------------------------
 *
 * 2. Utilisation du compilateur gcc
 *
 * gcc (GNU Compiler Collection) est l'un des compilateurs C les plus utilisés.
 *
 * Commande de base pour compiler un fichier :
 * 
 * gcc fichier_source.c -o nom_executable
 *
 * - fichier_source.c : le fichier C à compiler.
 * - -o nom_executable : le nom du fichier exécutable généré.
 *
 * Exemple :
 * gcc exos_1.c -o exos_1
 * 
 * Cette commande va générer un exécutable nommé "exos_1".
 * Pour l'exécuter :
 * ./exos_1
 *
 * Quelques options utiles :
 * - gcc -Wall exos_1.c -o exos_1
 *   => Active l'affichage de tous les avertissements de compilation.
 *
 * - gcc -g exos_1.c -o exos_1
 *   => Génère des informations de débogage.
 *
 * - gcc -O2 exos_1.c -o exos_1
 *   => Active des optimisations pour améliorer la performance.
 *
 * Bonnes pratiques :
 * - Toujours compiler avec l'option -Wall pour détecter les erreurs potentielles.
 * - Ajouter -Wextra pour des avertissements supplémentaires.
 *
 * Exemple recommandé :
 * gcc -Wall -Wextra -g exos_1.c -o exos_1
 *
 *
 * Cours sur les variables en C avec exemples.
 *
 * 1. Qu'est-ce qu'une variable ?
 * Une variable est un emplacement mémoire nommé qui contient une valeur modifiable pendant l'exécution du programme.
 *
 * 2. Déclaration
 * Syntaxe : type nom_variable;
 * Exemple : int age;
 *
 * Le C est un langage typé, ce qui signifie que chaque variable doit être déclarée avec un type spécifique avant de l'utiliser.
 * 
 * 3. Types de base
 * - int : entier (ex: 10, -5)
 * - float : nombre à virgule simple (ex: 3.14)
 * - double : nombre à virgule double précision (ex: 3.14159)
 * - char : caractère (ex: 'A')
 * - unsigned int : entier non signé (ex: 10U)
 * - long : entier long (généralement 32 bits ou plus, ex: 100000L)
 * - short : entier court (généralement 16 bits)
 * - bool : booléen (vrai ou faux, nécessite l'inclusion de <stdbool.h> en C)
 * - string : chaîne de caractères (en C, on utilise un tableau de char, ex: "Bonjour")
 * - void : type vide, utilisé pour indiquer l'absence de valeur (ex: fonction qui ne retourne rien).
 * - unsigned long : entier long non signé (ex: 100000UL)
 * - unsigned short : entier court non signé (ex: 100U)
 * * 3.1. Déclaration de plusieurs variables
 *
 * 
 *  On peut déclarer plusieurs variables du même type sur une seule ligne :
 * int x, y, z;
 * 
 * 4. Initialisation
 * On peut initialiser une variable au moment de sa déclaration :
 * int age = 30;
 *
 * 5. Affectation
 * On peut modifier la valeur d'une variable après sa déclaration :
 * age = 35;
 */


#include <stdio.h>

// -------------------------------
// Variable globale : accessible partout dans le fichier
int score_global = 100;

void afficherScore() {
    // Exemple d'accès à la variable globale
    printf("Score global : %d\n", score_global);
}








int main() {
    // Déclaration d'une variable entière
    int age;

    // Initialisation
    age = 25;

    // Affichage
    printf("Age initial : %d\n", age);

    // Modification de la variable
    age = 30;
    printf("Age modifié : %d\n", age);

    // Déclaration et initialisation d'une variable float
    float taille = 1.75f;
    printf("Taille : %.2f mètres\n", taille);

    // Déclaration et initialisation d'une variable char
    char lettre = 'C';
    printf("Lettre : %c\n", lettre);

    // Exemple de plusieurs variables
    int x = 5, y = 10;
    printf("x = %d, y = %d\n", x, y);


    /*
    * Suite du cours sur les variables en C :
    * - Constantes
    * - Modificateurs de type
    * - Portée des variables
    * - Variables globales et locales
    * - Entrée utilisateur
    * - Conversion de types (casting)
    */





    // 1. Déclaration d'une constante
    const float PI = 3.14159f;

    printf("La valeur de PI est : %.5f\n", PI);

    // 2. Modificateurs de type
    unsigned int vitesse = 120; // Entier positif uniquement
    long distance = 1000000L;   // Grand nombre
    short petiteValeur = 25;    // Petit nombre

    printf("Vitesse : %u km/h\n", vitesse);
    printf("Distance : %ld mètres\n", distance);
    printf("Petite valeur : %hd\n", petiteValeur);

    // 3. Variables locales
    int score_local = 50;
    printf("Score local : %d\n", score_local);

    afficherScore(); // Fonction utilisant la variable globale

    // 4. Lecture utilisateur
    int age2;
    printf("Entrez votre âge : ");
    scanf("%d", &age2);
    printf("Vous avez %d ans.\n", age2);

    // 5. Conversion de type (casting)
    float prix = 10.99f;
    int prixArrondi = (int) prix; // cast explicite
    printf("Prix arrondi : %d euros\n", prixArrondi);



    /*
    *   man gcc         Lire la doc du compilateur
    *   man printf      Lire la doc de printf
    *   man 3 printf    Accès direct à la section 3 (fonctions C)
    *   man scanf       Lire la doc de scanf
    *   man 3 scanf     Accès direct à la section 3 (fonctions C)
    */








    return 0;
}



