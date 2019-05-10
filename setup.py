from setuptools import setup, find_packages


packages = find_packages()
lc = open('LICENSE').read()
rm = open('README.MD').read()

setup(
    name="chamelon",
    version="1.0",
    author="Vctcn93",
    author_email="vincentvane@yeah.net",
    description="实现 GIS 坐标系转换的基础包",
    license=lc,
    keywords="SCity",
    packages=packages,
    long_description=rm,
    install_requires=['pandas', 'pytest'],
)
