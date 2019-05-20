#!/usr/bin/python3
# -*- coding:utf8 -*-


__author__ = '@Github: Vctcn93'
__version__ = 1.0
__date__ = 20190510


"""
该脚本演示了模块中各方法使用的方式
"""


# 导入变色龙脚本
import chameleon as cml


# 1. 如何把单个经纬度坐标从 wgs84 转换为 gcj02
# 我们以广州市天河体育中心在 wgs84 中的坐标为例
# 假定广州市天河体育中心在 wgs84(EPSG:4326）中的经纬坐标值为 [113.3194, 23.1403]
wgs84_sport_center = [113.3194, 23.1403]


# 使用模块中的 wgs84togcj02 方法，将 wgs84 坐标系下的坐标转换为 gcj02 坐标系下的坐标：
gcj02_sport_center = cml.wgs84_to_gcj02(wgs84_sport_center)
print(f'国测局坐标系坐标为:{gcj02_sport_center}')  # 打印出换算后的经纬度坐标
# OUTPUT： 国测局坐标系坐标为:[113.32481304825205, 23.13770219137702]


# 2. 类似于从：
# gcj02 转 wgs84、wgs84 转 bd09、bd09 转 gcj02、gcj02 转 bd09、bd09 转 wgs84，
# 均可使用模块中对应的方法
gcj02_sport_center = [113.32481304825205, 23.13770219137702]


# gcj02 转 wgs84
wgs84_sport_center = cml.wgs84_to_gcj02(gcj02_sport_center)
print(f'地心坐标系坐标为:{wgs84_sport_center}')  # 打印出换算后的经纬度坐标
# OUTPUT: 地心坐标系坐标为:[113.33023701919959, 23.135113604425456]


# wgs84 转 bd09
bd09_sport_center = cml.wgs84_to_bd09(wgs84_sport_center)
print(f'百度坐标系坐标为:{bd09_sport_center}')  # 打印出换算后的经纬度坐标
# OUTPUT: 百度坐标系坐标为:[113.3422201772925, 23.138199057854955]


# bd09 转 gcj02
gcj02_sport_center = cml.bd09_to_gcj02(bd09_sport_center)
print(f'国测局坐标系坐标为:{gcj02_sport_center}')  # 打印出换算后的经纬度坐标
# OUTPUT: 国测局坐标系坐标为:[113.33567198159767, 23.132534536732628]


# gcj02 转 bd09
bd09_sport_center = cml.gcj02_to_bd09(gcj02_sport_center)
print(f'百度坐标系坐标为:{bd09_sport_center}')  # 打印出换算后的经纬度坐标
# OUTPUT: 百度坐标系坐标为:[113.3422201807085, 23.13819925826263]


# bd09 转 wgs84
wgs84_sport_center = cml.bd09_to_wgs84(bd09_sport_center)
print(f'地心坐标系坐标为:{wgs84_sport_center}')  # 打印出换算后的经纬度坐标
# OUTPUT: 地心坐标系坐标为:[113.33022610850503, 23.13510471422404]


# 例子二：
# 在部分情况下，我们所拿到的数据，并非是数字列表形式的经纬度，
# 其数据，有可能会以这样的方式存在，比如我们依旧以广州市天河体育中心的wgs84坐标为例，
# 假设我们拿到的数据，为这种形式：'113.3194, 23.1403'
# 我们处于转坐标系的需要，为了使该形式的数据，转化为我们支持的数字列表形式，
# 便可以使用变色龙模块中，提供的各种的转格式的方法，
# 由字符形式，转换为数字列表形式的：cml.strlocationtofloatlocation()；
# 由纯数字列表形式，转换为字符形式：cml.floatlocationtostrlocation()。

str_wgs84_sport_center = '113.3194, 23.1403'  # 获取到的数据为字符形式的经纬度坐标
list_wgs84_sport_center = cml.str_location_to_float_location(  # 使用字符转换为纯数字列表的方法
    str_wgs84_sport_center
)
print(f'转换之后的数据为:{list_wgs84_sport_center}')  # 打印出换算后的数据
# OUTPUT: 转换之后的数据为:[113.3194, 23.1403]


# 此时，我们便可使用转换为数字列表的经纬坐标数据，去进行相关的坐标转换。
list_gcj02_sport_center = cml.wgs84_to_gcj02(list_wgs84_sport_center)
print(f'转换之后的经纬度为:{list_gcj02_sport_center}')  # 打印出换算后的数据
# OUTPUT: 转换之后的经纬度为:[113.32481304825205, 23.13770219137702]


# 同样，在部分情况下，我们出于对数据传输的要求，需要把纯数字列表的数据，转换为字符的形式:
str_gcj02_sport_center = cml.float_location_to_str_location(list_gcj02_sport_center)
print(f'转换之后的数据为:{str_gcj02_sport_center}')  # 打印出换算后的数据
# OUTPUT: 转换之后的数据为: 113.32481304825205,23.13770219137702
