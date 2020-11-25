# coding=utf-8

# Author: mathchq <mathchq@gmail.com>
import pandas as pd

samples = """trade_date stock_code stock_name   open   high    low  close
2008-12-12   sh600000       浦发银行  13.85  15.50  13.60  13.88
2008-12-19   sh600000       浦发银行  14.25  15.05  13.39  14.67
2008-12-26   sh600000       浦发银行  14.67  14.68  13.26  13.41
2008-12-31   sh600000       浦发银行  13.19  13.50  13.00  13.25
2009-01-09   sh600000       浦发银行  13.51  14.60  13.35  14.09
2009-01-16   sh600000       浦发银行  14.09  16.10  13.80  15.62
2009-01-23   sh600000       浦发银行  15.85  16.95  15.78  16.69
2009-02-06   sh600000       浦发银行  16.80  17.78  16.23  17.56"""


def string2df(strs, sep=','):
    """
    '\s' 空格, '\s+' 尽可能的匹配空格
    
    :param strs:
    :param sep:
    :return:
    """
    
    return pd.read_csv(__import__('io').StringIO(strs), sep=sep)


def numeric_columns(df):
    return df.columns[[*map(pd.api.types.is_numeric_dtype, df.dtypes)]]


if __name__ == '__main__':
    df = string2df(samples, '\s+')
    numeric_columns(df)
    # rolling apply要求每个元素可被强制转换成float类型
