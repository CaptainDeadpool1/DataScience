
#Acquire Matrix!

matrix=[]
while True:
    try:
        s = input()
        if s != '':
            matrix.append(list(map(int, s.split())))
    except EOFError:
        break


righe = len(matrix)
colonne = len(matrix[0])

# Creating auxiliar matrix with all 0 values!
aux= [[0] * colonne for i in range(righe)]

for i in range(colonne):
    aux[0][i] = matrix[0][i]

#Column sum
for i in range(1,righe):
    for j in range(colonne):
        aux[i][j] = matrix[i][j] + aux[i-1][j]
# Rows sum
for i in range(righe):
    for j in range(1,colonne):
        aux[i][j] += aux[i][j-1]

print ('\n'.join(' '.join(str(cell) for cell in row) for row in aux))
