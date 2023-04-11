n = int(input("Введите размер массива: "))
a = [int(input(f"Введите элемент a[{i}]: ")) for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            print(a[i], end=' ')
        else:
            print(' ', end=' ')
    print()
