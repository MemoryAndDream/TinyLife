# -*- coding: utf-8 -*-
"""
Description :
date：          2023/3/22
"""


def move_origin( dirts):  # 原始的移动不一定只有一个方向
    # 1,2 3,4互相抵消

    if 1 in dirts and 2 in dirts:
        dirts.remove(1)
        dirts.remove(2)
    if 3 in dirts and 4 in dirts:
        dirts.remove(3)
        dirts.remove(4)
    print(dirts)


move_origin([1,3])
move_origin([1,2,3])
move_origin([1,3,4])
move_origin([1,2,3,4])