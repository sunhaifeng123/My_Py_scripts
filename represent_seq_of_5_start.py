#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import argparse

# 读取文件：
parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", help="Input File", type=str)
parser.add_argument("-o","--output", help="Output File", type=str)

args = parser.parse_args()

input_file = args.input
output_file = args.output

Input = open(input_file, 'r')
Output = open(output_file,'w')

rep = "-------"

# 循环读取：
for line in Input.readlines():
    line = line.strip('\n')

    if rep.startswith(line):
        Output.write(line + '\t' + rep + '\n')
    else:
        rep = line
        Output.write(line + '\t' + rep + '\n')

## Example-Input: (need to be sorted):
## sort in shell: sort -r in.txt > in.sorted.txt
# AAABBBCCC
# AAABBB
# AAA
# BBB
# CCC

## Example-Onput:
# AAABBBCCC       AAABBBCCC
# AAABBB  AAABBBCCC
# AAA     AAABBBCCC
# BBB     BBB
# CCC     CCC
