#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

FILE *f;

int conta_palavras_arquivo()
{    
    char str[100];
    int num_palavras = 0;
    while (fscanf(f, "%s", str) == 1)
    {
        num_palavras++;
    }
    return num_palavras;
}

char *escolhe_palavra_secreta()
{
    static char palavra_secreta[100];
    f = fopen("palavras.txt", "r"); // caminho, leitura

    if (f == 0)
    {
        printf("Desculpe, arquivo não encontrado.");
        exit(1);
    }

    // quero escolher uma linha
    srand(time(0));
    int randomico = rand() % conta_palavras_arquivo(f);
    fseek(f, 0, SEEK_SET);
    int index_atual_palavra = 0;
    while ((fscanf(f, "%s", palavra_secreta)) != EOF)
    {
        if (index_atual_palavra == randomico)
        {
            break;
        }
        index_atual_palavra++;
    }
    // vou lendo sequencialmente ate loop acabar
    // palavra_secreta -> valor no indice aleatorio q pegamos
    fclose(f);
    return palavra_secreta;
}

void adiciona_palavra()
{
    char opcao;
    printf("Deseja adicionar uma nova palavra? (default: n/y) ");
    scanf(" %c", &opcao);
    if (opcao == 'y')
    {
        printf("Qual a nova palavra? \n");
        char nova_palavra[100];
        scanf("%s", nova_palavra);

        f = fopen("palavras.txt", "a");
        if(f == NULL){
            printf("Desculpe, não consegui abrir o arquivo.");
            
        }
        fprintf(f, "\n%s", nova_palavra);        
        fclose(f);
    }
    else
    {
        printf("Obrigado por jogar o jogo da forca! :)\n");
        exit(1);
    }
}

void gera_baner()
{
    printf("***********************\n");
    printf("*    JOGO DA FORCA    *\n");
    printf("***********************\n\n");
}

void chutar(char *chutes, int *tentativas)
{
    char chute;
    scanf(" %c", &chute);        // %c ignora o enter (enter é um char digitado)
    chutes[*tentativas] = chute; // guarda o char chute dentro do array
    (*tentativas)++;
}

int ja_foi_chutado(char letra, char *chutes, int tentativas)
{
    for (int i = 0; i < tentativas; i++)
    {
        if (chutes[i] == letra)
        {
            return 1;
        }
    }
    return 0;
}

void desenha_forca(char *palavra_secreta, char *chutes, int tentativas)
{
    for (int i = 0; i < strlen(palavra_secreta); i++)
    {
        int existe_letra = ja_foi_chutado(palavra_secreta[i], chutes, tentativas);
        if (existe_letra)
        {
            printf("%c ", palavra_secreta[i]);
        }
        else
        {
            printf("_ ");
        }
    }
}

int enforcou(char *chutes, char *palavra_secreta, int tentativas)
{
    int erros = 0;
    for (int i = 0; i < tentativas; i++)
    {
        int existe_letra = 0;
        for (int j = 0; j < strlen(palavra_secreta); j++)
        {
            if (chutes[i] == palavra_secreta[j])
            {
                existe_letra = 1;
                break;
            }
        }
        if (!existe_letra)
            erros++;
    }
    return erros >= 5; // limite de erros
}

int ganhou(char *palavra_secreta, char *chutes, int tentativas)
{
    for (int i = 0; i < strlen(palavra_secreta); i++)
    {
        if (!ja_foi_chutado(palavra_secreta[i], chutes, tentativas))
        {
            return 0;
        }
    }
    return 1;
}

int main()
{
    // char palavra_secreta[20];
    char palavra_secreta[100];
    char chutes[26];    // array é por natureza um ponteiro
    int tentativas = 0; // quantos chutes ja deu
    strcpy(palavra_secreta, escolhe_palavra_secreta());

    gera_baner();
    do
    {
        desenha_forca(palavra_secreta, chutes, tentativas);
        printf("\n");
        chutar(chutes, &tentativas);

    } while (!ganhou(palavra_secreta, chutes, tentativas) &&
             !enforcou(chutes, palavra_secreta, tentativas));

    adiciona_palavra();
    return 0;
}
