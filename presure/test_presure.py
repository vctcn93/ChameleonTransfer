#!/usr/bin/python3
# -*- coding:utf8 -*-


__author__ = '@Github: Vctcn93'
__version__ = 1.0
__date__ = 20190510


"""
压力测试：
    测试同样换算100万次广州天河体育中心的坐标数据，测试运算速度。
"""


import chameleon as cml
import pandas as pd
from datetime import datetime


class Timer:
    """
    定义一个时间测试类
    """
    def __init__(self):
        self.callbacks = list()

    def run(self):
        for c in self.callbacks:
            name = c.__name__
            t1 = datetime.now()
            c()
            t2 = datetime.now()
            s = t2 - t1
            s = s.microseconds * .000001 + s.seconds
            print('%20s --> %6.2fs' % (name, s))


def make_list_series():
    dict_ = dict()

    for i in range(500000):
        dict_[f'{i}'] = [113.3194, 23.1403]
    return pd.Series(dict_)


def make_str_series():
    dict_ = dict()

    for i in range(500000):
        dict_[f'{i}'] = '113.3194, 23.1403'
    return pd.Series(dict_)


def normal_wgs84togcj02_500k():
    wgs84 = [113.3194, 23.1403]

    for i in range(500000):
        cml.wgs84togcj02(wgs84[0], wgs84[1])


def normal_strlocationtofloatlocation_500k():
    location = '113.3194, 23.1403'

    for i in range(500000):
        cml.strlocationtofloatlocation(location)


def normal_floatlocationtostrlocation_500k():
    location = [113.3194, 23.1403]
    for i in range(500000):
        cml.floatlocationtostrlocation(location)


if __name__ == '__main__':
    t = Timer()
    globals()['listseries'] = make_list_series()
    globals()['strseries'] = make_str_series()

    t.callbacks.append(normal_wgs84togcj02_500k)
    t.callbacks.append(normal_strlocationtofloatlocation_500k)
    t.callbacks.append(normal_floatlocationtostrlocation_500k)

    t.run()
