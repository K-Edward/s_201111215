
def getKey(keyPath):
    key = dict()
    f = open(keyPath,'r')
    
    for line in f.readlines():
        row = line.split('=')
        key[row[0]] = row[1].strip()
        
    return key