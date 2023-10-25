/*Faça um algoritmo que gere uma matriz 4x4 (4 linhas e 4 colunas), cujo valores podem ser definidos durante declaração.
Em seguida, o seu programa deve calcular e mostrar a tela a soma de todos os elementos da diagonal principal.*/

#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    int matriz[4][4] = {{1, 2, 3, 4},
                        {5, 6, 7, 8},
                        {9, 10, 11, 12},
                        {13, 14, 15, 16}};
    int soma = 0;

    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            if (i == j) {
                soma += matriz[i][j];
            }
        }
    }
    printf("A soma da diagonal da matriz é: %i", soma);

}
