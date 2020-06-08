'''demo'''
import time
import pandas as pd
from collections import deque
import numpy as np
'''
edit by 徐鸿嘉
class Boxave
input: single value
ouput:
'''
class Boxave(object):
    def __init__(self,set_win_size=5):
        self.backlist=[]
        self.input_num=0
        self.tsum=0
        self.win_size=set_win_size
        self.win_q=deque(maxlen=set_win_size)
    def data_in(self,value):
        if self.input_num<=self.win_size:
            self.backlist.append(value)
            self.win_q.append(value)
            self.input_num=self.input_num+1
            if self.input_num==self.win_size:
                self.tsum=sum(self.backlist[:self.win_size])
                self.input_num = self.input_num + 1
            return value
        else:
            val_win_size_before = self.win_q.popleft()
            self.win_q.append(value)
            self.tsum=self.tsum+value-val_win_size_before
            self.backlist.append(self.tsum/self.win_size)
            return self.tsum/self.win_size
    def get_back_list(self):
        return self.backlist
    def boxave_list_to_list(self,list):
        winsize = 5
        tsum = sum(list[:5])
        backlist = []
        for i in list[:5]:
            backlist.append(i)
        for i in range(5, len(list)):
            tsum = tsum + list[i] - list[i - 5]
            backlist.append(tsum / winsize)
        return backlist

def boxave(list):
    winsize = 5
    tsum = sum(list[:5])
    backlist = []
    for i in list[:5]:
        backlist.append(i)
    for i in range(5, len(list)):
        tsum = tsum + list[i] - list[i - 5]
        backlist.append(tsum / winsize)
    return backlist


def ma(datas, dataName):
    datas_copy = datas.copy()
    datas_copy['sma'] = datas[dataName].rolling(5).mean()  # 简单移动平均
    print(datas_copy.head())

    return datas_copy


def ewm(datas, dataName, alpha):
    datas_copy = datas.copy()
    datas_copy['ewm'] = datas[dataName].ewm(alpha=alpha, min_periods=5).mean()  # 指数移动平均线
    print(datas_copy.head())  # 查看前5行
    return datas_copy


def exponential_smoothing_1(alpha, s):
    '''
    一次指数平滑
    :param alpha:  平滑系数
    :param s:      数据序列， list
    :return:       返回一次指数平滑模型参数， list
    '''

    s_temp = []
    s_temp.append(s[0])

    for i in range(1, len(s), 1):
        s_temp.append(alpha * s[i - 1] + (1 - alpha) * s_temp[i - 1])

    return s_temp


def exponential_smoothing_2(alpha, datas, dataName):
    '''
    二次指数平滑
    :param alpha:  平滑系数
    :param s:      数据序列， list
    :return:       返回二次指数平滑模型参数a, b， list
    '''
    s = datas[dataName]
    s_single = exponential_smoothing_1(alpha, s)
    s_double = exponential_smoothing_1(alpha, s_single)

    a_double = [0 for i in range(len(s))]
    b_double = [0 for i in range(len(s))]

    for i in range(len(s)):
        a_double[i] = 2 * s_single[i] - s_double[i]  # 计算二次指数平滑的a
        b_double[i] = (alpha / (1 - alpha)) * (s_single[i] - s_double[i])  # 计算二次指数平滑的b

    return a_double, b_double


def exponential_smoothing_3(alpha, datas, dataName):
    '''
   三次指数平滑
   :param alpha:  平滑系数
   :param s:      数据序列， list
   :return:       返回三次指数平滑模型参数a, b, c， list
   '''
    s = datas[dataName]
    s_single = exponential_smoothing_1(alpha, s)
    s_double = exponential_smoothing_1(alpha, s_single)
    s_triple = exponential_smoothing_1(alpha, s_double)

    a_triple = [0 for i in range(len(s))]
    b_triple = [0 for i in range(len(s))]
    c_triple = [0 for i in range(len(s))]
    for i in range(len(s)):
        a_triple[i] = 3 * s_single[i] - 3 * s_double[i] + s_triple[i]
        b_triple[i] = (alpha / (2 * ((1 - alpha) ** 2))) * (
                (6 - 5 * alpha) * s_single[i] - 2 * ((5 - 4 * alpha) * s_double[i]) + (4 - 3 * alpha) * s_triple[i])
        c_triple[i] = ((alpha ** 2) / (2 * ((1 - alpha) ** 2))) * (s_single[i] - 2 * s_double[i] + s_triple[i])
    return a_triple, b_triple, c_triple


def predict_value_with_exp_smoothing_2(alpha, s, dataName):
    a, b = exponential_smoothing_2(alpha, s, dataName)
    s_temp = []
    # s_temp.append(a[0])
    for i in range(len(a)):
        s_temp.append(a[i] + b[i])

    return s_temp


def predict_value_with_exp_smoothing_3(alpha, s, dataName):
    a, b, c = exponential_smoothing_3(alpha, s, dataName)
    s_temp = []
    # s_temp.append(a[0])
    for i in range(len(a)):
        s_temp.append(a[i] + b[i] + c[i])

    return s_temp


if __name__ == '__main__':
    path = 'data.xlsx'
    xls = pd.ExcelFile(path)
    df = xls.parse('单点时序')

    datas = df[:1000]
    '''
    print(datas.values[0][5])
    print(datas.values[1][5])
    print(datas.values[2][5])
    print(datas.values[3][5])
    '''
    dataSet = 'no.5'
    alphaValue = 0.002

    #after = boxave(datas[dataSet])
    box=Boxave(set_win_size=5)
    after=[]
    for i,data in enumerate(datas[dataSet]):
        temp = box.data_in(data)
        after.append(temp)
    #after=box.get_back_list()

    ma_data = ma(datas, dataSet)
    ewm_data = ewm(datas, dataSet, alphaValue)
    for i in range(4):
        ma_data.loc[i, 'sma'] = datas.loc[i, dataSet]
        ewm_data.loc[i, 'ewm'] = datas.loc[i, dataSet]
    ES1_data = exponential_smoothing_1(alphaValue, datas[dataSet])
    ES2_data = predict_value_with_exp_smoothing_2(alpha=alphaValue, s=datas, dataName=dataSet)
    ES3_data = predict_value_with_exp_smoothing_3(alpha=alphaValue, s=datas, dataName=dataSet)

    for i in range(6):
        ES1_data.append(0)
    print(len(ES1_data))
    for i in range(6):
        ES2_data.append(0)
    print(len(ES3_data))
    for i in range(6):
        ES3_data.append(0)

    df.insert(6, 'ES1', ES1_data, )
    df.insert(7, 'ES2', ES2_data, )
    df.insert(8, 'ES3', ES3_data, )
    df.insert(9, 'sma', ma_data['sma'], )
    df.insert(10, 'ewm', ewm_data['ewm'], )

    df.to_excel('data_'+str(alphaValue)+'.xlsx', sheet_name='Sheet1', index=False)
    xls.close()
