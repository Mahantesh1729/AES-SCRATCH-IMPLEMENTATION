from subBytes import SubBytes
from inputTransformation import InputTransformation
from permutation import Permutation

def inputPlainText():
    print("Enter the plain text: ", end=" ")
    return input()

def generateMatrix(data):
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

plain_text = inputPlainText()

# print(plain_text)

ascii_row_column = InputTransformation.toAscii(plain_text)

matrix = generateMatrix(ascii_row_column)
print(matrix)

step1 = SubBytes.subByteTransformation(matrix)

print()

print(step1)

step1 = Permutation.shiftRows(step1)

print(step1)

# print(SubBytes.subBytes)