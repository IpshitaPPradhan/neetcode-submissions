class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum = {}
        num_index = []
        index = 0
        for num in nums:
            diff = target - num
            if diff in two_sum:
                return [two_sum[diff], index]
            two_sum[num] = index
            two_sum.update({num: index})
            num_index = index
            index += 1
