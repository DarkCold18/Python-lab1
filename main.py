import module1
import module2

while True:
    print("\n" + "=" * 30)
    print("           МЕНЮ")
    print("=" * 30)
    print("1. Обчислити значення виразу")
    print("2. Знайти суму чисел, кратних 5 (від 500 до 1000)")
    print("3. Вихід з програми")
    choice = input("\nОберіть дію (введіть 1, 2 або 3): ")
    if choice == '1':
        print("\n--- Обчислення виразу ---")
        a = float(input("Введіть значення a: "))
        b = float(input("Введіть значення b: "))
        x = float(input("Введіть значення x: "))
        y = float(input("Введіть значення y (y >= 0): "))
        while y < 0:
            y = float(input("Помилка! Корінь з від'ємного числа неможливий. Введіть y >= 0: "))
        result = module1.calculate_expression(a, b, x, y)
        print("Результат y =", result)
    elif choice == '2':
        print("\n--- Знаходження суми ---")
        result_sum = module2.sum_multiples_of_5()
        print("Сума натуральних чисел, кратних 5 (від 500 до 1000) дорівнює:", result_sum)
    elif choice == '3':
        print("Роботу програми завершено.")
        break
    else:
        print("Неправильний вибір! Будь ласка, введіть 1, 2 або 3.")
