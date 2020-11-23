# coding=utf-8

# Author: mathchq <mathchq@gmail.com>

import pandas as pd
import numpy as np


def max_values():
    # 获取多个一维序列的最大值
    cols = 6
    rows = 6
    vector_list = [np.random.random(rows) for _ in range(cols)]
    
    # usage 1
    value1 = np.vstack(vector_list).max(axis=0)
    # usage 2
    value2 = np.maximum.reduce(vector_list)
    # usage 3
    value3 = pd.concat([pd.Series(_) for _ in vector_list], axis=1).max(axis=1).to_numpy()

    np.testing.assert_array_equal(value1, value2)
    np.testing.assert_array_equal(value1, value3)


if __name__ == '__main__':
    max_values()
