from os import listdir
from os.path import isfile, join


resultData = 'DataRemains\\ResultData.txt'

def readFile(getfile):
    f = open(getfile,'r')
    fout = f.read()
    f.close()
    return fout

def writeFile(outStr,outfile):
    outStr = '\n'.join(outStr)
    f = open(outfile,'w')
    f.write(outStr)
    f.close()

outStr = readFile(resultData)
line = [i for i in outStr.split('\n')]
line.pop()
s = 0
mid = len(line)//4
m = mid
for i in range(1,4):
    writeFile(line[s:m],'Project_I'+str(i)+'\\'+resultData)
    s = m
    m = m+mid
writeFile(line[s:],'Project_I4\\'+resultData)




