class Solution:
    def specialTriplets(self, nums):
        MOD = 10**9 + 7
        from collections import Counter

        right = Counter(nums)
        left = Counter()
        ans = 0

        for j in range(len(nums)):
            right[nums[j]] -= 1
            target = nums[j] * 2

            ans = (ans + left[target] * right[target]) % MOD

            left[nums[j]] += 1

        return ans % MOD
