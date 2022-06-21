class MixColumns:
    
    
    def multiply(n, num):
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
            print(column)
            column = MixColumns.mixColumn(column)
            resultMatrix.append(column)
            
        resultMatrix = MixColumns.transpose(resultMatrix)
        
        return resultMatrix
            
# print(MixColumns.multiply(2, 'f2'))

print(MixColumns.mixColumn(['63', 'f2', '7d', 'd4']))

print(MixColumns.multiplyMatrix([
    ['63', 'c9', 'fe', '30'],
    ['f2', '63', '26', 'f2'],
    ['7d', 'd4', 'c9', 'c9'],
    ['d4', 'fa', '63', '82']
]))
                