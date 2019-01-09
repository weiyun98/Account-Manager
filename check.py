#!E:\python\Lib\idlelib\idle.pyw
# -*- coding: UTF-8 -*-
from account import str2float


def readStr(s):
    n=0
    while s[n]!='\t':
        n += 1
    return s[:n]


file = open("account.txt",'r',encoding='UTF-8')
fileSum = open("Sum.txt",'r')

sum = str2float(fileSum.readline().rstrip('\n'))
num = 0.0
for line in file.readlines():
        num += str2float(readStr(line))

if num == sum:
    print ("check ok.")
else:
    print("There are some things wrong here.")
file.close()
fileSum.close()
input()
