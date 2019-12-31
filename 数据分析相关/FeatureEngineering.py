"""
item: 特征工程
author by WIT_lyp
timestamp: 2019/11/16
"""
import pandas as pd
import numpy as np

class FeatureEngineer:
    def __init__(self):
        pass

    """
    函数功能:连续变量离散化，手动分箱
    @:param datas[DataFrame] 将要划分的数据
    @:param binary_ranges[list] 划分的各个区间
    @:param binary_names [list] 划分后的离散标签
    @:param labels 将要划分的字段
    """
    def series_to_dispersed_bin(self, datas, binary_ranges, binary_names, labels):
        datas_temp = datas
        datas_temp['labels'] = pd.cut(np.array(datas['labels']), bins=binary_ranges, labels=binary_names)

        return datas_temp

    def series_to_dispersed_binning(self, ):
        pass


if __name__ == '__main__':
    pass