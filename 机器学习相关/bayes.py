"""
item: 朴素贝叶斯算法及变种
author by WIT_lyp
timestamp: 2019/11/6 18:14

"""
import numpy as np
from sklearn import datasets
# 新闻数据集
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.naive_bayes import MultinomialNB, BaseDiscreteNB, GaussianNB
from pyecharts import Line


class Bayes:

    def __init__(self):
        pass

    """
    函数功能:提取鸢尾花数据集
    @:param:None
    @:return:type[dict] 返回训练以及测试数据
    """
    def iris_datasets(self):
        _iris = datasets.load_iris()
        x_train, x_test, y_train, y_test = train_test_split(_iris.data, _iris.target)

        return {"x_train": x_train,
                "x_test": x_test,
                "y_train": y_train,
                "y_test": y_test}

    def news_datasets(self):
        news = fetch_20newsgroups(subset="all")
        x_train, x_test, y_train, y_test = train_test_split(news.data, news.target)
        return {"x_train": x_train,
                "x_test": x_test,
                "y_train": y_train,
                "y_test": y_test}

    """
    函数功能:贝叶斯-多项式模型(打印训练结果)
    @:param:datasets:type[dict] 拥有{"x_train", "x_test", "y_train", "y_test"}
    @:return:None
    """
    def multi_model(self, datasets):
        model = MultinomialNB()
        model.fit(datasets["x_train"], datasets["y_train"])
        print(classification_report(model.predict(datasets["x_test"]), datasets["y_test"]))
        self.model = model


    """
    函数功能:贝叶斯-高斯模型(打印训练结果)
    @:param:datasets:type[dict] 拥有{"x_train", "x_test", "y_train", "y_test"}
    @:return:None
    """
    def gaussian_model(self, datasets):
        model = GaussianNB()
        model.fit(datasets["x_train"], datasets["y_train"])
        print(classification_report(model.predict(datasets["x_test"]), datasets["y_test"]))
        self.model = model


    """
    函数功能:贝叶斯-伯努利模型(打印训练结果)
    @:param:datasets:type[dict] 拥有{"x_train", "x_test", "y_train", "y_test"}
    @:return:None
    """
    def base_model(self, datasets):
        model = BaseDiscreteNB()
        model.fit(datasets["x_train"], datasets["y_train"])
        print(classification_report(model.predict(datasets["x_test"]), datasets["y_test"]))
        self.model = model

    def predict_plot(self, datasets):
        pre = self.model.predict(datasets["x_test"])
        line = Line("预测-原始标签对比图(朴素贝叶斯)")
        l = [i for i in range(50)]
        print(l)
        line.add("预测结果", l, pre[:50])
        line.add("原始标签", l, datasets["y_test"][:50])
        # line.show_config()
        line.render("bayes.html")

if __name__ == '__main__':
    ml = Bayes()
    ml.news_datasets()

