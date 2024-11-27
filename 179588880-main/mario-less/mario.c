#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    while (true)
    {
        int integer = get_int("Height: ");
        if (integer == 0)
        {
            continue;
        }
        if (integer / abs(integer) == 1)
        {
            for (int i = 1; i <= integer; i++)
            {
                printf("%*s", integer - i, "");
                for (int j = 1; j <= i; j++)
                {
                    printf("#");
                }
                printf("\n");
            }
            break;
        }
        else
        {
            continue;
        }
    }
}
