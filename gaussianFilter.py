# _*_ coding:utf-8 _*_
__author__ = 'hsj'
__date__ = '2020/6/2 下午8:49'

import numpy as np
import pandas as pd

def gaussianFilter(input,output,size=5,sigma=1.3):
    xls = pd.ExcelFile(input)
    df = xls.parse('时空1')
    avemap = [[-4, -2], [-4, -1], [-4, 0], [-4, 1], [-4, 2],
              [-3, -3], [-3, -2], [-3, -1], [-3, 0], [-3, 1], [-3, 2], [-3, 3],
              [-2, -4], [-2, -3], [-2, -2], [-2, -1], [-2, 0], [-2, 1], [-2, 2], [-2, 3], [-2, 4],
              [-1, -4], [-1, -3], [-1, -2], [-1, -1], [-1, 0], [-1, 1], [-1, 2], [-1, 3], [-1, 4],
              [0, -4], [0, -3], [0, -2], [0, -1], [0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
              [1, -4], [1, -3], [1, -2], [1, -1], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
              [2, -4], [2, -3], [2, -2], [2, -1], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
              [3, -3], [3, -2], [3, -1], [3, 0], [3, 1], [3, 2], [3, 3],
              [4, -2], [4, -1], [4, 0], [4, 1], [4, 2]]
    pad=size//2
    weights = np.zeros((size, size), dtype=np.float)
    for x in range(-pad, -pad + size):
        for y in range(-pad, -pad + size):
            weights[y + pad, x + pad] = np.exp(-(x ** 2 + y ** 2) / (2 * (sigma ** 2)))
    weights /= (2 * np.pi * sigma * sigma)
    weights /= weights.sum()
    results=[]
    results.append('gaussianFilter')
    for l in range(1,101):
        data=df.ix[l,1:70].values
        values = np.zeros((size, size), dtype=np.float)
        for x in range(-pad, -pad + size):
            for y in range(-pad, -pad + size):
                values[y + pad, x + pad] = data[avemap.index([y, x])]
        results.append(np.sum(weights*values))
    df.insert(70,'gaussianFilter',results)
    df.to_excel(output, sheet_name='Sheet1', index=False)
    xls.close()

if __name__ == '__main__':
    gaussianFilter('data.xlsx','data5.xlsx')
