#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import argparse
import pandas as pd

# 读取文件：
parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", help="Input File", type=str)
parser.add_argument("-c","--column", help="The column to sort", type=int)
parser.add_argument("-o","--output", help="Output File", type=str)

args = parser.parse_args()

input_file = args.input
column = args.column
output_file = args.output

f = open(input_file, 'r') # 打开文本

data = pd.read_csv(f,sep="\t") # 读取文本

# print (data)

col_sort = data.columns.tolist()[column-1] # 获取第一列name

data_sort = data.sort_values(by=col_sort, ascending= False) # ColNames_First：根据第一列排序；ascending：是否升序，默认No

# print (data_sort)

data_sort.to_csv(output_file, sep="\t", index=False) # 输出为txt格式

f.close() # 关闭文本

print ("Success!")
