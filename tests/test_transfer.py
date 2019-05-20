#!/usr/bin/python3
# -*- coding:utf8 -*-


__author__ = '@Github: Vctcn93'
__version__ = 1.0
__date__ = 20190513


import chameleon as cml


def test_transfer():
    location = [50, 60]
    assert cml.wgs84_to_gcj02(location) == [50, 60]
    assert cml.wgs84_to_bd09(location) == [50, 60]
    assert cml.gcj02_to_wgs84(location) == [50, 60]
    assert cml.bd09_to_wgs84(location) == [50, 60]

    location = [80, 60]
    assert cml.wgs84_to_gcj02(location) == [80, 60]
    assert cml.wgs84_to_bd09(location) == [80, 60]
    assert cml.gcj02_to_wgs84(location) == [80, 60]
    assert cml.bd09_to_wgs84(location) == [80, 60]

    location = [50, 50]
    assert cml.wgs84_to_gcj02(location) == [50, 50]
    assert cml.wgs84_to_bd09(location) == [50, 50]
    assert cml.gcj02_to_wgs84(location) == [50, 50]
    assert cml.bd09_to_wgs84(location) == [50, 50]

    location = [80, 50]
    assert cml.wgs84_to_gcj02(location) != [80, 50]
    assert cml.wgs84_to_bd09(location) != [80, 50]
    assert cml.gcj02_to_wgs84(location) != [80, 50]
    assert cml.bd09_to_wgs84(location) != [80, 50]
