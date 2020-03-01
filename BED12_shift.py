#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Usage: python
# Created By Haifeng Sun, 20200301, NJMU, haifeng4432@gmail.com

import argparse
parser = argparse.ArgumentParser()

parser.add_argument("inputFile", help="input a BED12 file", type=str)
args = parser.parse_args()
input = args.inputFile

input_data = open(input, 'r')


# 正链：第一个exon长度加3bp：
def exon(string):
    num = string.count(',')
    res = str(int(string.split(',')[0])+3)
    for i in range(0,num-1):
        res = res+","+string.split(',')[i+1]
    return res+","

# 负链：最后一个exon长度加3bp:
def exon_rev(string):
    num = string.count(',')
    res = str(int(string.split(',')[num-1])+3)
    for i in range(num-2,-1,-1):
        res = string.split(',')[i]+","+res
    return res+","


# 正链：第2及以后坐标向前移动3bp:
def shift(string):
    num = string.count(',')
    res = string.split(',')[0]
    for i in range(0,num-1):
        res = res+","+str(int(string.split(',')[i+1])+3)
    return res+","


# tmp = '0,10,'
# print (tmp)
# print (shift(tmp))
# print (exon(tmp))
# print (exon_rev(tmp))


for i in input_data.readlines():
    df = i.split('\t')
    if df[5] == "+":
        print (df[0]+"\t"+str(int(df[1])-3)+"\t"+df[2]+"\t"+df[3]+"\t"+df[4]+"\t"+df[5]+"\t"+
                str(int(df[1])-3)+"\t"+df[2]+"\t"+df[8]+"\t"+
                exon(df[10])+"\t"+shift(df[11]))
    elif df[5] == "-":
        print (df[0]+"\t"+df[1]+"\t"+str(int(df[2])+3)+"\t"+df[3]+"\t"+df[4]+"\t"+df[5]+"\t"+
                df[1]+"\t"+str(int(df[2])+3)+"\t"+df[8]+"\t"+
                exon_rev(df[10])+"\t"+df[11],end='')
