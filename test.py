# -*- coding:utf-8 -*-
# @Author   :dqfzj
# @Email    :dqfzj@foxmail.com
# @time     :2020/6/4 9:55
# @File     :test.py
# @Software :PyCharm
'''demo'''
import time
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import random
import scipy as sc

def boxave(list):
    predicts = [list[0]]
    position_predict = predicts[0]
    predict_var = 0
    v_std = 1  # yu ce fang cha 越大实时性越好
    odo_var = 10  # ce liang fang cha
    for i in range(1, 1000):
        predict_var += v_std ** 2
        position_predict = position_predict * odo_var / (predict_var + odo_var) + list[i] * predict_var / (
                predict_var + odo_var)
        predict_var = (predict_var * odo_var) / (predict_var + odo_var) ** 2
        predicts.append(position_predict)
    return predicts


if __name__ == '__main__':
    X = np.linspace(0, 4 * np.pi, 1000, endpoint=True)
    Y = np.sin(X)*340
    signal_array = Y
    noise_array = np.random.normal(0, 30, 1000)
    """noise_array = []
    for x in range(itr):
        noise_array.append(random.gauss(mu,sigma))"""
    signal_noise_array = signal_array + noise_array
    xs = signal_noise_array

    xn = xs  # 原始输入端的信号为被噪声污染的正弦信号

    dn = signal_array  # 对于自适应对消器，用dn作为期望
    yn=boxave(signal_noise_array)

    plt.figure(1)
    plt.plot(xn, label="$xn$")
    plt.plot(yn, label="$dn$")
    plt.xlabel("Time(s)")
    plt.ylabel("Volt")
    plt.title("original signal xn and desired signal dn")
    plt.legend()

    plt.figure(2)
    plt.plot(dn, label="$dn$")
    plt.plot(yn, label="$yn$")
    plt.xlabel("Time(s)")
    plt.ylabel("Volt")
    plt.title("original signal xn and processing signal yn")
    plt.legend()

    plt.show()