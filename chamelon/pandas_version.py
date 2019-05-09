#!/usr/bin/python3
# -*- coding:utf8 -*-


__author__ = '@Github: Vctcn93'
__version__ = 1.0
__date__ = 20190509


"""
transfer 模块的 pandas 版本
使用 pandas 直接通过 Series 使用浮点运算，提高运算效率
"""


import chameleon
import pandas as pd


def wgs84togcj02(lnglat: pd.Series) -> pd.Series:
    return lnglat.apply(lambda x: chamelon.wgs84togcj02(x[0], x[1]))


def wgs84tobd09(lnglat: pd.Series) -> pd.Series:
    return lnglat.apply(lambda x: chamelon.wgs84tobd09(x[0], x[1]))


def gcj02towgs84(lnglat: pd.Series) -> pd.Series:
    return lnglat.apply(lambda x: chamelon.gcj02towgs84(x[0], x[1]))


def gcj02tobd09(lnglat: pd.Series) -> pd.Series:
    return lnglat.apply(lambda x: chamelon.gcj02tobd09(x[0], x[1]))


def bd09towgs84(lnglat: pd.Series) -> pd.Series:
    return lnglat.apply(lambda x: chamelon.bd09towgs84(x[0], x[1]))


def bd09togcj02(lnglat: pd.Series) -> pd.Series:
    return lnglat.apply(lambda x: chamelon.bd09togcj02(x[0], x[1]))


def lnglattomercator(
        lnglat: pd.Series,
        reference_position: list = (0, 0),
        convert_rate: list = (1, 1)
) -> pd.Series:
    return lnglat.apply(lambda x: chamelon.lnglattomercator(
        x[0],
        x[1],
        reference_position,
        convert_rate
    )
                        )


def strlocationtofloatlocation(lnglat: pd.Series) -> pd.Series:
    return lnglat.apply(chamelon.strlocationtofloatlocation)


def floatlocationtostrlocation(lnglat: pd.Series) -> pd.Series:
    return lnglat.apply(chamelon.floatlocationtostrlocation)
