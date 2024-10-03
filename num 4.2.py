print("Способ выполнения при помощи format")
print("Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет.\n".format(name = input("Введите имя\n"), surname = input("Введите фамилию\n"), age = input("Введите возраст\n")))

print("Способ выполнения при помощи f-string")
name = input("Введите имя\n")
surname = input("Введите фамилию\n")
age = input("Введите возраст\n")
print(f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет.")