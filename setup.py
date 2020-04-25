#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Team: NESP Technology
Author: <a href="mailto:1756404649@qq.com">靳兆鲁 Email:1756404649@qq.com</a>
Time: Created 2020/4/25 23:07
Project: FishMovieManagerTools
Description:
"""
#  Copyright (c) 2020  NESP Technology Corporation. All rights reserved.
#
#    This program is free software; you can redistribute it and/or modify it
#    under the terms and conditions of the GNU General Public License,
#    version 2, as published by the Free Software Foundation.
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License.See the License for the specific language governing permissions and
#    limitations under the License.
#
#    If you have any questions or if you find a bug,
#    please contact the author by email or ask for Issues.
#
#    Author:JinZhaolu <1756404649@qq.com>

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
