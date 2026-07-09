class Solution(object):
    def setZeroes_better(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])
        rowlist=[0]*r
        collist=[0]*c
        for i in range(r):
            for j in range(c):
                if(matrix[i][j]==0):
                    rowlist[i]=1
                    collist[j]=1

        for i in range(r):
            for j in range(c):
                if(matrix[i][j]!=0 and (rowlist[i]==1 or collist[j]==1 )):
                    matrix[i][j]=0

    def setZeroes_optimal(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])
        # rowlist=[0]*r ---> matrix[i][0]
        # collist=[0]*c ---> matrix[0][j]
        col0=1
        for i in range(r):
            for j in range(c):
                if(matrix[i][j]==0):
                    matrix[i][0]=0
                    if(j==0):
                        col0=0
                    else:
                        matrix[0][j]=0

        for i in range(1,r):
            for j in range(1,c):
                if(matrix[i][j]!=0 and (matrix[i][0]==0 or matrix[0][j]==0)):
                    matrix[i][j]=0

        for i in range(1,c):
            if(matrix[0][i]!=0 and matrix[0][0]==0):
                matrix[0][i]=0   
        for i in range(0,r):
            if(matrix[i][0]!=0 and col0==0):
                matrix[i][0]=0                                  
                               



        
