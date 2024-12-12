#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Kullanıcıdan metin girişi
    string text = get_string("Text: ");

    // Mektup, kelime ve cümle sayılarını say
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // L ve S hesaplamaları, tamsayıların float'a çevrilmesi önemli
    float L = ((float) letters / words) * 100;
    float S = ((float) sentences / words) * 100;

    // Coleman-Liau index formülü
    float index = 0.0588 * L - 0.296 * S - 15.8;

    // Sonuçları yazdır
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %.0f\n", round(index)); // Yuvarlayarak tam sayı çıktısı
    }
}

// Harf sayma fonksiyonu
int count_letters(string text)
{
    int sum = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i])) // isalpha() fonksiyonu kullanarak harf olup olmadığını kontrol edin
        {
            sum++;
        }
    }
    return sum;
}

// Kelime sayma fonksiyonu
int count_words(string text)
{
    int sum = 1; // Kelime sayısı en az 1 olmalı
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == ' ') // Boşluklara bakarak kelimeleri sayın
        {
            sum++;
        }
    }
    return sum;
}

// Cümle sayma fonksiyonu
int count_sentences(string text)
{
    int sum = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == '.' || text[i] == '!' ||
            text[i] == '?') // Noktalama işaretleriyle cümleleri sayın
        {
            sum++;
        }
    }
    return sum;
}
