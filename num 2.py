counter = 0
negcounter = 0
print("Введите число")
a = int(input())
if a > 0:
    for i in range(-a, a + 2):
        print(i)
        if i < 0:
            negcounter += i
        if i > 0:
            counter += i
    print(f"Сумма отрицательных чисел: {negcounter}\nСумма положительных чисел: {counter}")
elif a == 0:
    print(0, "Сумма отрицательных чисел: 0 \n Сумма положительных чисел: 0")
else:
    for i in range(-a, a, -1):
        print(i)
        if i < 0:
            negcounter += i
        if i > 0:
            counter += i
    print(f"Сумма отрицательных чисел: {negcounter}\nСумма положительных чисел: {counter}")

