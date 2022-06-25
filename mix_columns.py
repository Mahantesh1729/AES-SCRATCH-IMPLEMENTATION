class MixColumns:
    
    
    def multiply(n, num):
        if type(num) != int:
            num = int(num,16)
        
        temp = bin(num)
        temp = temp.replace("0b", "")
        
        if len(temp) != 8:
            temp = '0' + temp
        
        num = num << 1
        
        # print(temp)
        
        # print(num)
        
        if temp[0] == '1':
            num = num ^ int('100011011', 2)
        
        return num
    
    def mixColumn(column):
        
        col0 = MixColumns.multiply(2, column[0]) ^ MixColumns.multiply(2, column[1]) ^ int(column[1], 16) ^ int(column[2], 16) ^ int(column[3], 16)
        
        col1 = int(column[0], 16) ^ MixColumns.multiply(2, column[1]) ^ MixColumns.multiply(2, column[2]) ^ int(column[2], 16) ^ int(column[3], 16)
        
        col2 = int(column[0], 16) ^ int(column[1], 16) ^ MixColumns.multiply(2, column[2]) ^ MixColumns.multiply(2, column[3]) ^ int(column[3], 16)
        
        col3 = int(column[0], 16) ^ MixColumns.multiply(2, column[0]) ^ int(column[1], 16) ^ int(column[2], 16) ^ MixColumns.multiply(2, column[3])
        
        return [hex(col0), hex(col1), hex(col2), hex(col3)]    
    
    
    def multiplyE(num):
        # x × 14 = ( ( ( ( x × 2 ) + x ) × 2 ) + x ) × 2
        return MixColumns.multiply(2, MixColumns.multiply(2, (MixColumns.multiply(2, num) ^ int(num, 16))) ^ int(num, 16))
    
    def multiplyB(num):
        # x × 11= ( ( ( ( x × 2 ) × 2 ) + x ) × 2 ) + x    
        return MixColumns.multiply(2, MixColumns.multiply(2, MixColumns.multiply(2, num)) ^ int(num, 16)) ^ int(num, 16)
    
    def multiplyD(num):
        # x × 13 = ( ( ( ( x × 2 ) + x ) × 2 ) × 2 ) + x
        return MixColumns.multiply(2, MixColumns.multiply(2, (MixColumns.multiply(2, num) ^ int(num, 16)))) ^ int(num, 16)
    
    def multiply9(num):
        # x × 9 = ( ( ( x × 2 ) × 2 ) × 2 ) + x
        return MixColumns.multiply(2, MixColumns.multiply(2, MixColumns.multiply(2, num))) ^ int(num, 16)
    
    def invMixColumn(column):
        col0 = MixColumns.multiplyE(column[0]) ^ MixColumns.multiplyB(column[1]) ^ MixColumns.multiplyD(column[2]) ^ MixColumns.multiply9(column[3])
        col1 = MixColumns.multiply9(column[0]) ^ MixColumns.multiplyE(column[1]) ^ MixColumns.multiplyB(column[2]) ^ MixColumns.multiplyD(column[3])
        col2 = MixColumns.multiplyD(column[0]) ^ MixColumns.multiply9(column[1]) ^ MixColumns.multiplyE(column[2]) ^ MixColumns.multiplyB(column[3]) 
        col3 = MixColumns.multiplyB(column[0]) ^ MixColumns.multiplyD(column[1]) ^ MixColumns.multiply9(column[2]) ^ MixColumns.multiplyE(column[3]) 
        
        return [col0, col1, col2, col3] 
    
    def transpose(matrix):
        
        result = [[0 for j in range(4)] for i in range(4)]
        
        for i in range(4):
            for j in range(4):
                result[i][j] = matrix[j][i]
        
        
        return result

    def multiplyMatrix(matrix):
                
        resultMatrix = []
                
        for i in range(4):
            column = []
            for j in range(4):
                column.append(matrix[j][i])
            column = MixColumns.mixColumn(column)
            resultMatrix.append(column)
            
        resultMatrix = MixColumns.transpose(resultMatrix)
        
        return resultMatrix
    
    
    
    def invMultiplyMatrix(matrix):
        resultMatrix = []
        for i in range(4):
            column = []
            for j in range(4):
                column.append(matrix[j][i])
            column = MixColumns.invMixColumn(column)
            resultMatrix.append(column)
            
        resultMatrix = MixColumns.transpose(resultMatrix)
        
        return resultMatrix
            
# print(MixColumns.multiply(2, 'f2'))

# print(MixColumns.mixColumn(['63', 'f2', '7d', 'd4']))

# print(MixColumns.multiplyMatrix([['3f', '8a', 'df', '77'], ['ea', '84', 'd1', '48'], ['1', '51', '36', 'fa'], ['81', '9d', '8f', '48']]))


