def elementwise_multiplication(a, b):
    """
    逐元素乘法
    :param a: 第一个向量 (列表)
    :param b: 第二个向量 (列表)
    :return: 结果向量 (列表)
    """
    assert len(a) == len(b), "向量长度不一致"
    return [x * y for x, y in zip(a, b)]

def elementwise_addition(a, b):
    """
    逐元素加法
    :param a: 第一个向量 (列表)
    :param b: 第二个向量 (列表)
    :return: 结果向量 (列表)
    """
    assert len(a) == len(b), "向量长度不一致"
    return [x + y for x, y in zip(a, b)]

def vector_sum(a):
    """
    向量求和
    :param a: 向量 (列表)
    :return: 向量元素之和 (浮点数)
    """
    return sum(a)

def vector_average(a):
    """
    向量平均值
    :param a: 向量 (列表)
    :return: 向量元素的平均值 (浮点数)
    """
    if len(a) == 0:
        raise ValueError("向量不能为空")
    return sum(a) / len(a)

def w_sum(a,b):
    """
    计算两个向量的加权和 (逐元素乘积之和)
    :param a: 第一个向量 (列表)
    :param b: 第二个向量 (列表)
    :return: 两个向量对应元素乘积之和 (浮点数)
    """
    assert (len(a) == len(b))
    output = 0
    for i in range(len(a)):
        output += (a[i]*b[i])
    return output