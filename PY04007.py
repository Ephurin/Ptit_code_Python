class Matrix:

    def __init__(self, n , m, mat):
        self.m = m
        self.n = n
        self.mat = mat
    
    def matrixMul(self):
        ans = []
        for i in range(self.n):
            ans += [[0] * self.n]
            for j in range(self.n):
                for k in range(self.m):
                    ans[i][j] += self.mat[i][k] * self.mat[j][k]
        return Matrix(self.n, self.m, ans)

    def printMatrix(self):
        for i in self.mat:
            print(*i)
        return ''

for t in range(int(input())):
    n, m = map(int, input().split())
    mat = []
    for i in range(n):
        mat.append([int(j) for j in input().split()])
    matrix = Matrix(n, m, mat)
    matrix = matrix.matrixMul()
    matrix.printMatrix()