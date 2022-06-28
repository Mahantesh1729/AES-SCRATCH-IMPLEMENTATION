from subBytes import SubBytes
from invSubBytes import InvSubBytes
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

def generateMatrix(alist):
    matrix = [[0 for j in range(4)] for i in range(4)]
    length = len(alist)
    k = 0
    for i in range(4):
        for j in range(4):
            if length > 0:
                length -= 1
                matrix[j][i] = alist[k]
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
    
    dummyW = [[j for j in i] for i in w]
        
    print("round key", 0,"is: ")
    print(dummyW)
    
    # print(matrix)
    
    matrix = addRoundKey(matrix, w)
    
    # print(matrix)
    
    # print("hello wolr")
    
    for i in range(1, 11):
        matrix = SubBytes.subByteTransformation(matrix)
        print()
        print("After substitution")
        print(matrix)
        print()
        matrix = Permutation.shiftRows(matrix)
        print("After permutation")
        print(matrix)
        
        if i  != 10:
            matrix = MixColumns.multiplyMatrix(matrix)
            print()
            print("After Mix Columns")
            print(matrix)
        
        w = transpose(wList[(i * 4) : (i + 1) * 4])
        
        dummyW = [[j for j in i] for i in w]
        
        
        print()
        print("round key", i,"is: ")
        print(dummyW)

        
        
        matrix = addRoundKey(matrix, w)
        print()
        print("After add round key")
        print(matrix)
        print()
    
    for i in matrix:
        print(i)

        










plain_text = inputPlainText()
cipher_key = cipherKeyInput()

wList = KeyGenerator.generateKey(cipher_key)

# print(wList)

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

# print("Generated cipher matrix for first test plain text 1")

# enCipher(testMatrix1, wList)
# print()

# print("Generated cipher matrix for first test plain text 2")
# enCipher(testMatrix2, wList)
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


# ###############################################################################################################
###################### decryption begins from here ######################



def deCipher(cipherTextMatrix, wList):
    
    matrix = cipherTextMatrix.copy()
    
    w = wList[0:4].copy()
    
    w.reverse()
    
    w = transpose(w)
    
    
    dummyW = [[j for j in i] for i in w]
        
    print("round key", 0,"is: ")
    print(dummyW)

    matrix = addRoundKey(matrix, w)
    
    dummyMatrix = matrix.copy()
    
    dummyMatrix = [[hex(j).replace("0x", "") for j in i] for i in dummyMatrix]
    
    for i in dummyMatrix:
            print(i)
    
    print()
    
    for i in range(1, 11):

        matrix = Permutation.invShiftRows(matrix)
        
        print("After invShiftRows")
        print(matrix)
        print()
        
        matrix = InvSubBytes.invSubByteTransformation(matrix)
        
        print("After substitution")
        print(matrix)
        
        w = wList[(i * 4) : (i + 1) * 4]
        
        w.reverse()
        
        w = transpose(w)
        
        dummyW = [[j for j in i] for i in w]
            
        matrix = addRoundKey(matrix, w)
        matrix = [[hex(j).replace("0x", "") for j in i] for i in matrix]
        
        dummyW = [[j for j in i] for i in w]
        
        print("round key", i,"is: ")
        print(dummyW)
        if i  != 10:
            dummyMatrix = matrix.copy()
    
            for i in dummyMatrix:
                    print(i)
            print()
            matrix = MixColumns.invMultiplyMatrix(matrix)
            
            print("after mixColumns")
            print(matrix)
        else:
            for i in matrix:
                    print(i)
            print()
        # break
        
            
    print()
    # print(matrix)

    for i in matrix:
        for j in i:
            print(chr(int(j, 16)), end=" ")
        print()
    print()
    
    

# the first step in decryption is to reverse the generated key

wList.reverse()
# print(wList)
# print(len(wList))

print("Enter the cipher text to be decrypted: ", end="")

# cipherText = [hex(int(i)).replace("0x", "") for i in input().split(" ")]
cipherText = [ i for i in input().split(" ")]

# same function has been used for both plain and cipher text to generateMatrix

cipherTextMatrix = generateMatrix(cipherText)

# print(cipherTextMatrix)

print("Generated plain text after deciphering is: ")

# print(cipherTextMatrix)

deCipher(cipherTextMatrix, wList)