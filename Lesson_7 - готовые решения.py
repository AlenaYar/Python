# 1) ========================================================================================

class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        return '\n'.join((map(str, self.list)))

    def __add__(self, other):
        c = []
        for i in range(len(self.list)):
            c.append([])
            for j in range(len(self.list[0])):
                c[i].append(self.list[i][j] + other.list[i][j])
        return '\n'.join(map(str, c))


a = [[1, 2, 3, 4], [5, 6, 7, 8]]
b = [[8, 7, 6, 5], [4, 3, 2, 1]]
a = Matrix(a)
b = Matrix(b)
c = a + b
print(f"First matrix:\n{a}\n")
print(f"Second matrix:\n{b}\n")
print(f"Total matrix:\n{c}\n")

# 3) ========================================================================================

class MyCell:
    def __init__(self, c):
        self.c = c

    def make_order(self, row):
        c_row = int(self.c / row)
        s = ''
        for i in range(c_row):
            s += 'o' * row + '\n'
        s += (self.c - c_row * row) * 'o'
        return s

    def __str__(self):
        return self.c

    def __add__(self, other):
        return self.c + other.c

    def __sub__(self, other):
        return self.c - other.c

    def __mul__(self, other):
        return self.c * other.c

    def __truediv__(self, other):
        return self.c // other.c


a = MyCell(22)
b = MyCell(11)

add = MyCell(a + b)
print(a + b)
print(f'{add.make_order(9)}\n')

sub = MyCell(a - b)
print(a - b)
print(f'{sub.make_order(9)}\n')

mul = MyCell(a * b)
print(a * b)
print(f'{mul.make_order(9)}\n')

tru = MyCell(a / b)
print(a / b)
print(f'{tru.make_order(9)}')