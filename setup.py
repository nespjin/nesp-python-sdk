#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Team: NESP Technology
Author: <a href="mailto:1756404649@qq.com">靳兆鲁 Email:1756404649@qq.com</a>
Time: Created 2020/4/25 23:07
Project: FishMovieManagerTools
Description:
"""
from setuptools import setup

setup(
    name="NespSdkPython",  # pypi中的名称，pip或者easy_install安装时使用的名称
    version="1.0",
    author="Mr.Jin",
    author_email="1756404649@qq.com",
    description="NESP Software Development Kit for Python",
    # license="GPLv3",
    # keywords="redis subscripe",
    # url="https://ssl.xxx.org/redmine/projects/RedisRun",
    packages=['nesp'],  # 需要打包的目录列表

    # 需要安装的依赖
    # install_requires=[
    #     'redis>=2.10.5',
    # ],

)
