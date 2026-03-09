""" 这是前端层,本文件实现功能如下:
1,完成矩阵绘制
2.完成排序的动画绘制
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from utility import get_color_by_status

def init_visualizer(arr_len: int, max_val: int) -> tuple:
    """
    初始化可视化画布和柱子对象
    :param arr_len: 数组长度
    :param max_val: 数组元素最大值
    :return: (fig, ax, bars) 画布、轴、柱子对象
    """
    # 创建画布和绘图轴
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_title("Sorting Visualization", fontsize=14)
    ax.set_xlabel("Index", fontsize=12)
    ax.set_ylabel("Value", fontsize=12)
    # 隐藏x轴刻度，避免干扰视觉
    ax.set_xticks([])
    # 固定y轴范围，避免动画过程中y轴跳动
    ax.set_ylim(0, max_val + 10)

    # 初始化柱子：初始高度为0，颜色为待排序的浅蓝色
    init_arr = [0] * arr_len
    init_colors = [get_color_by_status(0)] * arr_len
    bars = ax.bar(
        range(arr_len),
        init_arr,
        color=init_colors,
        width=0.8
    )
    return fig, ax, bars

def update_frame(bars, arr: list, status_arr: list) -> None:
    """
    根据当前数组和状态数组更新柱子的高度和颜色
    :param bars: 柱子对象集合
    :param arr: 当前数组
    :param status_arr: 当前状态数组
    :return: None
    """
    for i, (bar, val, status) in enumerate(zip(bars, arr, status_arr)):
        # 更新柱子高度
        bar.set_height(val)
        # 根据状态码更新柱子颜色
        bar.set_color(get_color_by_status(status))

def run_animation(step_generator, fig, ax, bars, interval: int = 100) -> None:
    """
    运行排序可视化动画
    :param step_generator: 排序分步生成器
    :param fig: 画布
    :param ax: 轴
    :param bars: 柱子对象
    :param interval: 帧间隔，毫秒，默认100
    :return: None
    """
    # 在画布右上角添加性能文本，显示耗时、比较次数、交换次数
    performance_text = ax.text(
        0.8, 0.95,
        "",
        transform=ax.transAxes,
        ha="center",
        fontsize=12
    )

    # 动画每帧的更新函数
    def animate(frame_data):
        arr, status_arr, perf = frame_data
        # 更新柱子的高度和颜色
        update_frame(bars, arr, status_arr)
        # 更新性能文本
        performance_text.set_text(
            f"Time: {perf['time']:.2f}s | Compare: {perf['compare']} | Swap: {perf['swap']}"
        )
        # 修复：将BarContainer转换为列表，加上文本对象，返回所有需要更新的Artist
        return list(bars) + [performance_text]

    # 修复：添加cache_frame_data=False解决缓存警告
    ani = animation.FuncAnimation(
        fig,
        animate,
        frames=step_generator,
        interval=interval,
        repeat=False,
        blit=True,
        cache_frame_data=False
    )

    # 显示动画
    plt.tight_layout()
    plt.show()