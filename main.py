"""这是入口层,他将会集成我们设计的所有接口,也就是将各个零部件组合起来组成成一台有实际功能可以运行的机器
   我们在这里启动我们整个程序.
"""
from sort_algorithms import direct_insert_sort_step,half_insert_sort_step,shell_sort_step,bubble_sort_step,quick_sort_step,selection_sort_step,heap_sort_step,merge_sort_step,radix_sort_step,get_performance
from utility import generate_random_arr
from visualizer import  init_visualizer,run_animation

def get_selected_sort_algorithm():
    """
    交互式排序算法选择菜单：让用户选择要可视化的排序算法
    :return: 选中的排序算法函数(如selection_sort_step)
    """
    # 算法映射：键=选项编号，值=(算法名称, 算法函数)
    sort_algorithms = {
        1:("直接插入排序",direct_insert_sort_step),
        2:("折半插入排序",half_insert_sort_step),
        3:("希尔排序",shell_sort_step),
        4:("冒泡排序",bubble_sort_step),
        5:("快速排序",quick_sort_step),
        6:("简单选择排序",selection_sort_step),
        7:("堆排序",heap_sort_step),
        8:("归并排序",merge_sort_step),
        9:("基数排序",radix_sort_step)
    }

    # 显示选择菜单
    print("="*50)
    print("        排序可视化 - 算法选择")
    print("="*50)
    for idx, (alg_name, _) in sort_algorithms.items():
        print(f"[{idx}] {alg_name}")
    print("="*50)

    # 处理用户输入，防止非法输入
    while True:
        try:
            choice = int(input("请输入算法编号（1/9）："))
            if choice in sort_algorithms:
                selected_name = sort_algorithms[choice][0]
                print(f"\n✅ 已选择：{selected_name}")
                return sort_algorithms[choice][1]
            else:
                print(f"❌ 无效编号！请输入1-{len(sort_algorithms)}之间的数字")
        except ValueError:
            print("❌ 输入错误！请输入数字（如1、2）")

def main():
    """
    入口函数，集成所有模块运行排序可视化
    """
    # 1. 第一步：选择排序算法
    sort_func = get_selected_sort_algorithm()

    # 2. 配置参数（可根据需要修改）
    arr_length = 100  # 数组长度（越大动画越慢）
    max_val = 100    # 数组元素最大值
    frame_interval = 0.001 # 动画帧间隔（毫秒，越小动画越快）

    # 3. 工具层：生成随机数组
    random_arr = generate_random_arr(arr_length, max_val)
    print(f"\n🔢 生成随机数组（长度{arr_length}，前10个元素）：{random_arr[:10]}...")

    # 4. 后端：获取排序分步生成器
    step_generator = sort_func(random_arr)

    # 5. 前端：初始化可视化
    fig, ax, bars = init_visualizer(arr_length, max_val)

    # 6. 运行动画
    print("\n🎬 开始可视化（关闭窗口后显示性能统计）...")
    run_animation(step_generator, fig, ax, bars, frame_interval)

    # 7. 输出最终性能统计
    final_perf = get_performance(sort_func, random_arr)
    print(f"\n🏁 排序完成！性能统计：")
    print(f"耗时：{final_perf['time']:.2f}秒 | 比较次数：{final_perf['compare']} | 交换次数：{final_perf['swap']}")

if __name__ == "__main__":
    main()