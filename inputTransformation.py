class InputTransformation:
    
    def toAscii(text):
        return [[int(hex(ord(i))[2], 16), int(hex(ord(i))[3], 16)] for i in text]
    