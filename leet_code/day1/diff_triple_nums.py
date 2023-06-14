from typing import List


def get_diff_triple_nums(nums):
    triples = []
    for index in range(len(nums)):
        for index2 in range(index + 1, len(nums)):
            for index3 in range(index2 + 1, len(nums)):
                if len(set([nums[index], nums[index2], nums[index3]])) == 3:
                    triples.append(tuple([index, index2, index3]))
    return len(triples)


if __name__ == "__main__":
    nums = [4, 4, 2, 4, 3]
    [2, 3, 4, 4, 4]
    print(get_diff_triple_nums(nums))
