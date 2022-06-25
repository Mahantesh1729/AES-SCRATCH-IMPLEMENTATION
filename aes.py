from subBytes import SubBytes
from inputTransformation import InputTransformation
from permutation import Permutation
from keyGenerator import KeyGenerator
from mix_columns import MixColumns

def inputPlainText():
    print("Enter the plain text: ", end=" ")
    return input()

def cipherKeyInput():
    print("Enter the cipher key: ", end="")
    return input().split(" ")

def generateRowColumnMatrix(data):
    matrix = [[0 for j in range(4)] for i in range(4)]
    length = len(data)
    k = 0
    for i in range(4):
        for j in range(4):
            if length > 0:
                length -= 1
                matrix[j][i] = data[k]
                k += 1
            else:
                matrix[j][i] = [7, 10]
    
    return matrix

def generateMatrix(ascii_list):
    matrix = [[0 for j in range(4)] for i in range(4)]
    length = len(ascii_list)
    k = 0
    for i in range(4):
        for j in range(4):
            if length > 0:
                length -= 1
                matrix[j][i] = ascii_list[k]
                k += 1
            else:
                matrix[j][i] = '7a'
    
    return matrix


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

def transpose(wMatrix):
    matrix = [[0 for j in range(4)] for i in range(4)]
    
    for i in range(4):
        for j in range(4):
            matrix[i][j] = wMatrix[j][i]
            
    return matrix


def enCipher(plainTextBlock, wList):
    
    matrix = plainTextBlock.copy()
    # print(wList)
    
    w = transpose(wList[0:4])
    
    # print(matrix)
    
    matrix = addRoundKey(matrix, w)
    
    # print(matrix)
    
    # print("hello wolr")
    
    for i in range(1, 11):
        matrix = SubBytes.subByteTransformation(matrix)
        # print(matrix)
        matrix = Permutation.shiftRows(matrix)
        # print(matrix)
        
        if i  != 10:
            matrix = MixColumns.multiplyMatrix(matrix)
        
        w = transpose(wList[(i * 4) : (i + 1) * 4])
    
        matrix = addRoundKey(matrix, w)
        
        # print(matrix)
    
    for i in matrix:
        print(i)

        










plain_text = inputPlainText()
cipher_key = cipherKeyInput()

wList = KeyGenerator.generateKey(cipher_key)


ascii_row_column = InputTransformation.toAsciiRowColumn(plain_text)

ascii_list = InputTransformation.toAsciiList(plain_text)


# print(ascii_list)

asciiMatrix = generateMatrix(ascii_list)


testMatrix = generateMatrix(['00', '04', '12', '14', '12', '04', '12', '00','0c','00','13','11','8','23','19', '19'])
# ['00', '04', '12', '14', '12', '04', '12', '00','0c','00','13','11','8','23','19', '19']

print("Generated Cipher text for entered plain text is: ")

enCipher(asciiMatrix, wList)


testMatrix1 = generateMatrix(['00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',])

testMatrix2 = generateMatrix(['00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '01',])

print()

print("Generated cipher matrix for first test plain text 1")

enCipher(testMatrix1, wList)
print()

print("Generated cipher matrix for first test plain text 2")
enCipher(testMatrix2, wList)
# matrix = generateRowColumnMatrix(ascii_row_column)


# print(plain_text)

# enCipher(matrix)

# print(matrix)

# step1 = SubBytes.subByteTransformation(matrix)

# print()

# print(step1)

# step1 = Permutation.shiftRows(step1)

# print(step1)

# print(SubBytes.subBytes)