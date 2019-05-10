#!/usr/bin/python3
# -*- coding:utf8 -*-


__author__ = '@Github: Vctcn93'
__version__ = 1.0
__date__ = 20190509


import chameleon.constance as constance
import math


"""
transfert 转换模块
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


def __is_out_of_china(lng: float, lat: float) -> bool:
    """
    判断是否在国内，不在国内返回True，在国内返回False
    :param lng: float 经度
    :param lat: float 纬度
    :return: bool
    """
    if 72.004 < lng < 137.8347:
        return False
    if .8293 < lat < 55.8271:
        return False
    return True


def wgs84togcj02(lng: float, lat: float) -> list:
    """
    将wgs84坐标系转为火星坐标
    :param lng: float 经度
    :param lat: float 纬度
    :return: list[float] 经纬度数组
    """
    if __is_out_of_china(lng, lat):  # 如果不在国内
        return [lng, lat]  # 不做转换

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


def wgs84tobd09(lng: float, lat: float) -> list:
    """
    将wgs84坐标系转为百度坐标
    :param lng: float 经度
    :param lat: float 纬度
    :return: list[float] 经纬度数组
    """
    if __is_out_of_china(lng, lat):
        return [lng, lat]

    gcjlng, gcjlat = wgs84togcj02(lng, lat)
    bdlng, bdlat = gcj02tobd09(gcjlng, gcjlat)

    return [bdlng, bdlat]


def gcj02towgs84(lng: float, lat: float) -> list:
    """
    将火星坐标系转为wgs84坐标
    :param lng: float 经度
    :param lat: float 纬度
    :return: list[float] 经纬度数组
    """
    if __is_out_of_china(lng, lat):
        return [lng, lat]

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


def gcj02tobd09(lng: float, lat: float) -> list:
    """
    将火星坐标系转为百度坐标
    :param lng: float 经度
    :param lat: float 纬度
    :return: list[float] 经纬度数组
    """
    z = math.sqrt(lng * lng + lat * lat) + .00002 * math.sin(lat * constance.X_PI)
    theta = math.atan2(lat, lng) + .000003 * math.cos(lng * constance.X_PI)
    bd_lng = z * math.cos(theta) + .0065
    bd_lat = z * math.sin(theta) + .006
    return [bd_lng, bd_lat]


def bd09towgs84(lng: float, lat: float) -> list:
    """
    将百度坐标系转为wgs84坐标
    :param lng: float 经度
    :param lat: float 纬度
    :return: list[float] 经纬度数组
    """
    if __is_out_of_china(lng, lat):
        return [lng, lat]
    gcjlng, gcjlat = bd09togcj02(lng, lat)
    wgslng, wgslat = gcj02towgs84(gcjlng, gcjlat)
    return [wgslng, wgslat]


def bd09togcj02(lng: float, lat: float) -> list:
    """
    将百度坐标系转为火星坐标
    :param lng: float 经度
    :param lat: float 纬度
    :return: list[float] 经纬度数组
    """
    x = lng - .0065
    y = lat - .006
    z = math.sqrt(x * x + y * y) - .00002 * math.sin(y * constance.X_PI)
    theta = math.atan2(y, x) - .000003 * math.cos(x * constance.X_PI)
    gcj_lng = z * math.cos(theta)
    gcj_lat = z * math.sin(theta)
    return [gcj_lng, gcj_lat]


def lnglattomercator(
        lng: float,
        lat: float,
        reference_position: list = (0, 0),
        convert_rate: list = (1, 1),
) -> list:
    """
    将经纬度坐标二维展开为平面坐标
    :param lng: float 经度坐标
    :param lat: float 纬度坐标
    :param reference_position: list 经纬度参照零点坐标，如城市中心或项目中心
    :param convert_rate: list 形变比例
    :return: list 展开后的二纬坐标
    """
    x = lng - reference_position[0]
    y = lat - reference_position[1]

    x = x * constance.MERCATOR
    y = math.log(math.tan((90 + y) * constance.PI / 360)) / (constance.PI / 180)
    y = y * constance.MERCATOR

    return [x * convert_rate[0], y * convert_rate[1]]


def strlocationtofloatlocation(location: str) -> list:
    """
    将字符格式的经纬坐标转为数字列表格式的经纬坐标，用以计算
    :param location: str 如'123.456, 123.456'
    :return: list 如[123.456, 123.456]
    """
    # 预设location为'123.456, 123.456'
    str_locations = location.split(',')
    # 输出 [123.456, 123.456]
    return [num for num in map(float, str_locations)]


def floatlocationtostrlocation(location: list) -> str:
    """
    将数字列表格式的经纬坐标转为字符格式的经纬坐标，用以请求
    :param location: list 如[123.456, 123.456]
    :return: str 如'123.456, 123.456'
    """
    # 预设location为[123.456, 123.456]
    # 输出 '123.456, 123.456'
    return ','.join([text for text in map(str, location)])
