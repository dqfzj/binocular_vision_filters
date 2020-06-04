'''demo'''
import time
import pandas as pd
import numpy as np

def boxave(list):
    predicts = [list[0]]
    position_predict = predicts[0]
    predict_var = 0
    v_std = 1  # yu ce fang cha
    odo_var = 10  # ce liang fang cha
    for i in range(1, 1000):
        predict_var += v_std ** 2
        position_predict = position_predict * odo_var / (predict_var + odo_var) + list[i] * predict_var / (
                predict_var + odo_var)
        predict_var = (predict_var * odo_var) / (predict_var + odo_var) ** 2
        predicts.append(position_predict)
    return predicts




if __name__ == '__main__':
    path='C:\\Users\\Feng\\Desktop\\data.xlsx'
    xls=pd.ExcelFile(path)
    df=xls.parse('单点时序')

    datas=df['no.1'][:1000]
    #print(datas)
    after=boxave(datas)
    #print(after)
    for i in range(6):
        after.append(0)
    df.insert(6,'boxave',after,)
    df.to_excel('C:\\Users\\Feng\\Desktop\\fuyao1.xlsx',sheet_name='Sheet1',index=False)
    xls.close()