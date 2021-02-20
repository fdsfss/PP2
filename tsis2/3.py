class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        k = i = j = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j and nums[i] == nums[j]:
                    k += 1
        return k