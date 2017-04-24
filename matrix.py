from math import floor
class matrix:
    ss = 0
    
    def __init__(self, mat=[]):
        self.m = mat

    @property
    def m(self):
        return self.__m

    @m.setter
    def m(self, val):
        if not isinstance(val, list):
            raise TypeError("m must be list")
        for i in val:
            if not isinstance(i, list):
                raise TypeError("incorrect data format")
            if len(i) != len(val[0]):
                raise ValueError("incorrect row length")
        self.__m = self.__toss(val)
        
    @property
    def rows(self):
        return len(self.m)

    @property
    def cols(self):
        if self.rows == 0:
            return 0
        else:
            return len(self.m[0])            

    def __toss(self, m):
        mat = m
        if matrix.ss != 0:
            a = lambda x: x % matrix.ss
            b = lambda x: list(map(a, x))
            mat = list(map(b, m))
        return mat
            
    def row(self, index):
        self.m = self.__toss(self.m)
        if len(self.m) > index:
            return self.m[index]
        
    def col(self, index):
        self.m = self.__toss(self.m)
        return list(map(lambda x: x[index], self.m))
    
    def transpose(self):
        n = matrix()
        for i in range(len(self.m[0])):
            n.m.append(self.col(i))
        return n
    
    def __sq(self):
        l = len(self.m)
        for i in self.m:
            if len(i) != l:
                return False
        return True
    
    def __str__(self):
        self.m = self.__toss(self.m)
        s = ""
        for i in self.m:
            for j in i:
                s += str(j) + ' '
            s += '\n'
        return s
    
    def minor(self, x, y):
        mat = self.m[:y] + self.m[y+1:]
        mat = list(map(lambda a: a[:x] + a[x+1:], mat))
        n = matrix()
        n.m = mat
        return n

    def mminor(self, xs, ys):
        mat = self.m
        if (len(ys)>0):
            mat = self.m[:ys[0]]
            for i in range(len(ys)-1):
                mat = mat + self.m[ys[i]+1:ys[i+1]]
            mat = mat + self.m[ys[len(ys)-1]+1:]
        if (len(xs)>0):
            xs = [-1] + xs
            for i in range(len(mat)):
                nat = []
                for j in range(len(xs)-1):
                    nat += mat[i][xs[j]+1:xs[j+1]]
                nat += mat[i][xs[len(xs)-1]+1:]
                mat[i] = nat
        n = matrix()
        n.m = mat
        return n

    def rank(self):
        nul = True
        for i in self.m:
            for j in i:
                if j != 0:
                    nul = False
                    break
        if nul:
            return 0
        #for n in range(2, min(self.rows, self.cols)):
            

        
    
    def det(self):
        if not self.__sq:
            raise ValueError("Matrix is not square")
        if len(self.m) == 1:
            return self.m[0][0]
        else:
            res = 0
            for i in range(len(self.m)):
                res += (((-1)**i) * self.m[0][i] * self.minor(i,0).det())
            if matrix.ss != 0:
                res %= matrix.ss
            return res
    def __neg__(self):
        n = self * (-1)
        n.m = self.__toss(n.m)
        return n
        
    def __mul__(self, num):
        if isinstance(num, matrix):
            return self.__mulmat(num)
        else:
            a = lambda x: list(map(lambda y: num * y, x))
            b = self.__toss(list(map(a, self.m)))
            newm = matrix(b)
            return newm
        
    def __mulmat(self, other):
        if self.cols != other.rows:
            raise ValueError("Wrong matrix sizes")
        n = []
        nn = []
        for j in range(self.rows):
            for i in range(other.cols):
                nnn = 0
                for k in range(self.cols):
                    nnn += (self[j][k] * other[k][i])
                nn.append(nnn)
            n.append(nn)
            nn = []
        newm = matrix(self.__toss(n))
        return newm
    
    def __truediv__(self, num):
        a = lambda x: list(map(lambda y: y/num, x))
        b = list(map(a, self.m))
        newm = matrix(self.__toss(b))
        return newm
    
    def __rmul__(self, num):
        return self * num

    def __pow__(self,num):
        num = floor(num)
        a = self
        if not self.__sq():
            raise ValueError("Matrix has to be square")
        for i in range(1, num):
            a *= self
        return a
    
    def __add__(self, other):
        if (len(self.m) != len(other.m)):
            raise ValueError("Matricies have different dimensions")
        n = []
        for i in range(len(self.m)):
            if len(self.m[i]) != len(other.m[i]):
                raise ValueError("Matricies have different dimensions")
            else:
                nn = []
                for j in range(len(self.m[i])):
                    nn.append(self.m[i][j] + other.m[i][j])
                n.append(nn)
        newm = matrix(self.__toss(n))
        return newm
    
    def __sub__(self, other):
        if (len(self.m) != len(other.m)):
            raise ValueError("Matricies have different dimensions")
        n = []
        for i in range(len(self.m)):
            if len(self.m[i]) != len(other.m[i]):
                raise ValueError("Matricies have different dimensions")
            else:
                nn = []
                for j in range(len(self.m[i])):
                    nn.append(self.m[i][j] - other.m[i][j])
                n.append(nn)
        newm = matrix(self.__toss(n))
        return newm
    def __invert__(self):
        d = self.det()
        if d == 0:
            raise ValueError("Matrix is not invertable (det == 0)")
        if not self.__sq():
            raise ValueError("Matrix is not square")
        adj = []
        a = []
        for i in range(self.cols):
            for j in range(self.rows):
              a.append((-1)**(i+j) * self.minor(i,j).det())
            adj.append(a)
            a = []
        adj = matrix(adj)
        adj = adj/d
        if matrix.ss != 0:
            adj.m = self.__toss(adj.m)
        return adj
    
    def __getitem__(self, index):
        return self.m[index]

a = matrix([[1,5],[2,2]])
#matrix.ss = 6
print(a)
print(~a)
print(a*~a)

s = matrix([[1,2,3],[4,3,5],[54,3,2]])
print(s)
print(s.mminor([1],[2]))
m = matrix([[0,0,0],[0,0,0]])
print(m.rank())

