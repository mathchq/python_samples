# coding=utf-8

# Author: mathchq <mathchq@gmail.com>

import sample_module
from sample_module import *


def test_single_underscore():
    """
    python中的单下划线：标示变量或函数仅供内部使用
    但并不具备强制约束性
    
    :return:
    """
    assert '_local_print_message' in dir(sample_module), '_local_print_message not in sample_module!'
    assert print_message(), 'call print_message() failed!'

    # 通过from sample_module import * 方式无法被成功导入
    try:
         _local_print_message()
    except NameError as e:
        print('Exception: ', str(e))
    
    assert sample_module._local_print_message(), 'call sample_module._local_print_message() failed!'


if __name__ == '__main__':
    test_single_underscore()