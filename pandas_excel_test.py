#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author liuzhihang
# @date 2021/8/24 15:14

import pandas as pd
from pandas import DataFrame

# 第一个 sheet
# frame = pd.read_excel('/Users/liuzhihang/Desktop/test.xlsx',1)

data = pd.read_excel("/Users/liuzhihang/Desktop/test.xlsx")

# 打印表
print(data)

# 打印第一行
print(data.values[0])
print(data.values[0][1])

# 查看某一列的值

print(data['姓名'])

# 新增列
data['小名'] = None

# 新增行
data.loc[3] = ['王五', 10, 'js', 20, '小五']

# 删除行：axis=0
# data = data.drop([0, 1], axis=0)

# 删除列：axis=1
# data.drop('标题列3', axis=1)

# 保存
DataFrame(data).to_excel('/Users/liuzhihang/Desktop/test.xlsx', sheet_name='Sheet1', index=False, header=True)
