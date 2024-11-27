
def count_letters(text):
    sum = 0
    for i in range(0, len(text)):
        if text[i].isalpha():
            sum += 1
    return sum


def count_words(text):
    sum = 1
    for i in range(0, len(text)):
        if text[i] == " ":
            sum += 1
    return sum


def count_sentences(text):
    sentence_endings = ".!?"  # Cümle bitişlerini belirleyen karakterler
    sum = 0
    for i in text:
        if i in sentence_endings:
            sum += 1
    return sum


def main():
    text = input("Lütfen metini giriniz:")

    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    L = (letters / words) * 100
    S = (sentences / words) * 100

    index = 0.0588 * L - 0.296 * S - 15.8

    if index < 1:
        print("Before Grade 1")
    elif (index >= 16):
        print("Grade 16+")
    else:
        print("Grade {}".format(round(index)))


if __name__ == "__main__":
    main()
