def addRoundKey(textBlock, wList):
    
    w = wList.copy()
    
    w = [[int(b, 16) for b in a] for a in w]
    
    # print(w)
    
    matrix = textBlock.copy()
    
    matrix = [[int(a, 16) for a in b] for b in matrix]
    
    # print(matrix)
    
    for i in range(4):
        for j in range(4):
            matrix[i][j] = matrix[i][j] ^ w[i][j]
            
   
    
    return matrix



matrix = addRoundKey(textBlock, wList)