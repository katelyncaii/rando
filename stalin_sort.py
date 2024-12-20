#Stalin Sort

def stalin_sort(nums):
    new_nums = [None for i in range(len(nums))]
    new_nums[0] = nums[0]
    pointer = 1
    for i in range(1,len(nums)):
        if nums[i] < new_nums[pointer-1]:
            continue
        new_nums[pointer] = nums[i]
        pointer += 1
    return new_nums[0:pointer]

#tests?
h = [1,2,3,4,5]
stalined_h = stalin_sort(h)
assert stalined_h == h

i = [1,2,4,3,5]
stalined_i = stalin_sort(i)
assert stalined_i == [1,2,4,5]

j = [5,1,2,3,4]
stalined_j = stalin_sort(j)
assert stalined_j == [5]

k = [3,1,2,6,5,9,8]
stalined_k = stalin_sort(k)
assert stalined_k == [3,6,9]