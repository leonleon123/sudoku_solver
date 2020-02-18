import sys, math
class SudokuSolver:
    def __init__(self, filename):
        with open(filename) as file:
            self.data = [list(map(int, x.replace("\n", "").split(" "))) for x in file.readlines()]
        self.n = len(self.data)
        self.q_size = int(math.sqrt(self.n))
        self.solve(0,0)

    def check_row(self, i, j):
        tmp = [x for x in self.data[i] if x != 0]
        return len(set(tmp)) == len(tmp)

    def check_col(self, i, j):
        tmp = [self.data[x][j] for x in range(self.n) if self.data[x][j] != 0]
        return len(set(tmp)) == len(tmp)

    def check_quadrant(self, i, j):
        tmp = []
        i_offset, j_offset = int(i/self.q_size)*self.q_size, int(j/self.q_size)*self.q_size
        for ii in range(i_offset, i_offset + self.q_size):
            for jj in range(j_offset, j_offset + self.q_size):
                if self.data[ii][jj] != 0: tmp.append(self.data[ii][jj])
        return len(set(tmp)) == len(tmp)

    def check_all(self,i,j):
        return self.check_row(i,j) and self.check_quadrant(i,j) and self.check_col(i,j)

    def finish(self):
        return all(all(el!=0 for el in row) for row in self.data)

    def solve(self, i, j):
        if i >= self.n: return
        if self.data[i][j] > 0: 
            return self.solve(i + int((j+1) % self.n == 0), (j+1) % self.n)
        for num in range(1,self.n+1):
            self.data[i][j] = num
            if self.check_all(i,j):
                if self.finish():
                    print(*[" ".join(list(map(str, x))) for x in self.data], sep="\n",end="\n\n")
                self.solve(i + int((j+1) % self.n == 0), (j+1) % self.n)
            self.data[i][j] = 0
            
SudokuSolver(sys.argv[1])