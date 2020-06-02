# _*_ coding:utf-8 _*_
import pandas as pd

def arithmeticMeanFilter(input,output):
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
    size = 5
    results=[]
    results.append('arithmeticMeanFilter')
    for l in range(1,101):
        sum=0
        data=df.ix[l,1:70].values
        for m in range(int(-size / 2), int(size / 2 + 1)):
            for n in range(int(-size / 2), int(size / 2 + 1)):
                sum+=data[avemap.index([m,n])]
        results.append(sum/(size*size))
    df.insert(70,'arithmeticMeanFilter',results)
    df.to_excel(output, sheet_name='Sheet1', index=False)
    xls.close()

if __name__ == '__main__':
    arithmeticMeanFilter('data.xlsx','data2.xlsx')
