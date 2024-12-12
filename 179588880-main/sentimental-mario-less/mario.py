while True:
    try:
        height = int(input("Height: "))
        if (height == -1 or height == 0):
            print("Type another number")

        if 0 < height < 9:
            for i in range(1, height+1):
                print(" "*(height-i) + ("#"*(i)))
            break
        else:
            continue
    except ValueError:
        print("Geçersiz giriş! Lütfen bir sayı girin.")
        continue
