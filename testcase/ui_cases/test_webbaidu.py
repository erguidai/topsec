# -*- coding: utf-8 -*-
'''
@Time    : 2022/5/2 12:46
@Author  : ergudai
@File    : test_webbaidu.py
'''

import pytest  # 引入pytest包


def test_a():  # test开头的测试函数
    print("------->test_web baidu")
    assert 1  # 断言成功


def test_b():
    print("------->test_b")
    assert 0  # 断言失败


if __name__ == '__main__':
    pytest.main("-s  test_demo.py")  # 调用pytest的main函数执行测试
