'''demo'''
import time
import pandas as pd
import numpy as np

def boxave(list):
    winsize=5
    tsum=sum(list[:5])
    backlist=[]
    for i in list[:5]:
        backlist.append(i)
    for i in range(5,len(list)):
        tsum=tsum+list[i]-list[i-5]
        backlist.append(tsum/winsize)
    return backlist




if __name__ == '__main__':
    path='C:\\Users\\Feng\\Desktop\\data.xlsx'
    xls=pd.ExcelFile(path)
    df=xls.parse('单点时序')

    datas=df['no.1'][:1000]
    after=boxave(datas)
    for i in range(6):
        after.append(0)
    df.insert(6,'boxave',after,)
    df.to_excel('C:\\Users\\Feng\\Desktop\\data1.xlsx',sheet_name='Sheet1',index=False)
    xls.close();