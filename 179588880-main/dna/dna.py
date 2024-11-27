import csv
import sys


def main():

    if len(sys.argv) != 3:
        print("Usage: python dna.py database.csv sequence.txt")
        sys.exit(1)

    database = []
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            database.append(row)

    with open(sys.argv[2]) as file:
        sequence = file.read()

    str_counts = []
    for str_seq in header[1:]:
        str_counts.append(longest_match(sequence, str_seq))

    for row in database:
        name = row[0]
        str_values = [int(num) for num in row[1:]]
        if str_values == str_counts:
            print(name)
            return

    print("No match")


def longest_match(sequence, subsequence):
    """Verilen dizide subsequence'in en uzun tekrar sayısını döndürür."""
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    for i in range(sequence_length):
        count = 0
        while sequence[i + count * subsequence_length:i + (count + 1) * subsequence_length] == subsequence:
            count += 1
        longest_run = max(longest_run, count)

    return longest_run


if __name__ == "__main__":
    main()
