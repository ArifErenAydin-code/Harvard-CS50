#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int cents;
    int calculate_quarters(int cents);

    while (true)
    {
        cents = get_int("Change owed: ");
        if (cents < 0)
        {
            printf("Please write an positive integer\n");
            continue;
        }
        else if (cents == 0)
        {
            printf("0\n");
            continue;
        }
        else
        {
            int quarters = calculate_quarters(cents);
            printf("Change owed: %d\n", quarters);
            break;
        }
    }
}
int calculate_quarters(int cents)
{
    int twentyfive_count = cents / 25;
    cents -= twentyfive_count * 25;
    int ten_count = cents / 10;
    cents -= ten_count * 10;
    int five_count = cents / 5;
    cents -= five_count * 5;
    int one_count = cents / 1;
    int quarters = twentyfive_count + ten_count + five_count + one_count;
    return quarters;
}
