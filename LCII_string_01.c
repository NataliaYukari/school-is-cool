/*Faça um programa que peça para um usuário digitar o login e uma senha.
O usuário poderá entrar no sistema somente se o login e a senha corresponderem.
O login deve ser "admin“ e a senha "1234“. Se o login e a senha corresponderem, mostre uma mensagem de boas vindas para o usuário.
Caso contrário, mostre uma mensagem de erro.*/

#include <stdio.h>
#include <locale.h>
#include <string.h>

int main() {
    char login[50];
    char senha[50];

    printf("Olá, digite:\n");
    printf("Login: ");
    gets(login);

    printf("\nSenha: ");
    gets(senha);
}
