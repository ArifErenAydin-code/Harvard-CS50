#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
int findpoint(string word);
int main(void)
{
    string str1 = get_string("Player 1:");
    string str2 = get_string("Player 2:");

    int p1point = findpoint(str1);
    int p2point = findpoint(str2);

    if (p1point > p2point)
    {
        printf("Player 1 wins!\n");
    }
    else if (p2point > p1point)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}
int findpoint(string word)
{
    int sum = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        if (isupper(word[i]))
        {
            sum += POINTS[word[i] - 'A'];
        }
        else if (islower(word[i]))
        {
            sum += POINTS[word[i] - 'a'];
        }
    }
    return sum;
}
