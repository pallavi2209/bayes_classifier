import sys
import os
import glob
def main():
  folder=sys.argv[1]
  outFile=open(sys.argv[2],'w')
  listFiles=glob.glob(str(folder)+"/*.txt")
  sortedList=sorted(listFiles)
#  print(sortedList)
  for file in sortedList:
    mylist=file.split(".")
    fileList=mylist[0].split("/")
    fileName=fileList[len(fileList)-1]
    #print(fileName)
    outFile.write(fileName+" ")
    inFile=open(file,'r',errors='ignore')
    data=inFile.read()
    outFile.write(data.replace('\n',' '))
    outFile.write('\n')
  inFile.close()
  outFile.close()
if __name__=="__main__":
  main()

