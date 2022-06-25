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
    
    
    def rightShift(row, count):
        
        for i in range(count):
            temp = row[3]
            j = 2
            while j != -1:
                row[j + 1] = row[j]
                j -= 1
            
            row[0] = temp
            
        return row
    
    
    def shiftRows(matrix):
        
        for i in range(1, 4):
            matrix[i] = Permutation.leftShift(matrix[i], i)
        
        return matrix
    
    def invShiftRows(matrix):
        
        for i in range(1, 4):
            matrix[i] = Permutation.rightShift(matrix[i], i)
            
        return matrix
        
        
        
# a = [
#     [1, 2, 3, 4],
#     [1, 2, 3, 4],
#     [1, 2, 3, 4],
#     [1, 2, 3, 4],
# ]

# a = Permutation.invShiftRows(a)

# for i in a:
#     print(i)