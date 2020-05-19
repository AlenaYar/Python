a = float(input("Введите a: "))
b = float(input("Введите b: "))
print("Результат:")
l = 1
while True:
    print(f"{l}" + "-й день: " + f"{a:.2f}" + " км")
    a += a * 0.1
    l += 1
    if a <= b:
        continue

    if a > b:
        print(f"{l}" + "-й день: " + f"{a:.2f}" + " км")
        break

print("Ответ: на " + str(l) + "-й день спортсмен достиг результата - не менее " + str(int(b)) + " км.")
