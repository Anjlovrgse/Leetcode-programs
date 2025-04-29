class Solution(object):
    def twoSum(self, nums, target):
      
        prev_map = {}  # Dictionary to store the indices of numbers

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[num] = i
        return []  # Return an empty list if no solution is found
    

    

#Iteration steps,if target is 9:

#i=0, num=2 → diff = 7 → 7 not in prev_map → store 2:0

#i=1, num=7 → diff = 2 → 2 is in prev_map → return [0, 1]