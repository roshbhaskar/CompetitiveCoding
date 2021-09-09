'''
Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

TC : O(N*M)

'''

def spiral(matrix):
        result=[]
        top=0
        left=0
        down=len(matrix)-1
        right=len(matrix[0])-1
        dir_=0
        while(top<=down and left<=right):
            if(dir_==0):
                for i in range(left,right+1):
                    result.append(matrix[top][i])
                top+=1
            elif(dir_==1):
                for i in range(top,down+1):
                    print(i,right,matrix[i])
                    result.append(matrix[i][right])
                right-=1
            elif(dir_==2):
                for i in range(right,left-1,-1):
                    result.append(matrix[down][i])
                down-=1
            elif(dir_==3):
                for i in range(down,top-1,-1):
                    result.append(matrix[i][left])
                left+=1
            dir_=(dir_+1)%4
        return result
            
print(spiral([[1,2,3],[4,5,6],[7,8,9]]))