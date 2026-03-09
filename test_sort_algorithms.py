import pytest
from src.sort_algorithms import selection_sort_step, bubble_sort_step, get_performance

# 参数化测试：测试不同排序算法对不同数组的排序正确性
@pytest.mark.parametrize(
    "sort_func, input_arr, expected_arr",
    [
        (selection_sort_step, [5, 3, 1, 4, 2], [1, 2, 3, 4, 5]),
        (bubble_sort_step, [5, 3, 1, 4, 2], [1, 2, 3, 4, 5]),
        (selection_sort_step, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # 已排序数组
        (bubble_sort_step, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        (selection_sort_step, [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # 逆序数组
        (bubble_sort_step, [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ]
)
def test_sort_correctness(sort_func, input_arr, expected_arr):
    """测试排序算法的最终结果是否正确"""
    step_generator = sort_func(input_arr.copy())
    final_arr = None
    for arr, _, _ in step_generator:
        final_arr = arr
    assert final_arr == expected_arr



