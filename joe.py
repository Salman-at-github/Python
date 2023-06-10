# This program generates a matrix of random integers and applies various operations on it
import random

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for j in range(cols)] for i in range(rows)]
    
    def __str__(self):
        s = ''
        for row in self.data:
            s += ' '.join([str(x) for x in row]) + '\n'
        return s
    
    def randomize(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = random.randint(0, 10)
    
    def transpose(self):
        new_matrix = Matrix(self.cols, self.rows)
        for i in range(self.cols):
            for j in range(self.rows):
                new_matrix.data[i][j] = self.data[j][i]
        self.data = new_matrix.data
    
    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Matrices must have same dimensions')
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] += other.data[i][j]
    
    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Matrices must have same dimensions')
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] -= other.data[i][j]
    
    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError('Invalid dimensions')
        new_matrix = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                sum = 0
                for k in range(self.cols):
                    sum += self.data[i][k] * other.data[k][j]
                new_matrix.data[i][j] = sum
        self.data = new_matrix.data

# Test the Matrix class
a = Matrix(3, 4)
a.randomize()
print('Matrix a:')
print(a)

b = Matrix(4, 3)
b.randomize()
print('Matrix b:')
print(b)

c = Matrix(3, 3)
c.randomize()
print('Matrix c:')
print(c)

a.transpose()
print('Matrix a transposed:')
print(a)

a.add(c)
print('Matrix a + c:')
print(a)

a.subtract(c)
print('Matrix a - c:')
print(a)

a.multiply(b)
print('Matrix a * b:')
print(a)
