def calculate_average(numbers):
    """
    计算列表的平均值
    :param numbers: 数字列表
    :return: 平均值，如果列表为空返回None
    """
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    # 测试代码
    test_list = [1, 2, 3, 4, 5]
    result = calculate_average(test_list)
    print(f"列表 {test_list} 的平均值是: {result}")