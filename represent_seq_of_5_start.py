#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import argparse

# 读取文件：
parser = argparse.ArgumentParser()
parser.add_argument("-i","--input_fasta", help="Input File", type=str)

args = parser.parse_args()

input_file = args.input_fasta

Input = open(input_file, 'r')

rep = "NNN"

# 循环读取：
for line in Input.readlines():
    line = line.strip('\n')

    if rep.startswith(line):
        print (line + '\t' + rep)
    else:
        rep = line
        print (line + '\t' + rep)

        
# Example:
# input (need to be sorted):
## AAABBBCCC
## AAABBB
## AAA
## BBB
## CCC
# onput:
## AAABBBCCC       AAABBBCCC
## AAABBB  AAABBBCCC
## AAA     AAABBBCCC
## BBB     BBB
## CCC     CCC
