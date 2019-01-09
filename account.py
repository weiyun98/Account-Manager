#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
from functools import reduce


def str2float(s):
    def fn(x,y):
        return x*10+y
    n = s.index('.')

    s1=list(map(int,[x for x in s[:n]]))
    s2=list(map(int,[x for x in s[n+1:]]))
    return reduce(fn,s1)+reduce(fn,s2)/(10**len(s2))


def nowtime():
    ticks = time.localtime(time.time())
    return str(ticks.tm_year)+'年'+str(ticks.tm_mon)+'月'+str(ticks.tm_mday)+'日'


if __name__ == '__main__':
    while True:
        price = input("请输入价钱：")
        if price == 'exit':
            exit()
        elif price =='query':
            fileSum = open("Sum.txt",'r')
            sum = str2float(fileSum.readline().rstrip('\n'))
            print (sum)
            fileSum.close()
            continue
        event = input("请输入事件：")

        file = open("account.txt",'a+',encoding='UTF-8')
        fileSum = open("Sum.txt",'r+')
        sum = str2float(fileSum.readline().rstrip('\n'))
        sum += float(price)
        file.write(str(float(price)))
        file.write('\t'+event+'\t'+nowtime()+'\n')
        fileSum = open("Sum.txt",'w')
        fileSum.write(str(sum))
        file.close()
        fileSum.close()
