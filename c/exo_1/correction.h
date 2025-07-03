#ifndef CORRECTION_H
#define CORRECTION_H

#include <stdbool.h>

extern int score_sante; // variable globale déclarée dans correction.c

void afficherScore(void);
bool verifierBilanSportif(float poids, float taille, float imc_calcule, int score_sante_calcule);

#endif
