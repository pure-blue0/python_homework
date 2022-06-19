# coding: utf-8
import string
import keyword
import re

keywords= keyword.kwlist
signList = {}
if_cnt, try_cnt = 0, 0
forFlag, ifFlag, tryFlag, elifFlag, elseFlag, exceptFlag = 0, 0, 0, 0, 0, 0
line_num = 0
def grammarCheck():
    global if_cnt,try_cnt,forFlag, ifFlag, tryFlag, elifFlag, elseFlag, exceptFlag, line_num
    fileName=input("输入文件名称:")
    try:
        pyFile = open(fileName,"r",encoding='utf-8')
    except:
        print("文件名称错误")
        return 0
    text = pyFile.read()
    lines = text.splitlines()
    for line in lines:
        line_num = lines.index(line)
        if re.findall (r"for ",line) != []:
            forFlag += checkfor(line)
        if re.findall (r"if ",line) != []:
            if re.findall(r"elif ", line) != []:
                elifFlag += checkelif(line)
            else:
                ifFlag += checkif(line)
        if re.findall(r"else", line) != []:
            elseFlag += checkelse(line)
        if re.findall(r"try", line) != []:
            tryFlag+=checktry(line)
        if re.findall(r"expect ", line) != []:
            exceptFlag+=checkexcept(line)
    if(forFlag+ifFlag+tryFlag+elifFlag+elseFlag+exceptFlag)==0:
        print("no error")
    else:
        print("for:",forFlag)
        print("if:", ifFlag)
        print("else:", elseFlag)
        print("elif:",elifFlag)
        print("try:", tryFlag)
        print("except:", exceptFlag)



    #     print("line=",words)
    # print(signList)

def checkfor(line):
    global line_num
    findflag = re.match (r" *for (.*?) in (.*?):",line)
    if findflag != None:
        return 0
    else:
        print("for Error in Line {}:{}".format(line_num,line))
        return 1

def checkif(line):
    global line_num, if_cnt
    if_cnt += 1
    findflag = re.match (r" *if (.*?):",line)
    if findflag != None:
        return 0
    else:
        print("if Error in Line {}:{}".format(line_num,line))
        return 1

def checkelif(line):
    global line_num, if_cnt
    findflag = re.match (r" *elif (.*?):",line)
    if (findflag != None) and (if_cnt > 0) :
        return 0
    else:
        print("elif Error in Line {}:{}".format(line_num,line))
        return 1

def checkelse(line):
    global line_num, if_cnt

    findflag = re.match (r" *else *:",line)
    if (findflag != None) and (if_cnt > 0) :
        if_cnt -= 1
        return 0
    else:
        print("else Error in Line {}:{}".format(line_num,line))
        if_cnt -= 1
        return 1

def checktry(line):
    global line_num, try_cnt
    try_cnt += 1
    findflag = re.match (r" *try *:",line)
    if findflag != None:
        return 0
    else:
        print("try Error in Line {}:{}".format(line_num,line))
        return 1

def checkexcept(line):
    global line_num, try_cnt
    findflag = re.match (r" *except (.*?):",line)
    if (findflag != None) and (try_cnt > 0):
        try_cnt -= 1
        return 0
    else:
        try_cnt -= 1
        print("except Error in Line {}:{}".format(line_num,line))
        return 1

if __name__ == "__main__":
    grammarCheck()




