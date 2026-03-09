""" 这是后端层,该文件负责完成所有排序算法设计
    用生成器分步返回排序状态,使得前端可以逐帧更新动画,进而完成排序动画演示
"""
import time
def swap(a: int, b: int, arr: list) -> None:
    """
    实现两个数组元素交换位置
    参数:
    a,b为交换元素的位序
    arr为数组
    """
    cache=arr[a]
    arr[a]=arr[b]
    arr[b]=cache
    return None

def init_sort(arr:list)->list:
    """
    实现排序的初始化,初始化所有通信参数,直接放置在任意排序算法第一行即可,序列解包获取参数
    """
    sort_arr=arr.copy()
    n=len(sort_arr)
    staus_arr=[0]*n #将所有数组标记为待排序状态
    compare_count=0
    swap_count=0
    start_time=time.time()
    return [sort_arr,n,staus_arr,compare_count,swap_count,start_time]

#插入排序:每次将一个代排序的记录按其关键字大小插入到前面已经排好序的子序列中,直到全部记录插入完成
def direct_insert_sort_step(arr:list) -> tuple:
    """
    直接插入排序:
        不断将第i个元素插入到前i-1个元素中
    参数: 
        arr:随机数组
    返回值:
        当前状态数组,标记了所有数组的排序状态
        当前数组,标记了所有数组的数值信息
        比较次数
        时间差
        交换次数
    """
    sort_arr,n,staus_arr,compare_count,swap_count,start_time=init_sort(arr)
    #开始直接插入排序
    """ 1. 选中第i个元素,我们现在要将其插入到前i-1个元素中
        2. 将第i个元素和前i-1个元素逐个对比,如果第i个元素更小,那么当前比对元素向后移一个
    """
    for i in range(1,n):
        staus_arr[i]=2
        cache= sort_arr[i]
        aim_position=i-1
        while sort_arr[aim_position] > cache and aim_position>=0:
            compare_count+=1
            swap_count+=1
            sort_arr[aim_position+1]=sort_arr[aim_position]
            aim_position-=1
        sort_arr[aim_position+1]=cache
        staus_arr[i]=3
        #向前端通信,返回当前性能数据
        performance={
            "time": time.time()-start_time,
            "compare": compare_count,
            "swap": swap_count
        }
        yield sort_arr.copy(),staus_arr.copy(),performance
    staus_arr = [3] * n
    current_time = time.time() - start_time
    performance = {
        "time": current_time,
        "compare": compare_count,
        "swap": swap_count
    }
    yield sort_arr.copy(), staus_arr.copy(), performance
    
def half_insert_sort_step(arr: list)->tuple:
    """
    折半插入排序:  优化了直接插入的查找过程,本次采用折半查找找到该插入的位置
            1.确定有序数组左边界low,右边界high
            2.mid=low+high/2 得到中间值,如果中间值比当前值大,那么high=mid-1,比当前值小,那么low=mid+1
            3.重复直到high<left,将hjgh+1到原来的high都向右移动
    参数:
        arr:随机数组
    返回值:
        当前状态数组,标记了所有数组的排序状态
        当前数组,标记了所有数组的数值信息
        比较次数
        时间差
        交换次数 
    """
    sort_arr,n,staus_arr,compare_count,swap_count,start_time=init_sort(arr)
    #开始排序
    for i in range(1,n):
        cache=sort_arr[i]
        staus_arr[i]=2
        low=0
        high=i-1
        while low <= high:
            mid=(low+high)//2
            if cache < sort_arr[mid]:
                high=mid-1
            else:
                low=mid+1
            compare_count+=1
        index=i-1
        while index>=(high+1):
            sort_arr[index+1]=sort_arr[index]
            swap_count+=1
            index-=1
        sort_arr[high+1]=cache
        staus_arr[i]=3
        #向前端通信,返回当前性能数据
        performance={
            "time": time.time()-start_time,
            "compare": compare_count,
            "swap": swap_count
        }
        yield sort_arr.copy(),staus_arr.copy(),performance
    staus_arr = [3] * n
    current_time = time.time() - start_time
    performance = {
        "time": current_time,
        "compare": compare_count,
        "swap": swap_count
    }
    yield sort_arr.copy(), staus_arr.copy(), performance

import time  # 确保导入time模块

# 先确保init_sort函数已定义（如果还没定义）
def init_sort(arr: list) -> tuple:
    sort_arr = arr.copy()
    n = len(sort_arr)
    status_arr = [0] * n  # 0:待排序 1:比较中 2:当前操作 3:已排序
    compare_count = 0
    swap_count = 0
    start_time = time.time()
    return sort_arr, n, status_arr, compare_count, swap_count, start_time

def bubble_sort_step(arr: list) -> tuple:
    """
    冒泡排序分步实现，完全贴合你的代码流程
    """
    sort_arr, n, status_arr, compare_count, swap_count, start_time = init_sort(arr)
    
    for i in range(n-1):
        # 标记本轮要确定的最终位置为「当前操作」
        status_arr[n-1 - i] = 2
        swapped = False
        
        # 遍历未排序部分，相邻元素比较
        for j in range(n-1 - i):
            # 标记当前比较的两个元素为「比较中」
            status_arr[j] = 1
            status_arr[j+1] = 1
            compare_count += 1
            
            if sort_arr[j] > sort_arr[j+1]:
                # 交换元素
                sort_arr[j], sort_arr[j+1] = sort_arr[j+1], sort_arr[j]
                swap_count += 1
                swapped = True
                # 标记交换的元素为「当前操作」
                status_arr[j] = 2
                status_arr[j+1] = 2
                
                # 向前端通信，返回当前状态
                performance = {
                    "time": time.time()-start_time,
                    "compare": compare_count,
                    "swap": swap_count
                }
                yield sort_arr.copy(), status_arr.copy(), performance
            
            # 恢复比较元素的状态为「待排序」
            status_arr[j] = 0
            status_arr[j+1] = 0
        
        # 标记本轮确定的元素为「已排序」
        status_arr[n-1 - i] = 3
        
        # 如果本轮没有交换，说明数组已经有序，提前退出
        if not swapped:
            break
        
        # 每轮结束后向前端通信
        performance = {
            "time": time.time()-start_time,
            "compare": compare_count,
            "swap": swap_count
        }
        yield sort_arr.copy(), status_arr.copy(), performance
    
    # 排序完成，所有元素标记为「已排序」
    status_arr = [3] * n
    current_time = time.time() - start_time
    performance = {
        "time": current_time,
        "compare": compare_count,
        "swap": swap_count
    }
    yield sort_arr.copy(), status_arr.copy(), performance

def shell_sort_step(arr: list) -> tuple:
    """
    希尔排序分步实现，完全贴合你的代码流程
    """
    sort_arr, n, status_arr, compare_count, swap_count, start_time = init_sort(arr)
    
    # 生成希尔增量序列：n/2 → n/4 → ... → 1
    gap = n // 2
    
    while gap > 0:
        # 按增量分组，每组进行插入排序
        for i in range(gap, n):
            cache = sort_arr[i]
            status_arr[i] = 2  # 标记当前操作的元素
            j = i
            
            # 分组插入排序：向前找插入位置
            while j >= gap:
                compare_count += 1
                status_arr[j - gap] = 1  # 标记比较中的元素
                
                if cache < sort_arr[j - gap]:
                    # 移动元素
                    sort_arr[j] = sort_arr[j - gap]
                    swap_count += 1
                    status_arr[j] = 1  # 标记移动的元素
                    j -= gap
                    
                    # 向前端通信
                    performance = {
                        "time": time.time()-start_time,
                        "compare": compare_count,
                        "swap": swap_count
                    }
                    yield sort_arr.copy(), status_arr.copy(), performance
                else:
                    # 找到插入位置，恢复比较状态
                    status_arr[j - gap] = 0
                    break
            
            # 把当前元素插入到正确位置
            sort_arr[j] = cache
            status_arr[i] = 3  # 标记当前元素为已排序
            # 恢复所有临时标记的状态
            for k in range(j, i+1):
                if status_arr[k] == 1:
                    status_arr[k] = 0
        
        # 每轮增量处理完后向前端通信
        performance = {
            "time": time.time()-start_time,
            "compare": compare_count,
            "swap": swap_count
        }
        yield sort_arr.copy(), status_arr.copy(), performance
        
        # 缩小增量
        gap = gap // 2
    
    # 排序完成，所有元素标记为「已排序」
    status_arr = [3] * n
    current_time = time.time() - start_time
    performance = {
        "time": current_time,
        "compare": compare_count,
        "swap": swap_count
    }
    yield sort_arr.copy(), status_arr.copy(), performance

def quick_sort_step(arr: list) -> tuple:
    """
    快速排序分步实现，完全贴合你的代码流程
    """
    sort_arr, n, status_arr, compare_count, swap_count, start_time = init_sort(arr)
    
    # 用栈保存待排序区间，避免递归无法分步yield
    stack = [(0, n-1)]
    
    while stack:
        left, right = stack.pop()
        if left >= right:
            continue
        
        # 标记基准元素为「当前操作」
        pivot_val = sort_arr[left]
        status_arr[left] = 2
        i, j = left, right
        
        # 分区过程
        while i < j:
            # 从右往左找小于基准的元素
            while i < j:
                compare_count += 1
                status_arr[j] = 1  # 标记为比较中
                if sort_arr[j] < pivot_val:
                    sort_arr[i] = sort_arr[j]
                    swap_count += 1
                    i += 1
                    status_arr[j] = 0  # 恢复比较状态
                    break
                status_arr[j] = 0
                j -= 1
            
            # 从左往右找大于基准的元素
            while i < j:
                compare_count += 1
                status_arr[i] = 1  # 标记为比较中
                if sort_arr[i] > pivot_val:
                    sort_arr[j] = sort_arr[i]
                    swap_count += 1
                    j -= 1
                    status_arr[i] = 0  # 恢复比较状态
                    break
                status_arr[i] = 0
                i += 1
        
        # 把基准放到正确位置
        sort_arr[i] = pivot_val
        status_arr[i] = 3  # 标记基准为已排序
        status_arr[left] = 0  # 恢复原基准位置状态
        
        # 向前端通信
        performance = {
            "time": time.time()-start_time,
            "compare": compare_count,
            "swap": swap_count
        }
        yield sort_arr.copy(), status_arr.copy(), performance
        
        # 左右区间入栈，继续排序
        stack.append((left, i-1))
        stack.append((i+1, right))
    
    # 排序完成，所有元素标记为已排序
    status_arr = [3] * n
    current_time = time.time() - start_time
    performance = {
        "time": current_time,
        "compare": compare_count,
        "swap": swap_count
    }
    yield sort_arr.copy(), status_arr.copy(), performance

def selection_sort_step(arr: list) -> tuple:
    """
    简单选择排序分步实现，完全贴合你的代码流程
    """
    sort_arr, n, status_arr, compare_count, swap_count, start_time = init_sort(arr)
    
    for i in range(n-1):
        # 标记当前边界为「当前操作」
        status_arr[i] = 2
        min_idx = i
        
        # 找未排序部分的最小值
        for j in range(i+1, n):
            compare_count += 1
            status_arr[j] = 1  # 标记为比较中
            if sort_arr[j] < sort_arr[min_idx]:
                status_arr[min_idx] = 0  # 恢复原最小值状态
                min_idx = j
                status_arr[min_idx] = 2  # 标记新最小值为当前操作
            else:
                status_arr[j] = 0  # 恢复比较状态
        
        # 交换当前边界和最小值
        if min_idx != i:
            sort_arr[i], sort_arr[min_idx] = sort_arr[min_idx], sort_arr[i]
            swap_count += 1
            status_arr[min_idx] = 0  # 恢复最小值位置状态
        
        # 标记当前边界为已排序
        status_arr[i] = 3
        
        # 向前端通信
        performance = {
            "time": time.time()-start_time,
            "compare": compare_count,
            "swap": swap_count
        }
        yield sort_arr.copy(), status_arr.copy(), performance
    
    # 最后一个元素标记为已排序
    status_arr[-1] = 3
    current_time = time.time() - start_time
    performance = {
        "time": current_time,
        "compare": compare_count,
        "swap": swap_count
    }
    yield sort_arr.copy(), status_arr.copy(), performance

def heap_sort_step(arr: list) -> tuple:
    """
    堆排序分步实现，完全贴合你的代码流程
    """
    sort_arr, n, status_arr, compare_count, swap_count, start_time = init_sort(arr)
    
    # 建大顶堆
    for i in range(n//2 - 1, -1, -1):
        status_arr[i] = 2  # 标记当前调整节点为当前操作
        j = i
        while True:
            left = 2*j + 1
            right = 2*j + 2
            largest = j
            
            # 比较左孩子
            if left < n:
                compare_count += 1
                status_arr[left] = 1  # 标记为比较中
                if sort_arr[left] > sort_arr[largest]:
                    largest = left
                status_arr[left] = 0  # 恢复比较状态
            
            # 比较右孩子
            if right < n:
                compare_count += 1
                status_arr[right] = 1  # 标记为比较中
                if sort_arr[right] > sort_arr[largest]:
                    largest = right
                status_arr[right] = 0  # 恢复比较状态
            
            if largest != j:
                # 交换节点
                sort_arr[j], sort_arr[largest] = sort_arr[largest], sort_arr[j]
                swap_count += 1
                status_arr[j] = 0  # 恢复原节点状态
                status_arr[largest] = 2  # 标记新节点为当前操作
                j = largest
                
                # 向前端通信
                performance = {
                    "time": time.time()-start_time,
                    "compare": compare_count,
                    "swap": swap_count
                }
                yield sort_arr.copy(), status_arr.copy(), performance
            else:
                status_arr[j] = 3  # 标记为已排序
                break
    
    # 堆排序主过程
    for i in range(n-1, 0, -1):
        # 交换堆顶和最后一个元素
        sort_arr[0], sort_arr[i] = sort_arr[i], sort_arr[0]
        swap_count += 1
        status_arr[0] = 2  # 标记堆顶为当前操作
        status_arr[i] = 3  # 标记已排序元素
        
        # 向前端通信
        performance = {
            "time": time.time()-start_time,
            "compare": compare_count,
            "swap": swap_count
        }
        yield sort_arr.copy(), status_arr.copy(), performance
        
        # 调整堆
        j = 0
        while True:
            left = 2*j + 1
            right = 2*j + 2
            largest = j
            
            # 比较左孩子
            if left < i:
                compare_count += 1
                status_arr[left] = 1  # 标记为比较中
                if sort_arr[left] > sort_arr[largest]:
                    largest = left
                status_arr[left] = 0  # 恢复比较状态
            
            # 比较右孩子
            if right < i:
                compare_count += 1
                status_arr[right] = 1  # 标记为比较中
                if sort_arr[right] > sort_arr[largest]:
                    largest = right
                status_arr[right] = 0  # 恢复比较状态
            
            if largest != j:
                sort_arr[j], sort_arr[largest] = sort_arr[largest], sort_arr[j]
                swap_count += 1
                status_arr[j] = 0  # 恢复原节点状态
                status_arr[largest] = 2  # 标记新节点为当前操作
                j = largest
                
                # 向前端通信
                performance = {
                    "time": time.time()-start_time,
                    "compare": compare_count,
                    "swap": swap_count
                }
                yield sort_arr.copy(), status_arr.copy(), performance
            else:
                status_arr[j] = 3  # 标记为已排序
                break
    
    # 排序完成
    status_arr[0] = 3
    current_time = time.time() - start_time
    performance = {
        "time": current_time,
        "compare": compare_count,
        "swap": swap_count
    }
    yield sort_arr.copy(), status_arr.copy(), performance

def merge_sort_step(arr: list) -> tuple:
    """
    归并排序分步实现，完全贴合你的代码流程
    """
    sort_arr, n, status_arr, compare_count, swap_count, start_time = init_sort(arr)
    
    # 迭代式归并，从长度1的子数组开始
    length = 1
    while length < n:
        for i in range(0, n, 2*length):
            left = i
            mid = i + length - 1
            right = min(i + 2*length - 1, n-1)
            
            # 标记当前合并区间为比较中
            for k in range(left, right+1):
                status_arr[k] = 1
            
            # 合并两个子数组
            temp = []
            i_left, i_right = left, mid+1
            
            while i_left <= mid and i_right <= right:
                compare_count += 1
                if sort_arr[i_left] <= sort_arr[i_right]:
                    temp.append(sort_arr[i_left])
                    i_left += 1
                else:
                    temp.append(sort_arr[i_right])
                    i_right += 1
                    swap_count += 1
            
            # 处理剩余元素
            while i_left <= mid:
                temp.append(sort_arr[i_left])
                i_left += 1
            while i_right <= right:
                temp.append(sort_arr[i_right])
                i_right += 1
            
            # 把合并结果放回原数组
            for k in range(left, right+1):
                sort_arr[k] = temp[k-left]
                status_arr[k] = 2  # 标记为当前操作
            
            # 向前端通信
            performance = {
                "time": time.time()-start_time,
                "compare": compare_count,
                "swap": swap_count
            }
            yield sort_arr.copy(), status_arr.copy(), performance
            
            # 标记合并区间为已排序
            for k in range(left, right+1):
                status_arr[k] = 3
        
        length *= 2
    
    # 排序完成
    current_time = time.time() - start_time
    performance = {
        "time": current_time,
        "compare": compare_count,
        "swap": swap_count
    }
    yield sort_arr.copy(), status_arr.copy(), performance

def radix_sort_step(arr: list) -> tuple:
    """
    基数排序分步实现，完全贴合你的代码流程
    """
    sort_arr, n, status_arr, compare_count, swap_count, start_time = init_sort(arr)
    
    # 找到最大值，确定最大位数
    max_val = max(sort_arr)
    digit = 1
    
    while max_val // digit > 0:
        # 初始化10个桶
        buckets = [[] for _ in range(10)]
        
        # 标记当前处理的元素为比较中
        for i in range(n):
            status_arr[i] = 1
        
        # 按当前位入桶
        for i in range(n):
            num = sort_arr[i]
            current_digit = (num // digit) % 10
            buckets[current_digit].append(num)
            status_arr[i] = 2  # 标记为当前操作
            compare_count += 1
            
            # 向前端通信
            performance = {
                "time": time.time()-start_time,
                "compare": compare_count,
                "swap": swap_count
            }
            yield sort_arr.copy(), status_arr.copy(), performance
        
        # 把桶中元素放回原数组
        index = 0
        for bucket in buckets:
            for num in bucket:
                sort_arr[index] = num
                status_arr[index] = 3  # 标记为已排序
                index += 1
                swap_count += 1
        
        # 向前端通信
        performance = {
            "time": time.time()-start_time,
            "compare": compare_count,
            "swap": swap_count
        }
        yield sort_arr.copy(), status_arr.copy(), performance
        
        digit *= 10
    
    # 排序完成
    current_time = time.time() - start_time
    performance = {
        "time": current_time,
        "compare": compare_count,
        "swap": swap_count
    }
    yield sort_arr.copy(), status_arr.copy(), performance

def selection_sort_step(arr: list) -> tuple:
    """
    实现选择排序
    1. 第i趟从未排序元素中找最小元素,不断将其标记为正在排序元素,
    2. 找到最小元素后,将其与位序为第i-1的数值进行交换
    参数:
        sort_arr 随机数组
    返回值:
        当前状态数组,标记了所有数组的排序状态
        当前数组,标记了所有数组的数值信息
        比较次数
        时间差
        交换次数
    """
    sort_arr,n,staus_arr,compare_count,swap_count,start_time=init_sort(arr)

    #开始选择排序
    for i in range(n-1): #一共进行n-1趟排序逐次进行返回更新动画
        index=i
        min_index=i
        min_value=sort_arr[i]
        staus_arr[i]=2 #将当前元素设置为正在排序
        while index<n-1:
            staus_arr[index+1]=1 #当前比较元素设置为比较中
            if sort_arr[index+1] < min_value:
                min_value=sort_arr[index+1]
                staus_arr[min_index]=0
                min_index=index+1
                staus_arr[index+1]=2
            else:
                staus_arr[index+1]=0
            index+=1
            compare_count+=1
        #选择到了最小值
        swap(i,min_index,sort_arr)
        swap_count+=1
        staus_arr[i]=3

        #向前端通信,返回当前性能数据
        performance={
            "time": time.time()-start_time,
            "compare": compare_count,
            "swap": swap_count
        }
        yield sort_arr.copy(),staus_arr.copy(),performance
    staus_arr = [3] * n
    current_time = time.time() - start_time
    performance = {
        "time": current_time,
        "compare": compare_count,
        "swap": swap_count
    }
    yield sort_arr.copy(), staus_arr.copy(), performance

def get_performance(sort_func, sort_arr: list) -> dict:
    """
    统计排序算法的最终性能数据
    :param sort_func: 排序函数（如selection_sort_step）
    :param sort_arr: 待排序数组
    :return: 最终性能字典
    """
    gen = sort_func(sort_arr.copy())
    final_perf = None
    for _, _, perf in gen:
        final_perf = perf
    return final_perf