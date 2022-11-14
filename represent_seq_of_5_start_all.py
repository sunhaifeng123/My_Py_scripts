#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import argparse
import pandas as pd

# 读取文件：
parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", help="Input File", type=str)
parser.add_argument("-o","--output", help="Output File", type=str)

args = parser.parse_args()

input_file = args.input
output_file = args.output

data = pd.read_csv(input_file, sep="\t", dtype=str) # 读取文本


# 根据第一列排序：
col_sort = data.columns.tolist()[0] # 获取第一列的colname
data_sort = data.sort_values(by=col_sort, ascending= False) # ColNames_First：根据第一列排序；ascending：是否升序，默认No


# 输出header：
Output = open(output_file,'w')
Output.write("\t".join(list(data_sort.columns)) + '\t' + "Represent_Seq" + '\n')

# 循环输出：
rep = "------"

for i in range(len(data)): # 每行

    seq = str(data_sort.iloc[i,0]) # 第i行、第1列的seq序列（字符串）

    line_list = list(data_sort.iloc[i]) # 数据框的第i行转为list
    line_list_str = "\t".join(line_list) # list转为以\t分隔的字符串

    if rep.startswith(seq): # 如果smatch

        # print ("match!")
        Output.write(line_list_str + '\t' + rep + '\n')

    else: # 如果不match

        # print ("Not match!")
        rep = seq
        Output.write(line_list_str + '\t' + rep + '\n')

print ("Success!")

## Example-Input:
# Row.names       baseMean        log2FoldChange
# AAABBBCCC       1       2
# AAABBB  3       4
# AAA     5       6
# BBB     7       8
# CCC     9       10

## Example-Output:
# Row.names       baseMean        log2FoldChange  Represent_Seq
# CCC     9       10      CCC
# BBB     7       8       BBB
# AAABBBCCC       1       2       AAABBBCCC
# AAABBB  3       4       AAABBBCCC
# AAA     5       6       AAABBBCCC
