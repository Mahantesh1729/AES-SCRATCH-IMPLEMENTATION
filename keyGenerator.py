from subBytes import SubBytes

class KeyGenerator:

    def add(w1, w2):
        w1 = [int(a, 16) for a in w1]
        w2 = [int(a, 16) for a in w2]
        
        wResult = []
        
        for i in range(4):
            w = w1[i] ^ w2[i]
            w = hex(w).replace("0x", "")
            if len(w) == 1:
                w = '0' + w
            wResult.append(w)
        
        return wResult


    def RotWord(w1):
        w = w1.copy()
        temp = w[0]
        
        for i in range(1, 4):
            w[i - 1] = w[i]
            
        w[3] = temp
        
        return w

    def RCon(round):
        RConDict = {
            1: ['01', '00', '00', '00'],
            2: ['02', '00', '00', '00'],
            3: ['04', '00', '00', '00'],
            4: ['08', '00', '00', '00'],
            5: ['10', '00', '00', '00'],
            6: ['20', '00', '00', '00'],
            7: ['40', '00', '00', '00'],
            8: ['80', '00', '00', '00'],
            9: ['1b', '00', '00', '00'],
            10:['36', '00', '00', '00']
        }
        
        return RConDict[round]
    
    
    

    def generateKey(keyList):
        w_keys = []
        
        for i in range(4):
            w = keyList[i * 4: (i + 1) * 4]
            w_keys.append(w)
        
        for i in range(4, 44):
            
            if i % 4 != 0:
                w = KeyGenerator.add(w_keys[i - 1], w_keys[i - 4])
                w_keys.append(w)
            else:
                t = KeyGenerator.add(SubBytes.subWord(KeyGenerator.RotWord(w_keys[i - 1])), KeyGenerator.RCon(i / 4))
                # break
                w = KeyGenerator.add(t, w_keys[i - 4])
                w_keys.append(w)
            
        return w_keys



keys = KeyGenerator.generateKey(["24", "75", "a2", "b3", "34", "75", "56", "88", "31", "e2", "12", "00", "13", "aa", "54", "87"])

# print(keys)





# print("Enter the key for communication")

# keyList = input().split(' ')

# print(keyList)