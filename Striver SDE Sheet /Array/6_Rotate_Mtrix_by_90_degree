class Solution:
    def rotateMatrix(self, mat):
        # code here
        r=len(mat)
        c=len(mat[0])
        # anti-clockwise direction
        for i in range(r):
            mat[i][:]=mat[i][::-1]
        for i in range(r):
            for j in range(c):
                if(j>i): mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
        # clockwise direction
        for i in range(r):
            for j in range(c):
                if(j>i): mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
        for i in range(r):
                    mat[i][:]=mat[i][::-1]
