n = int(input("Введите время с секундах - "))
h = n // 3600
n1 = n % 3600
m = n1 // 60
s = n1 % 60
print(str(h) + str(":") + str(m) + str(":") + str(s))

