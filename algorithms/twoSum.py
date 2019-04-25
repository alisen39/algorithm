# 两数相加

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return []


if __name__ == '__main__':
    a = Solution().twoSum([-3, 4, -2, 90], -5)
    print(a)
