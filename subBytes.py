from inputTransformation import InputTransformation


class SubBytes:
    subFile = open('subByte.txt')
    subBytes = list(subFile)
    subBytes = [row.replace("\n", "").split(',') for row in subBytes]
    
    def subByteTransformation(matrix):
        step_1_matrix = [[0 for j in range(4)] for i in range(4)]

        for i in range(4):
            for j in range(4):
                a = hex(matrix[i][j]).replace("0x", "")
                if len(a) == 1:
                    a = '0' + a
                step_1_matrix[i][j] = SubBytes.subBytes[int(a[0], 16)][int(a[1], 16)]
        
        return step_1_matrix
    
    def subWord(w):
        result = []
        
        for i in range(4):
            result.append(SubBytes.subBytes[int(w[i][0], 16)][int(w[i][1], 16)])
            
        return result    