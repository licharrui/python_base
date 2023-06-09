def get_target_nums(target, nums):
    dic = {}
    index_list = []
    for index, num in enumerate(nums):
        j = dic.get(target - num, -1)
        if j != -1:
            index_list.append([index, dic[target - num]])
        dic[num] = index
    return index_list


target = 9
nums = [2, 3, 6, 7, 9]

test = get_target_nums(target, nums)

print(test)
