"""
item: 支持向量机相关算法实现
author by WIT_lyp
timestamp: 2019/11/6 18:14

"""
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.svm import SVC
from datetime import datetime
from sklearn.metrics import accuracy_score, \
    precision_score, recall_score, f1_score, cohen_kappa_score
import numpy as np
from pyecharts import Line
import matplotlib.pyplot as plt
"""
支持向量机类:实现SVM算法训练
@:param :[kernel] 核函数:"rbf", "poly", "sigmoid"
@:param :[C] 惩罚因子
@:param :[function] 多分类策略:"ovo", "ovr"
"""


class SupportVector:
    def __init__(self, kernel, C, function):
        self.kernel = kernel
        self.C = C
        self.function = function


    def svm_model(self, datasets):
        print("训练开始时间: ", datetime.now().strftime('%H:%M:%S'))
        svm = SVC(kernel=self.kernel, C=self.C, decision_function_shape=self.function).fit(datasets["x_train"], datasets["y_train"])
        print(svm)
        print("训练结束时间: ", datetime.now().strftime('%H:%M:%S'))

        imgs_pred = svm.predict(datasets["x_test"])
        true = np.sum(imgs_pred == datasets["y_test"])
        print("预测结果正确的数目: ", true)
        print("预测结果错误的数目: ", datasets["y_test"].shape[0] - true)
        print("预测结果准确率: ", true / datasets["y_test"].shape[0])
        print(classification_report(svm.predict(datasets["x_test"]), datasets["y_test"]))


        # 构建评价模型
        print("\n\n##########  评价部分  ############\n\n")
        print('使用SVM预测的数据准确率为: ',
              accuracy_score(datasets["y_test"], imgs_pred))
        print('使用SVM预测的数据精确率为: ',
              precision_score(datasets["y_test"], imgs_pred, average="weighted"))
        print('使用SVM预测的数据召回率为: ',
              recall_score(datasets["y_test"], imgs_pred, average="weighted"))
        print('使用SVM预测的数据的F1值为: ',
              f1_score(datasets["y_test"], imgs_pred, average="weighted"))
        print("使用SVM预测的数据的Cohen's Kappa系数为: ",
              cohen_kappa_score(datasets["y_test"], imgs_pred))

        self.svm = svm

    def svm_predict(self, datasets):
        pre = self.svm.predict(datasets["x_test"])
        line = Line("预测-原始标签对比图(SVM)")
        l = [i for i in range(30)]
        print(l)
        line.add("预测结果", l, pre[:30], is_smooth=True )
        line.add("原始标签", l, datasets["y_test"][:30], is_smooth=True)
        # line.show_config()
        line.render("svm.html")


if __name__ == '__main__':
    pass