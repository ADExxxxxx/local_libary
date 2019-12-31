"""
item: 数据填充，删除，插值
author by WIT_lyp
timestamp: 2019/11/16 17:32
"""

import pandas as pd
import numpy as np
from collections import Counter
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import ClusterCentroids



class DataPreprocess:
    def __init__(self):
        pass

    """
    函数功能: 对训练数据进行清洗
    @:param: x[Dataframe] 处理的数据
    @:feat_Remv: 将要删除的字段
    @:return: 处理后的数据
    """
    def Data_preprocessing(self, data, feat_Remv):
        # 删除重复值
        data = data.drop_duplicates()
        # 删除指定字段
        data = data.drop(feat_Remv, axis = 1)
        # 填充缺失值
        data = data.fillna(-1)

        return data

    """
    函数功能: 对训练数据种类及其数量进行打印
    @:param: data[auto]:想要统计的数据
    @:return: None
    """
    def Data_label_count(self, data):
        print(Counter(data))

    """
    函数功能: 对数据进行上采样补全(基于SMOTE规则)
    @:param: datas[auto]:想要补全的数据
    @:labels: 想要补全的标签
    @:return: data_smote, label_smote 采样后的数据及标签
    """
    def Data_up_sampling(self, datas, labels):
        smo = SMOTE()
        data_smote, label_smote = smo.fit_sample(datas, labels)
        print(Counter(label_smote))
        return data_smote, label_smote

    """
    函数功能: 对数据进行下采样补全(基于聚类分析规则)
    @:param: datas[auto]:想要补全的数据
    @:labels: 想要补全的标签
    @:return: data_cc, label_cc 采样后的数据及标签
    """
    def Data_under_sampling(self, datas, labels):
        cc = ClusterCentroids()
        data_cc, label_cc = cc.fit_sample(datas, labels)
        print(Counter(label_cc))
        return data_cc, label_cc


if __name__ == "__main__":
    data = pd.DataFrame({"A":[1, 2, 3, 1], "B":[1, 2, 3, 4]})
    dp = DataPreprocess()
