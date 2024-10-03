while True:
    print("Введите число")
    a = input()
    if(a.isnumeric()):
        print("Длина числа = ", len(a))
    else:
        print("Это не число")
        exit()