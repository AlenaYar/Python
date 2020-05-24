# 1)============================================================================================

my_file = open("text_1.txt", "w", encoding="utf-8")
while True:
    string = input('Enter string: ')
    if not string:
        break
    print(string, file=my_file)
my_file.close()

# 2)============================================================================================

lines = 0
with open("text_2.txt", "r") as my_file:
    for line in my_file:
        lines += 1
        words = len(line.split(' '))

print("Lines:", lines)
print("Words:", words)

# 3)============================================================================================


# 4)============================================================================================

dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("text_4-1.txt", "w") as new_file:
    with open("text_4.txt", 'r') as my_file:
        line = my_file.read().split("\n")
        #print(line)
        for i in line:
            i = i.split(" - ")
            #print(i)
            new_file.writelines(dict[i[0]] + ' - ' + i[1] + "\n")

# 5)============================================================================================

with open("text_5.txt", "w", encoding="utf-8") as my_file:
    my_file.writelines("11 22 33 44 55 66 77 88 99")
f = open("text_5.txt")
n = f.read()
#print(n)
n = n.split()
#print(n)
for i in range(len(n)):
    n[i] = int(n[i])
print(sum(n))

# 6)============================================================================================

with open("text_6.txt", "r") as my_file:
    my_dict = dict()
    for line in my_file:
        subject, hours = line.split(": ")
        for i in hours.split():
            if i != "-":
                my_dict[subject] = my_dict.get(subject, 0) + int(i.split("(")[0])
print(my_dict)

# 7)============================================================================================