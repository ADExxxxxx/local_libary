import pyecharts
import numpy as np
import pandas as pd
from pyecharts import Line




if __name__ == '__main__':
    data = np.genfromtxt("1.txt",delimiter="\t")
    shijian = data[:, 0]
    renkou = data[:, 1]
    qiyegeshu = data[:, 2]
    lirun = data[:, -2]
    print(shijian)
    print(renkou)
    print(qiyegeshu)
    line = Line("人口变化趋势与企业活力")
    line.use_theme('roma')
    l = range(9)
    line.add("人口(万人)", l, renkou, is_smooth=True, line_width=3)
    line.add("规模以上工业企业单位数(个)", l, qiyegeshu, is_smooth=True, line_color="blue", line_width=3)
    line.add("规模以上工业企业利润总额", l, lirun, is_smooth=True, line_color="green", line_width=3)
    line.add("规模以上工业企业利润总额", shijian, lirun, is_smooth=True)
    # line.show_config()
    line.render()