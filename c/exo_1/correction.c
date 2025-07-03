#include "correction.h"
#include <stdio.h>
#include <math.h>

#define IMC_NORMAL 25.0f
#define SCORE_SANTE_INITIAL 100

int score_sante = SCORE_SANTE_INITIAL;

bool verifierBilanSportif(float poids, float taille, float imc_calcule, int score_sante_calcule) {
    float imc_attendu = poids / (taille * taille);
    int score_attendu = SCORE_SANTE_INITIAL;

    if (imc_attendu > IMC_NORMAL) {
        score_attendu -= 10;
    }

    float precision = 0.01f;

    if (fabs(imc_calcule - imc_attendu) > precision) {
        printf("Erreur : IMC incorrect. Attendu : %.2f, Obtenu : %.2f\n", imc_attendu, imc_calcule);
        return false;
    }

    if (score_sante_calcule != score_attendu) {
        printf("Erreur : Score santé incorrect. Attendu : %d, Obtenu : %d\n", score_attendu, score_sante_calcule);
        return false;
    }
    printf("Correction : Bilan sportif correct !\n");
    return true;
}

void afficherScore() {
    printf("Score santé : %d\n", score_sante);
}
