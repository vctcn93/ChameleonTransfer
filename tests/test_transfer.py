#!/usr/bin/python3
# -*- coding:utf8 -*-


__author__ = '@Github: Vctcn93'
__version__ = 1.0
__date__ = 20190513


import chameleon as cml


def test_transfer():
    location = [50, 60]
    assert cml.wgs84togcj02(location) == [50, 60]
    assert cml.wgs84tobd09(location) == [50, 60]
    assert cml.gcj02towgs84(location) == [50, 60]
    assert cml.bd09towgs84(location) == [50, 60]

    location = [80, 60]
    assert cml.wgs84togcj02(location) == [80, 60]
    assert cml.wgs84tobd09(location) == [80, 60]
    assert cml.gcj02towgs84(location) == [80, 60]
    assert cml.bd09towgs84(location) == [80, 60]

    location = [50, 50]
    assert cml.wgs84togcj02(location) == [50, 50]
    assert cml.wgs84tobd09(location) == [50, 50]
    assert cml.gcj02towgs84(location) == [50, 50]
    assert cml.bd09towgs84(location) == [50, 50]

    location = [80, 50]
    assert cml.wgs84togcj02(location) != [80, 50]
    assert cml.wgs84tobd09(location) != [80, 50]
    assert cml.gcj02towgs84(location) != [80, 50]
    assert cml.bd09towgs84(location) != [80, 50]
