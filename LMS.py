# -*- coding:utf-8 -*-
# @Author   :dqfzj
# @Email    :dqfzj@foxmail.com
# @time     :2020/6/2 14:48
# @File     :LMS.py
# @Software :PyCharm
# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# 定义向量的内积
def multiVector(A, B):
    C = np.zeros(len(A))

    for i in range(len(A)):
        C[i] = A[i] * B[i]

    return sum(C)


# 取定给定的反向的个数

def inVector(A, b, a):
    D = np.zeros(b - a + 1)
    # print(D.shape)
    for i in range(b - a + 1):
        D[i] = A[i + a]

    return D[::-1]


# lMS算法的函数

def LMS(xn, M, mu, itr):
    en = np.zeros(itr)

    W = [[0] * M for i in range(itr)]
    for k in range(itr)[M - 1:itr]:
        x = inVector(xn, k, k - M + 1)
        d = x.mean()

        y = multiVector(W[k - 1], x)

        en[k] = d - y

        W[k] = np.add(W[k - 1], 2 * mu * en[k] * x)  # 更新权重

    # 求最优时滤波器的输出序列

    yn = np.inf * np.ones(len(xn)+6)

    for k in range(len(xn))[M - 1:len(xn)]:
        x = inVector(xn, k, k - M + 1)

        yn[k] = multiVector(W[len(W) - 1], x)

    return yn, en


if __name__ == "__main__":

    # 参数初始化
    itr = 1000  # 采样的点数
    sigma = 0.12
    noise_size = itr

    M = 32  # 滤波器的阶数

    mu = 0.001  # 步长因子

    """对数据源进行更换"""

    path = 'C:\\Users\\Feng\\Desktop\\data.xlsx'
    xls = pd.ExcelFile(path)
    df = xls.parse('单点时序')

    datas = df['no.5'][:1000]/100


    # 调用LMS算法
    start=time.time()
    (yn, en) = LMS(datas,M, mu, itr)
    end=time.time()
    print(end-start)
    df.insert(10, 'lms', yn*100, )
    df.to_excel('C:\\Users\\Feng\\Desktop\\output.xlsx', sheet_name='Sheet1', index=False)
    xls.close()


    # 画出图形

    plt.figure(1)
    plt.plot(datas*100, label="$dn$")
    plt.plot(yn*100, label="$yn$")
    plt.xlabel("Time(s)")
    plt.ylabel("Volt")
    plt.title("original signal xn and processing signal yn  10  0.001")
    plt.legend()

    plt.figure(2)
    plt.plot(en, label="$en$")
    plt.xlabel("Time(s)")
    plt.ylabel("Volt")
    plt.title("error between processing signal yn and desired voltage dn")
    plt.legend()
    plt.show()


