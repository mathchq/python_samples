# coding=utf-8

'''
认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
'''


# 默认参数必须指向不变对象

# 可变参数

def product(*args):
    prod = 1
    for _ in args:
        prod *= _
    return prod


# 关键字参数
def cat(**kw):
    if 'age' in kw: print(kw['age'])
    
    if 'weight' in kw: print(kw['weight'])


# 命名关键字(确定的可变参数)
def person(name, age, *, city, job):
    print(name, age, city, job)


def person(name, age, *args, city, job):
    print(name, age, args, city, job)


if __name__ == '__main__':
    print(product(2, 3, 4))
    cat(age=4, weight=6)
