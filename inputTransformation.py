class InputTransformation:
    
    def toAsciiRowColumn(text):
        return [[int(hex(ord(i))[2], 16), int(hex(ord(i))[3], 16)] for i in text]
    
    def toAsciiList(text):
        return [hex(ord(i)).replace("0x", "") for i in text]