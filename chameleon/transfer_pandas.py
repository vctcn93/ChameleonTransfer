#!/usr/bin/python3
# -*- coding:utf8 -*-


__author__ = '@Github: Vctcn93'
__version__ = 1.0
__date__ = 20190509


import chameleon as cml
import pandas as pd


def wgs84togcj02(lnglat: pd.Series) -> pd.Series:
    return lnglat.apply(cml.wgs84_to_gcj02)


def wgs84tobd09(lnglat: pd.Series) -> pd.Series:
    return lnglat.apply(cml.wgs84_to_bd09)


def gcj02towgs84(lnglat: pd.Series) -> pd.Series:
    return lnglat.apply(cml.gcj02_to_wgs84)


def gcj02tobd09(lnglat: pd.Series) -> pd.Series:
    return lnglat.apply(cml.gcj02_to_bd09)


def bd09towgs84(lnglat: pd.Series) -> pd.Series:
    return lnglat.apply(cml.bd09_to_wgs84)


def bd09togcj02(lnglat: pd.Series) -> pd.Series:
    return lnglat.apply(cml.bd09_to_gcj02)


def lnglattomercator(
        lnglat: pd.Series,
        reference_position: list = (0, 0),
        convert_rate: list = (1, 1)
) -> pd.Series:
    return lnglat.apply(lambda x: cml.lnglat_to_mercator(
        x,
        reference_position,
        convert_rate
    )
                        )


def strlocationtofloatlocation(lnglat: pd.Series) -> pd.Series:
    return lnglat.apply(cml.str_location_to_float_location)


def floatlocationtostrlocation(lnglat: pd.Series) -> pd.Series:
    return lnglat.apply(cml.float_location_to_str_location)


def str_lnglat_reverse(lnglat: pd.Series) -> pd.Series:
    return lnglat.apply(cml.str_lnglat_reverse)
