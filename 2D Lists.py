<<<<<<< HEAD
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][0])
print(matrix[1][2])
print("--------------------------------------------------")
for row in matrix: #print each row in the matrix
    for value in row: #print each value in the row
        print(value)

print("--------------------------------------------------")
for i in range(len(matrix)):
    for j in range(len(matrix[i])): #print the indices and values of each element in the matrix
=======
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][0])
print(matrix[1][2])
print("--------------------------------------------------")
for row in matrix: #print each row in the matrix
    for value in row: #print each value in the row
        print(value)

print("--------------------------------------------------")
for i in range(len(matrix)):
    for j in range(len(matrix[i])): #print the indices and values of each element in the matrix
>>>>>>> 0981ad8685c870ca7bf0ce4be72d496e180f8ead
        print(matrix[i][j])