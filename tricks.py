# coding=utf-8

def test_remove_redundant():
    
    # 移除公共元素的便捷写法
    remove_redundant = lambda _: [*{*_}]
    
    array = [1, 2, 2, 4, 3, 'a', 'a']
    array_single_element = remove_redundant(array)
    
    print(array)
    print(array_single_element)


if __name__ == '__main__':
    test_remove_redundant()
