import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.metrics import accuracy_score, \
    precision_score, recall_score, f1_score, cohen_kappa_score
from sklearn.metrics import classification_report
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import warnings
import SupportVector as svm
import bayes
from collections import Counter



warnings.filterwarnings("ignore")

with open('./new_data.txt', 'r', encoding='UTF-8') as fp:
    data_lines = fp.readlines()

datas_ls = []
labels_ls = []
lables=[]
label_dictionary = {'小麦':0, '水稻':1, '玉米':2, '稻麦轮作-水稻':3, '黄豆':4, '糜子':5, '冬小麦':6, '谷子':7, '荞麦':8, '柑橘': 9, '红薯':10, '洋芋': 11, '其他': 12}
for data_line in data_lines:
    line_split = data_line.strip().split('\t')
    if len(line_split) != 5:
        raise ValueError('data error! %s is not 5' % data_line)
    datas_ls.append(line_split[1:])
    labels_ls.append(label_dictionary[line_split[0]])

for i in labels_ls:
    temp = np.zeros(13,dtype=int)
    temp[i] = 0
    lables.append(temp)


def suffle(array_1, array_2):
    state = np.random.get_state()
    np.random.shuffle(array_1)
    np.random.set_state(state)
    np.random.shuffle(array_2)


    return array_1, array_2


min_max = preprocessing.StandardScaler()

datas_ls = np.array(datas_ls, dtype=np.float)
labels_ls = np.array(labels_ls, dtype=np.int)
datas_ls = min_max.fit_transform(datas_ls)

print(Counter(labels_ls))
from imblearn.over_sampling import SMOTE
# 定义SMOTE模型，random_state相当于随机数种子的作用
smo = SMOTE(random_state=42)
X_smo, y_smo = smo.fit_sample(datas_ls, labels_ls)
print(Counter(y_smo))

x_train, x_test, y_train, y_test = train_test_split(X_smo, y_smo, test_size=0.1)
datasets = {"x_train":x_train, "x_test":x_test, "y_train": y_train, "y_test": y_test}

"""
plt.subplot(3, 2, 1), plt.title("you ji wu")
plt.plot(range(907), datas_ls[:, 0])
plt.subplot(3, 2, 2), plt.title("N")
plt.plot(range(907), datas_ls[:, 1])

plt.subplot(3, 2, 3), plt.title("P")
plt.plot(range(907), datas_ls[:, 2])

plt.subplot(3, 2, 4), plt.title("K")
plt.plot(range(907), datas_ls[:, 3])

plt.subplot(3, 2, 5), plt.title("labels")
plt.hist(labels_ls.ravel(), range(13))

plt.show()
"""
print("************************* SVM结果 *************************************")
s = svm.SupportVector(kernel='rbf', C=10, function="ovo")
s.svm_model(datasets)
s.svm_predict(datasets)
print("***********************************************************************")

b = bayes.Bayes()
b.gaussian_model(datasets)
b.predict_plot(datasets)