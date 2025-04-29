class Solution(object):
    def twoSum(self, nums, target):
      
        prev_map = {}  # Dictionary to store the indices of numbers

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[num] = i
        return []  # Return an empty list if no solution is found
