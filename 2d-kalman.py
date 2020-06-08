import pandas as pd
<<<<<<< HEAD
import time
=======
>>>>>>> 920f5321bf3be6107c7f8793474adaf295908cd7
import numpy as np
def boxave(list):
    dt = 1 / 30
    # print(dt)
    # 初始状态
    x_mat = np.mat([[list[0], ], [0, ], [0, ]])
    # 状态转移矩阵
    f_mat = np.mat([[1, dt, 0.5 * dt * dt], [0, 1, dt], [0, 0, 1]])
    # 初始协方差矩阵
    p_mat = np.mat([[0.01, 0, 0], [0, 0.0001, 0], [0, 0, 0.0001]])
    # 状态转移协方差
    q_mat = np.mat([[1, 0, 0], [0, 0.1, 0], [0, 0, 0.01]])
    # 定义观测矩阵
    h_mat = np.mat([1, 0, 0])
    # 定义观测噪声协方差
    r_mat = np.mat([20])
    predicts = [datas[0]]
    for i in range(1, 1000):
        x_predict = f_mat * x_mat
        p_predict = f_mat * p_mat * f_mat.T + q_mat
        kalman = p_predict * h_mat.T / (h_mat * p_predict * h_mat.T + r_mat)
        x_mat = x_predict + kalman * (list[i] - h_mat * x_predict)
        p_mat = (np.eye(3) - kalman * h_mat) * p_predict
        predicts.append(x_predict[0,0])
    return predicts

<<<<<<< HEAD

=======
>>>>>>> 920f5321bf3be6107c7f8793474adaf295908cd7
if __name__ == '__main__':
    path = 'C:\\Users\\Feng\\Desktop\\data.xlsx'
    xls = pd.ExcelFile(path)
    df = xls.parse('单点时序')

<<<<<<< HEAD
    datas = df['no.5'][:1000]
    start = time.time()
    after = boxave(datas)
    end = time.time()
    print(end-start)
=======
    datas = df['no.1'][:1000]
    after = boxave(datas)
>>>>>>> 920f5321bf3be6107c7f8793474adaf295908cd7
    for i in range(6):
        after.append(0)
    df.insert(6, 'boxave', after, )
    df.to_excel('C:\\Users\\Feng\\Desktop\\K0.xlsx', sheet_name='Sheet1', index=False)
    xls.close()
