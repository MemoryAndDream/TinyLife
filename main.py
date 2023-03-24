
# -*- coding: utf-8 -*-
"""
Description :
date：          2023/3/14
"""
from diandian import DianDian
from environment import Environment

def test_live():
    dd = DianDian()
    dd.born()
    dd.live(1000)




def main():
    test_live()




if __name__ == '__main__':
    main()