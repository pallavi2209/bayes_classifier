import sys
import os
import glob
def main():
  folder=sys.argv[1]
  outFile=open(sys.argv[2],'w')
  listFiles=glob.glob(str(folder)+"*.txt")
  sortedList=sorted(listFiles)
#  print(sortedList)
  for file in sortedList:
    inFile=open(file,'r',errors='ignore')
    data=inFile.read()
    outFile.write(data.replace('\n',' '))
    outFile.write('\n')

if __name__=="__main__":
  main()
