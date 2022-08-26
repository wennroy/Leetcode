import time

def sort_and_concat_list(nums, l, r):
    sorted_arr = sorted(nums[l:r+1])
    return nums[:l] + sorted_arr + nums[r+1:]

def sort_and_alter_list(nums, l, r):
    sorted_arr = sorted(nums[l:r+1])
    nums[l:r+1] = sorted_arr
    return nums

def sort_list(nums, l, r):
    nums[l:r].sort()
    return nums

def sorted_list(nums, l, r):
    nums[l:r] = sorted(nums[l:r])
    return nums


if __name__ == '__main__':
    start_time = time.time()
    nums = list(range(1000000, -1, -1))
    sort_and_concat_list(nums, 250000, 750000)
    print(f"Elapsed {time.time() - start_time}s")

    start_time = time.time()
    nums = list(range(1000000, -1, -1))
    sort_and_alter_list(nums, 250000, 750000)
    print(f"Elapsed {time.time() - start_time}s")

    start_time = time.time()
    nums = list(range(1000000, -1, -1))
    sort_list(nums, 250000, 750000)
    print(f"Elapsed {time.time() - start_time}s")

    start_time = time.time()
    nums = list(range(1000000, -1, -1))
    sorted_list(nums, 250000, 750000)
    print(f"Elapsed {time.time() - start_time}s")


    # Elapsed 0.03760814666748047s
    # Elapsed 0.02990889549255371s
    # Elapsed 0.022216796875s
    # Elapsed 0.028279781341552734s