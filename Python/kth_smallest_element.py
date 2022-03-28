
def partition(nums, first, last):
    choose_pivot(nums)
    pivot = nums[first]
    lasts1 = first
    firstUnknown = first + 1
    while firstUnknown <= last:
        if nums[firstUnknown] < pivot:
            lasts1 += 1
            nums[firstUnknown], nums[lasts1] = nums[lasts1], nums[firstUnknown]

        firstUnknown += 1
    nums[lasts1], nums[first] = nums[first], nums[lasts1]
    return lasts1


def kth_min_element(nums, first, last, k):
    pivotIndex = partition(nums, first, last)
    k -= k
    if k == pivotIndex:
        print(nums[k])
    elif k < pivotIndex:
        kth_min_element(nums, first, pivotIndex - 1, k)
    else:
        kth_min_element(nums, pivotIndex + 1, last, k)
