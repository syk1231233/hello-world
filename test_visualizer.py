import pytest
import matplotlib.pyplot as plt
from src.visualizer import init_visualizer, update_frame
from src.utility import get_color_by_status

def test_init_visualizer():
    """测试可视化初始化是否正确"""
    arr_len = 5
    max_val = 100
    fig, ax, bars = init_visualizer(arr_len, max_val)
    # 检查画布、轴、柱子对象是否非空
    assert fig is not None
    assert ax is not None
    assert len(bars) == arr_len
    # 检查y轴范围是否正确
    assert ax.get_ylim() == (0, max_val + 10)
    # 检查初始柱子颜色是否为待排序的浅蓝色
    for bar in bars:
        assert bar.get_color() == get_color_by_status(0)
    plt.close(fig)

def test_update_frame():
    """测试帧更新是否正确"""
    arr_len = 5
    max_val = 100
    fig, ax, bars = init_visualizer(arr_len, max_val)
    # 测试数据
    test_arr = [1, 5, 3, 4, 2]
    test_status = [3, 2, 1, 1, 0]
    # 更新帧
    update_frame(bars, test_arr, test_status)
    # 检查柱子高度和颜色是否正确
    for i, (bar, val, status) in enumerate(zip(bars, test_arr, test_status)):
        assert bar.get_height() == val
        assert bar.get_color() == get_color_by_status(status)
    plt.close(fig)