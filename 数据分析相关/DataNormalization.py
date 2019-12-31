"""
item: 数据标准化
author by WIT_lyp
timestamp: 2019/11/16
"""

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

import numpy as np

class data_normalization:

    def __init__(self):
        pass

    """
    函数功能:min_max归一化(将按列进行标准化)
    @:param:data[auto]:将要归一化的数据
    @:param:range[tuple]:将要归一化的范围
    @:return:data_temp:处理后的数据拷贝(标准化不改变原始数据)
    """
    def min_max_scaler(self, data, range=(0, 1)):
        data_temp = data.copy()
        model = MinMaxScaler(feature_range=range)
        data_temp = model.fit_transform(data_temp)
        return data_temp

    """
    函数功能:标准差标准化
    @:param:data[auto]:将要标准化的数据
    @:return:data_temp:处理后的数据拷贝(标准化不改变原始数据)
    """
    def standard_scaler(self, data):
        data_temp = data.copy()
        model = StandardScaler()
        data_temp = model.fit_transform(data_temp)
        return data_temp

    """
    函数功能:均值标准化
    @:param:data[auto]:将要标准化的数据
    @:axis:[0 || 1], 0:按列处理 1:按行处理
    @:return:data_temp:处理后的数据拷贝(标准化不改变原始数据)
    """

    def mean_scaler(self, data, axis=0):
        data_temp = data.copy()
        mean_data = np.mean(data, axis=axis)
        data_temp = (data_temp - mean_data) / (np.max(data_temp, axis=axis) - np.min(data_temp, axis=axis))
        return data_temp

if __name__ == '__main__':
    dn = data_normalization()
    a = np.array([[1, 1, 1, 1], [2, 3, 3, 2], [3, 2, 3, 4]])
    b = dn.mean_scaler(a)

    print(a)
    print(np.mean(a,axis=0))
    #print((a - np.mean(a,axis=0))/(np.max(a, axis=0) - np.min(a, axis=0)))