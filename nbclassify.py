import sys
import pickle
import re
import math
import string
def main():
  arg1=sys.argv[1]
  arg2=sys.argv[2]

  outFile=open("arg2","w")
  reStr=re.compile(r' +')
  with open(arg1,"rb") as handle:
    data=pickle.load(handle)

  pDict=data["pDict"]
  pClassDict=data["pClassDict"]
  testFile=open(arg2,'r')
  for line in testFile:
    for c in string.punctuation:
      line=line.replace(c," ")
    line=line.lower()
    reStr.sub(' ',line)
    wordsList=line.split()
    maxProb=float("-infinity")
    maxPClass=""
    for k,v in pClassDict.items():
      pClass=pClassDict[k]
      pDoc=pClass
      for i in range(1,len(wordsList)):
        key=wordsList[i]
        if key in pDict:
          pKey=pDict[key][k]
        else:
          pKey=pDict["<unknownUNK>"][k]
        pDoc=pDoc+pKey
     # print(str(maxProb)+"compared with "+ str(pDoc))
      if maxProb<pDoc:
        maxProb=pDoc
        maxPClass=k
    print(maxPClass)
  testFile.close()
  outFile.close()
if __name__=="__main__":
  main()
