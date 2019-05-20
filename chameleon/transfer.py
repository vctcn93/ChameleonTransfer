#!/usr/bin/python3
# -*- coding:utf8 -*-


__author__ = '@Github: Vctcn93'
__version__ = 1.0
__date__ = 20190509


import chameleon.constance as constance
import math


"""
transfer 转换模块
使用常规运算，实现 GIS 中的坐标转换

    地心坐标 (WGS84)
    国际标准，从 GPS 设备中取出的数据的坐标系
        国际地图提供商使用的坐标系
    
     火星坐标 (GCJ-02)也叫国测局坐标系
        中国标准，从国行移动设备中定位获取的坐标数据使用这个坐标系
        国家规定： 国内出版的各种地图系统（包括电子形式），必须至少采用GCJ-02对地理位置进行首次加密
    
     百度坐标 (BD-09)
        百度标准，GCJ-02 的二次加密
        百度 SDK，百度地图，Geocoding 使用
     
     墨卡托平面坐标（Mercator）
        将某个坐标系的经纬度，以某一点为中心，转换成二维平面的坐标
"""


def must_be_china(func):
    """
    定义一个用于检测点是否在中国境内的装饰器
    :param func: 需要检测的函数
    :return: list 经纬度
    """
    def wrapper(lnglat):
        if 72.004 < lnglat[0] < 137.8347 and .8293 < lnglat[1] < 55.8271:
            return func(lnglat)
        return lnglat
    return wrapper


def __transform_lng(lng: float, lat: float) -> float:
    ret = 300 + lng + 2 * lat + .1 * lng * lng + \
          .1 * lng * lat + .1 * math.sqrt(math.fabs(lng))
    ret += (20 * math.sin(6.0 * lng * constance.PI) + 20 *
            math.sin(2 * lng * constance.PI)) * 2 / 3
    ret += (20 * math.sin(lng * constance.PI) + 40 *
            math.sin(lng / 3 * constance.PI)) * 2 / 3
    ret += (150 * math.sin(lng / 12 * constance.PI) + 300 *
            math.sin(lng / 30 * constance.PI)) * 2 / 3
    return ret


def __transform_lat(lng: float, lat: float) -> float:
    ret = -100 + 2 * lng + 3 * lat + .2 * lat * lat + \
          .1 * lng * lat + .2 * math.sqrt(math.fabs(lng))
    ret += (20 * math.sin(6.0 * lng * constance.PI) + 20 *
            math.sin(2 * lng * constance.PI)) * 2 / 3
    ret += (20 * math.sin(lat * constance.PI) + 40 *
            math.sin(lat / 3 * constance.PI)) * 2 / 3
    ret += (160 * math.sin(lat / 12 * constance.PI) + 320 *
            math.sin(lat * constance.PI / 30)) * 2 / 3
    return ret


@must_be_china
def wgs84_to_gcj02(lnglat):
    """
    将wgs84坐标系转为火星坐标
    :param lnglat: list[float] 经纬度数组
    :return: list[float] 经纬度数组
    """
    lng, lat = lnglat[0], lnglat[1]
    dlng = __transform_lng(lng - 105, lat - 35)
    dlat = __transform_lat(lng - 105, lat - 35)
    radlat = lat / 180 * constance.PI
    magic = math.sin(radlat)
    magic = 1 - constance.EE * magic * magic
    sqrtmagic = math.sqrt(magic)

    dlat = (dlat * 180) / ((constance.A * (1 - constance.EE)) / (magic * sqrtmagic) * constance.PI)
    dlng = (dlng * 180) / (constance.A / sqrtmagic * math.cos(radlat) * constance.PI)
    mglat = lat + dlat
    mglng = lng + dlng

    return [mglng, mglat]


@must_be_china
def wgs84_to_bd09(lnglat):
    """
    将wgs84坐标系转为百度坐标
    :param lnglat: list[float] 经纬度数组
    :return: list[float] 经纬度数组
    """
    return gcj02_to_bd09(wgs84_to_gcj02(lnglat))


@must_be_china
def gcj02_to_wgs84(lnglat):
    """
    将火星坐标系转为wgs84坐标
    :param lnglat: list[float] 经纬度数组
    :return: list[float] 经纬度数组
    """
    lng, lat = lnglat[0], lnglat[1]
    dlat = __transform_lat(lng - 105, lat - 35)
    dlng = __transform_lng(lng - 105, lat - 35)
    radlat = lat / 180.0 * constance.PI
    magic = math.sin(radlat)
    magic = 1 - constance.EE * magic * magic
    sqrtmagic = math.sqrt(magic)

    dlat = (dlat * 180) / ((constance.A * (1 - constance.EE)) / (magic * sqrtmagic) * constance.PI)
    dlng = (dlng * 180) / (constance.A / sqrtmagic * math.cos(radlat) * constance.PI)
    mglat = lat + dlat
    mglng = lng + dlng

    return [lng * 2 - mglng, lat * 2 - mglat]


def gcj02_to_bd09(lnglat):
    """
    将火星坐标系转为百度坐标
    :param lnglat: list[float] 经纬度数组
    :return: list[float] 经纬度数组
    """
    lng, lat = lnglat[0], lnglat[1]
    z = math.sqrt(lng * lng + lat * lat) + .00002 * math.sin(lat * constance.X_PI)
    theta = math.atan2(lat, lng) + .000003 * math.cos(lng * constance.X_PI)
    bd_lng = z * math.cos(theta) + .0065
    bd_lat = z * math.sin(theta) + .006
    return [bd_lng, bd_lat]


@must_be_china
def bd09_to_wgs84(lnglat):
    """
    将百度坐标系转为wgs84坐标
    :param lnglat: list[float] 经纬度数组
    :return: list[float] 经纬度数组
    """
    return gcj02_to_wgs84(bd09_to_gcj02(lnglat))


def bd09_to_gcj02(lnglat):
    """
    将百度坐标系转为火星坐标
    :param lnglat: list[float] 经纬度数组
    :return: list[float] 经纬度数组
    """
    lng, lat = lnglat[0], lnglat[1]
    x = lng - .0065
    y = lat - .006
    z = math.sqrt(x * x + y * y) - .00002 * math.sin(y * constance.X_PI)
    theta = math.atan2(y, x) - .000003 * math.cos(x * constance.X_PI)
    gcj_lng = z * math.cos(theta)
    gcj_lat = z * math.sin(theta)
    return [gcj_lng, gcj_lat]


def lnglat_to_mercator(lnglat, reference_position=(0, 0), convert_rate=(1, 1)):
    """
    将经纬度坐标二维展开为平面坐标
    :param lnglat: list[float] 经纬度数组
    :param reference_position: list 经纬度参照零点坐标，如城市中心或项目中心
    :param convert_rate: list 形变比例
    :return: list 展开后的二纬坐标
    """
    lng, lat = lnglat[0], lnglat[1]
    x = lng - reference_position[0]
    y = lat - reference_position[1]
    x = x * constance.MERCATOR
    y = math.log(math.tan((90 + y) * constance.PI / 360)) / (constance.PI / 180)
    y = y * constance.MERCATOR

    return [x * convert_rate[0], y * convert_rate[1]]


def str_location_to_float_location(location: str) -> list:
    """
    将字符格式的经纬坐标转为数字列表格式的经纬坐标，用以计算
    :param location: str 如'123.456, 123.456'
    :return: list 如[123.456, 123.456]
    """
    # 预设location为'123.456, 123.456'
    str_locations = location.split(',')
    # 输出 [123.456, 123.456]
    return [num for num in map(float, str_locations)]


def float_location_to_str_location(location: list) -> str:
    """
    将数字列表格式的经纬坐标转为字符格式的经纬坐标，用以请求
    :param location: list 如[123.456, 123.456]
    :return: str 如'123.456, 123.456'
    """
    # 预设location为[123.456, 123.456]
    # 输出 '123.456, 123.456'
    return ','.join(list(map(str, location)))


def str_lnglat_reverse(location: str) -> str:
    """
    将坐标的经纬值位置对调
    :param location: str '123.456, 456.123'
    :return: 对调完成的坐标值 '456.123,123.456'
    """
    list_location = str_location_to_float_location(location)
    list_location.reverse()
    return float_location_to_str_location(list_location)
