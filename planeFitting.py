# _*_ coding:utf-8 _*_
__author__ = 'hsj'
__date__ = '2020/6/4 上午9:34'

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

def planeFitting(input,output):
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
    n = len(avemap)
    X = []
    Y = []
    Z = []
    for i in range(n):
        X.append(avemap[i][0])
        Y.append(avemap[i][1])
    results = []
    results.append('planeFitting')
    for l in range(1, 101):
        Z = df.ix[l, 1:70].values
        # 创建系数矩阵A
        A = np.zeros((3, 3))
        for i in range(n):
            A[0, 0] = A[0, 0] + X[i] ** 2
            A[0, 1] = A[0, 1] + X[i] * Y[i]
            A[0, 2] = A[0, 2] + X[i]
            A[1, 0] = A[0, 1]
            A[1, 1] = A[1, 1] + Y[i] ** 2
            A[1, 2] = A[1, 2] + Y[i]
            A[2, 0] = A[0, 2]
            A[2, 1] = A[1, 2]
            A[2, 2] = n

        # 创建b
        b = np.zeros((3, 1))
        for i in range(n):
            b[0, 0] = b[0, 0] + X[i] * Z[i]
            b[1, 0] = b[1, 0] + Y[i] * Z[i]
            b[2, 0] = b[2, 0] + Z[i]

        # 求解X
        A_inv = np.linalg.inv(A)
        res= np.dot(A_inv, b)
        results.append(res[2, 0])
    df.insert(70, 'planeFitting', results)
    df.to_excel(output, sheet_name='Sheet1', index=False)
    xls.close()

if __name__ == '__main__':
    planeFitting('data.xlsx','planeFitting.xlsx')
