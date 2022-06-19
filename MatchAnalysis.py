
from random import random
def printIntro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0到1之间的小数表示）")


def getInputs():
    a = eval(input("请输入选手A的能力值(0-1): "))
    b = eval(input("请输入选手B的能力值(0-1): "))
    n = eval(input("模拟比赛的场次: "))
    missa = eval(input("请输入选手A的失误率(0-1): "))
    missb = eval(input("请输入选手B的失误率(0-1): "))
    wa = eval(input("请输入选手A优势天气(1,2,3): "))
    wb = eval(input("请输入选手B优势天气(1,2,3): "))
    w = eval(input("请输入当前天气(1,2,3): "))
    return a, b, n, missa, missb, wa, wb, w


def realprob(probA, probB, weathera, weatherb,weather):
    realprobA, realprobB = 0,0
    if(weather == weathera):
        realprobA = 1.2*probA
    else:
        realprobA = probA
    if (weather == weatherb):
        realprobB = 1.2 * probB
    else:
        realprobB = probB

    return realprobA,realprobB


def simNGames(n, probA, probB, missa, missb, weathera, weatherb, weather):
    winsA, winsB = 0, 0
    realprobA,realprobB=realprob(probA, probB, weathera, weatherb, weather)
    for i in range(n):
        scoreA, scoreB = simOneGame(realprobA, realprobB, missa, missb)
        print("one game")
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB


def gameOver(a,b):
    return a==15 or b==15


def islegalbeat(miss):
    if random() > miss:
        return 1
    else: return 0


def simOneGame(probA, probB, missa, missb):
    scoreA, scoreB = 0, 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if (random() < probA and islegalbeat(missa)):
                scoreA += 1
            else:
                serving="B"
        else:
            if (random() < probB and islegalbeat(missb)):
                scoreB += 1
            else:
                serving="A"
    return scoreA, scoreB
def printSummary(winsA, winsB):
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA, winsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB, winsB/n))
def matchAnalysis():
    printIntro()
    probA, probB, n, missa, missb, weathera, weatherb, weather = getInputs()
    winsA, winsB = simNGames(n, probA, probB,  missa, missb, weathera, weatherb, weather)
    printSummary(winsA, winsB)

if __name__ == '__main__':
    matchAnalysis()
