#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Team: NESP Technology
Author: <a href="mailto:1756404649@qq.com">靳兆鲁 Email:1756404649@qq.com</a>
Time: Created 2020/4/26 0:04
Project: FishMovieManagerTools
Description:Python Grammar extensions
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


import sys

sys.modules[__name__] = _const()
