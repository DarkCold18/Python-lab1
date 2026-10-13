def calculate_x(a, b):
    if a > b:
        return a * a - b
    elif a == b:
        return -a
    else:
        return (a * b - 1) / b
def build_pyramid(n):
    for i in range(1, n + 1):
        for j in range(n, i, -1):
            print(" ", end="")
        for j in range(i):
            print(i, end=" ")
        print("")
a = float(input("Введіть a (от 1 до 100): "))
while a < 1 or a > 100:
    a = float(input("Введіть ще раз a (от 1 до 100): "))
b = float(input("Введіть b (от 1 до 100): "))
while b < 1 or b > 100:
    b = float(input("Введіть ще раз b (от 1 до 100): "))
print("Результат X =", calculate_x(a, b))
print()
n = int(input("Введіть N (от 1 до 10): "))
while n < 1 or n > 10:
    n = int(input("Введіть ще раз N (от 1 до 10): "))
print()
build_pyramid(n)
