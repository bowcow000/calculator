def main():
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")

    choice = input("Введите номер операции: ")

    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    if choice == '1':
        result = num1 + num2
        print("Результат: ", result)
    elif choice == '2':
        result = num1 - num2
        print("Результат: ", result)
    elif choice == '3':
        result = num1 * num2
        print("Результат: ", result)
    elif choice == '4':

        if num2 or num1 == 0:
            print("Ошибка! Деление на ноль невозможно.")
        else:
            result = num1 / num2
            print("Результат: ", result)
    else:
        print("Ошибка! Неверный выбор операции.")

if __name__ == "__main__":
    main()