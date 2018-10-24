class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for x in range(n):
            if (target - nums[x]) in nums:
                if not x == nums.index(target - nums[x]):
                    return x, nums.index(target - nums[x])
     