"""
Software ------main <---input
           \     ↓
            \___run
        放入      ↓
头文件  <----- function

"""

from datetime import datetime
import disp_num
import MD5
import turtle_test
import textcheck
import MatchAnalysis
import webcrawler
import grammarcheck
def hw1():
    while(1):
        print("1.绘图程序\n")
        turtle_test.drawCharacter()
        break
def hw2():
    print("2.哈希函数\n")
    MD5.hashMD5()
def hw3():
    while(1):
        print("3.7段数码管显示\n"
              " 0.返回上一级\n"
              " 1.显示输入的时间\n"
              " 2.显示当前系统时间\n"
              " 3.显示数字\n"
              )
        try:hwNum = input("输入功能序号：")
        except:
            print("输入错误")
            break
        if hwNum == '0': break
        elif hwNum == '1':
            print(" 1.显示输入的时间\n")
            disp_num.dispDate(input("输入时间：Y-m=d+"))
        elif hwNum == '2':
            print(" 2.显示当前系统时间\n")
            disp_num.dispDate(datetime.now().strftime('%Y-%m=%d+'))
        elif hwNum == '3':
            print(" 3.显示数字\n")
            disp_num.dispDigit()
        elif hwNum == '4':
            print(" 4.更改字体\n")
            try:
                disp_num.fort = input("输入字体名称：")
            except:
                print("字体名称输入错误")
        else: print("输入序号错误")
def hw4():
    print("4.保留字符\n")
    textcheck.findKeyword()

def hw5():
    print("5.比赛模拟\n")
    MatchAnalysis.matchAnalysis()

def hw6():
    print("6.网络爬虫\n")
    webcrawler.crawlVideo()

def hw7():
    print("7.语法分析\n")
    grammarcheck.grammarCheck()

def run():
    while (1):
        print("现代编程课程作业：\n"
              "0.退出程序\n"
              "1.绘图程序\n"
              "2.哈希函数\n"
              "3.7段数码管显示\n"
              "4.保留字符\n"
              "5.比赛模拟\n"
              "6.网络爬虫\n"
              "7.语法分析\n")
        try:
            hwNum = input("输入作业序号：")
        except:
            print("输入错误")
            break
        if hwNum == '0':
            break
        elif hwNum == '1':
            hw1()
        elif hwNum == '2':
            hw2()
        elif hwNum == '3':
            hw3()
        elif hwNum == '4':
            hw4()
        elif hwNum == '5':
            hw5()
        elif hwNum == '6':
            hw6()
        elif hwNum == '7':
            hw7()
        else:
            print("输入错误")

if __name__ == "__main__":
    run()

