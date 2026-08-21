matrix=[]
for i in range(1,11) :
    row = []
    for j in range(1,11) :
        row.append(i*j)
    matrix.append(row) 
for row in matrix :
    for number in row :
        print(f'{number:4}', end='')
    print()
