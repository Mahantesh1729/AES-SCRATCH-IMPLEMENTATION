from inputTransformation import InputTransformation


class InvSubBytes:
    subFile = open('invSubByte.txt')
    invSubBytes = list(subFile)
    invSubBytes = [row.replace("\n", "").split(',') for row in invSubBytes]
    
    def invSubByteTransformation(matrix):
        step_1_matrix = [[0 for j in range(4)] for i in range(4)]

        for i in range(4):
            for j in range(4):
                a = hex(matrix[i][j]).replace("0x", "")
                if len(a) == 1:
                    a = '0' + a
                step_1_matrix[i][j] = InvSubBytes.invSubBytes[int(a[0], 16)][int(a[1], 16)]
        
        return step_1_matrix
    