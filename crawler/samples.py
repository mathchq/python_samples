# coding=utf-8
from urllib.parse import quote, unquote


# url链接中的中文字符转换
def test_quote():
    str_chinese = "窗前明月光"
    str_chinese_web = quote(str_chinese, encoding='gbk')
    
    assert str_chinese == unquote(str_chinese_web, encoding='gbk'), "转换错误"


if __name__ == '__main__':
    test_quote()
