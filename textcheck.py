# coding: utf-8
import string
import keyword
import re

keywords= keyword.kwlist
signList = {}
def findKeyword():
    fileName=input("输入文件名称:")
    try:
        pyFile = open(fileName,"r",encoding='utf-8')
    except:
        print("文件名称错误")
        return 0
    text = pyFile.read()
    lines = text.splitlines()
    for line in lines:
        for ch in line:
            if ch in string.punctuation:
                line = line.replace(ch, " ")
        words =line.split()
        for word in words:
            if( word in keywords) and (word not in signList):
                signList[word] = 1
            if (word in keywords) and (word in signList):
                signList[word] += 1
        print("line=",line)
    print(signList)

if __name__ == "__main__":
    findKeyword()

