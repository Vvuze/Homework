a = input()
if(len(a) != 3):
    print("Число не трёхзначное")
    exit()

else:
    for i in a:
        if (a.count(i) > 1):
            print("Число имеет повторяющиеся цифры")
            exit()

    for i in a:
        for j in a:
            for k in a:
                if (k == i) or (k == j) or (i == j):
                    continue
                else:
                        print(i + j + k)