# matrix addition on list elements

mat1 = [[1,2,3],[1,2,3,],[1,2,3]]
mat2 = [[1,2,3],[1,1,1],[2,2,2]]
sum_mat = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(mat1)):
    for j in range(len(mat2)):
        sum_mat[i][j] = mat1[i][j] + mat2[i][j]

for k in sum_mat:
    print(k)