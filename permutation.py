class Permutation:
    
    def leftShift(row, count):
        
        for i in range(count):
            temp = row[0]
            j = 1
            while j != 4:
                row[j - 1] = row[j]
                j += 1
            row[j - 1] = temp
                
        return row
    
    
    def shiftRows(matrix):
        
        for i in range(1, 4):
            matrix[i] = Permutation.leftShift(matrix[i], i)
        
        
        return matrix
        