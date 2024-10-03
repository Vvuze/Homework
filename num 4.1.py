ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
print("Сделайте ход")
a = input().upper()
if a in ship:
    print("Попал")
else:
    print("Не попал")