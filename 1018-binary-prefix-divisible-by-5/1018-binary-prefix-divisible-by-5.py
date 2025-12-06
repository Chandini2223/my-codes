class Solution(object):
    def prefixesDivBy5(self, nums):
        val = 0
        ans = []
        for b in nums:
            val = (val * 2 + b) % 5
            ans.append(val == 0)
        return ans
