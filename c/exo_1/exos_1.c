/*
 * Exercice : Calcul d’un bilan sportif
 * 
 * Objectifs :
 * 1. Demander le prénom de l’utilisateur (char prenom[50]).
 * 2. Demander l’âge (unsigned int age), la taille (float taille) et le poids (float poids).
 * 3. Calculer l’IMC (float imc) : imc = poids / (taille * taille)
 * 4. Utiliser une constante IMC_NORMAL = 25.0f
 * 5. Afficher un résumé des informations.
 * 6. Si imc > IMC_NORMAL, afficher un message d’alerte et diminuer la variable globale score_sante (int) initialisée à 100.
 * 7. Afficher le score santé avec la fonction externe afficherScore().
 * 8. En fin de main(), appeler la fonction externe bool verifierBilanSportif(float poids, float taille, float imc, int score_sante).
 * 9. Compiler avec : gcc -Wall -Wextra -g bilan_sportif.c correction.c -o bilan_sportif
 * 
 * Bonus :
 * Utiliser man 3 printf et man 3 scanf pour comprendre les formats.
 */


#include <stdio.h>
#include <stdbool.h>
#include "correction.h"

#define IMC_NORMAL 25.0f

int main() {
    // Variables à utiliser impérativement :
    char prenom[50];
    unsigned int age;
    float taille, poids, imc;

    // Score santé est une variable globale définie dans correction.c
    // On y accède directement via la variable globale score_sante

    // 1. Demander le prénom de l’utilisateur (avec scanf)
    // TODO :

    // 2. Demander l’âge (unsigned int)
    // TODO :

    // 3. Demander la taille (float)
    // TODO :

    // 4. Demander le poids (float)
    // TODO :

    // 5. Calculer l’IMC : imc = poids / (taille * taille)
    // TODO :

    // 6. Afficher un résumé des informations (prénom, âge, taille, poids, imc)
    // TODO :

    // 7. Si imc > IMC_NORMAL, afficher un message d’alerte et diminuer score_sante de 10
    // TODO :

    // 8. Afficher le score santé avec la fonction externe afficherScore()
    // TODO :

    // 9. Appeler la fonction externe verifierBilanSportif() avec poids, taille, imc, score_sante
    //    Puis afficher si l’élève a bien réalisé l’exercice ou non
    // TODO :

    return 0;
}
