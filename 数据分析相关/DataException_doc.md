# 数据异常处理

#### 1， 简单统计分析  ####
 对属性值进行一个描述性统计，从而查看哪些值是不合理的
#### 2，3σ原则  ####
 根据正态分布的定义，距离平均值3σ之外的概率不超过0.003，这属于极小概率事件
 ![110599c799d56b14282a74b6be4219da.png](en-resource://database/582:0)
```python
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
        data_temp[data_temp.columns.values[i]] = data_temp[
            data_temp[data_temp.columns.values[i]] 
            < data_up[data_temp.columns.values[i]]]        
        data_temp[data_temp.columns.values[i]] = data_temp[
            data_temp[data_temp.columns.values[i]] 
            > data_under[data_temp.columns.values[i]]]    
    return data_temp
```
#### 3，箱型图分析  ####
箱型图提供了一个标准，即大于或小于箱型图设定的上下界的数值即为异常值
    
箱形图（Box-plot）又称为盒须图、盒式图或箱线图，是一种用作显示一组数据分散情况资料的统计图。因形状如箱子而得名。在各种领域也经常被使用，常见于品质管理。它主要用于反映原始数据分布的特征，还可以进行多组数据分布特征的比 较。箱线图的绘制方法是：先找出一组数据的上边缘、下边缘、中位数和两个四分位数；然后， 连接两个四分位数画出箱体；再将上边缘和下边缘与箱体相连接，中位数在箱体中间

```python
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
    axes.set_ylabel("values of " + labels)    plt.show()
```

#### 4，聚类分析  ####
如DBSCAN基于密度的聚类方法，可用于离群点检测
![5ff2642622fccbf6dcbe6fcdbd8d27ad.png](en-resource://database/584:0)
