#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Team: NESP Technology
Author: <a href="mailto:1756404649@qq.com">靳兆鲁 Email:1756404649@qq.com</a>
Time: Created 2020/4/26 0:26
Project: FishMovieManagerTools
Description:Python Grammar extensions: Const
"""


class _const:
    """Const type for python

     Usage:# test.py
             import const
             const.PI=3.14
             print(const.PI)

     if you rebind a value,it will raise ConstError
     """

    class ConstError(TypeError):
        pass

    def __setattr__(self, key, value):
        """Check is rebind or not,raise ConstError if it's true"""
        if key in self.__dict__:
            raise self.ConstError("Can't rebind const (%s)" % key)
        self.__dict__[key] = value


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

import sys

sys.modules[__name__] = _const()
