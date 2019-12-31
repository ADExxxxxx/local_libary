"""
item: 数据异常检测
author by WIT_lyp
timestamp: 2019/11/16
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import DBSCAN


class DataException:
    def __init__(self):
        pass

    """
    函数功能:显示相关数据相关列的箱型图
    @:param data[DataFrame] 显示的数据
    @:param labels[all:打印所有列(默认)] 输入想显示的列
    """
    def box_plot(self, data, labels="all"):
        fig, axes = plt.subplots()
        if labels == "all":
            data.plot(kind='box', ax=axes)
        else:
            data[labels].plot(kind='box', ax=axes)
        axes.set_ylabel("values of " + labels)
        plt.show()


    """
    函数功能：删除异常数据(基于3σ原则)
    @:param data[DataFrame] 要删除的数据
    @:return data_temp[DataFrame] 异常值显示为NaN后的数据
    """
    def check_exception(self, data):
        data_temp = data.copy()
        data_std = data_temp.std()
        data_mean = data_temp.mean()
        data_up = data_mean + 3 * data_std
        data_under = data_mean - 3 * data_std
        for i in range(len(data_temp.columns.values)):
            data_temp[data_temp.columns.values[i]] = data_temp[data_temp[data_temp.columns.values[i]] < data_up[data_temp.columns.values[i]]]
            data_temp[data_temp.columns.values[i]] = data_temp[data_temp[data_temp.columns.values[i]] > data_under[data_temp.columns.values[i]]]
        return data_temp

    """
    函数功能：打印二维数据散点图
    @:param data[DataFrame] 要显示的数据(二维)
    """
    def scatter_analyse(self, data):
        plt.scatter(data.values[:, 0], data.values[:, 1], marker='o')
        plt.show()


    """
    函数功能：DBSCAN分析图
    @:param data[DataFrame] 要显示的数据(二维)
    @:param eps 阈值
    """
    def DBSCAN_analyse(self, data, eps=0.5):
        model = DBSCAN(eps=eps).fit_predict(data.values)
        plt.scatter(data.values[:, 0], data.values[:, 1], c=model)
        plt.show()


if __name__ == '__main__':
    arr = [[np.random.random(), i+np.random.random(), i + 1 + np.random.random()] for i in range(18)]
    arr.append([11, 44, 77])
    df = pd.DataFrame(arr)
    df.columns = ['a', 'b', 'c']
    df = df.drop("c", axis=1)
    de = DataException()
    de.DBSCAN_analyse(df, 3)

