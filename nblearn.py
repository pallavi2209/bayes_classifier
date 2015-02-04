import sys
import re
import pickle
import math
import string
def main():
  arg1=sys.argv[1]
  arg2=sys.argv[2]
  reStr=re.compile(r' +')
  trfile=open(arg1,'r')
  mainDict={}
  uniqW=set()
  for line in trfile:
    for c in string.punctuation:
      line=line.replace(c," ")
    line=line.lower()
    reStr.sub(' ',line)
    wordsList=line.split()
    strClass=wordsList[0].upper()
    if strClass not in mainDict:	
      mainDict[strClass]=({},0,0)
    cDict,cntClass,cntTokens=mainDict[strClass]
    cntClass=cntClass+1;
    for i in range(1,len(wordsList)):
      cntTokens=cntTokens+1
      key=wordsList[i]
      uniqW.add(key)
      if key in cDict:
        cDict[key]=cDict[key]+1
      else:
        cDict[key]=1
    mainDict[strClass]=cDict,cntClass,cntTokens
  uniqW.add("<unknownUNK>")
  totUniqW=len(uniqW)
  totClsCnt=0;
  for x,y,z in mainDict.values():
    totClsCnt=totClsCnt+y;
  
  pDict={}
  for token in uniqW:
    if token not in pDict:
      pDict[token]={}
    pClsDict=pDict[token]
    for k,v in mainDict.items():
      cToken=1
      if token in v[0]:
        cToken=cToken+v[0][token]
      pToken=math.log(cToken)-math.log(v[2]+totUniqW)
      pClsDict[k]=pToken

  pClassDict={}
  for x,y in mainDict.items():
    pX=math.log(y[1])-math.log(totClsCnt)
    pClassDict[x]=pX

  dictModel=dict(pDict=pDict, pClassDict=pClassDict)
  with open(arg2,"wb") as handle:
    pickle.dump(dictModel,handle)
  trfile.close()
  handle.close()    
 # print(dictModel)  
if __name__=="__main__":
  main()
