print("n + nn + nnn = ?")
n = int(input("Введите число n - "))
a = n
b = int(str(n) + str(n))
c = int(str(n) + str(n) + str(n))
d = a + b + c
print(str(a) + str(" + ") + str(b) + str(" + ") + str(c) + str(" = ") + str(d))