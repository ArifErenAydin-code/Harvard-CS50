def calculate_quarters(dolar):
    twentyfive_count = dolar // 0.25
    dolar -= twentyfive_count * 0.25
    dolar += 0.000000002
    print(dolar)

    ten_count = dolar // 0.10
    dolar -= ten_count * 0.10
    dolar += 0.000000002
    print(dolar)
    five_count = dolar // 0.05
    dolar -= five_count * 0.05
    dolar += 0.000000001
    print(dolar)
    one_count = dolar // 0.01

    quarters = twentyfive_count + ten_count + five_count + one_count
    print(twentyfive_count)
    print(ten_count)
    print(five_count)
    print(one_count)

    return quarters


def main():
    while True:
        try:

            cents = float(input("Change owed: "))

            if cents < 0:
                print("Please write a positive integer")
                continue
            elif cents == 0:
                print("0")
                continue
            else:

                quarters = calculate_quarters(cents)
                print("Change owed:", quarters)
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")


if __name__ == "__main__":
    main()
