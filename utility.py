""" 这是工具层,提供其他层需要的泛用小功能
本文件提供接口如下
1. 随机数组生成
2. 颜色映射

"""
import random

def generate_random_arr(length: int, max_val: int = 100) -> list:
    """
    生成一个随机数数组
    参数:
        length: 数组的长度
        max_val: 数组的最值
    返回值:
        数组,包含length个int类型数据
    异常:
        ValueError 输入length小于等于0时     
    """
    if length <= 0:
        raise ValueError("数组长度必须大于0")
    return [random.randint(0, max_val) for _ in range(length)]

def get_color_by_status(status_code: int) -> str:
    """
    将状态数组中存储的状态码转化为前端层matplotlib绘图所需要的颜色
    参数:
        status_code 状态码
    返回值:
        字符串,存储绘图所需的颜色信息
    异常:
        当状态码异常的时候返回带排序颜色
    """
    color_map = {
        0: "lightskyblue",  # 0：待排序
        1: "orange",        # 1：比较中
        2: "red",           # 2：当前操作
        3: "forestgreen"    # 3：已排序
    }
    # 非法状态码返回默认待排序颜色
    return color_map.get(status_code, "lightskyblue")