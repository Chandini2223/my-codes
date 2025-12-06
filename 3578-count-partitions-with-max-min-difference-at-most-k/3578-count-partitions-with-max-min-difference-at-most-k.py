from collections import deque

class Solution(object):
    def countPartitions(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        # r_exclusive[i] = smallest index e (> i or ==i) such that segment nums[i:e] is maximal valid (e is exclusive)
        r_exclusive = [0] * n

        maxdq = deque()   # store indices, front = index of current max
        mindq = deque()   # store indices, front = index of current min
        r = 0

        # two-pointer to compute r_exclusive for every l
        for l in range(n):
            # expand r while the segment [l..r] (inclusive) remains valid
            while r < n:
                x = nums[r]
                # update max deque
                while maxdq and nums[maxdq[-1]] <= x:
                    maxdq.pop()
                maxdq.append(r)
                # update min deque
                while mindq and nums[mindq[-1]] >= x:
                    mindq.pop()
                mindq.append(r)

                # if invalid, undo adding r and stop expanding
                if nums[maxdq[0]] - nums[mindq[0]] > k:
                    if maxdq and maxdq[-1] == r:
                        maxdq.pop()
                    if mindq and mindq[-1] == r:
                        mindq.pop()
                    break
                r += 1

            # now r is exclusive end for start l
            r_exclusive[l] = r

            # move left pointer forward: if l was at front of any deque, pop it
            if maxdq and maxdq[0] == l:
                maxdq.popleft()
            if mindq and mindq[0] == l:
                mindq.popleft()

        # dp[i] = number of ways to partition suffix starting at i
        # dp[n] = 1 (empty suffix)
        dp = [0] * (n + 1)
        dp[n] = 1
        # prefix[i] = sum of dp[i]..dp[n]  (prefix from i to end)
        prefix = [0] * (n + 2)
        prefix[n] = dp[n]  # =1
        prefix[n+1] = 0

        # compute dp from right to left
        for i in range(n - 1, -1, -1):
            e = r_exclusive[i]            # exclusive end index
            # dp[i] = sum_{t = i+1 .. e} dp[t] = prefix[i+1] - prefix[e+1]
            dp_val = (prefix[i+1] - prefix[e+1]) % MOD
            dp[i] = dp_val
            prefix[i] = (dp[i] + prefix[i+1]) % MOD

        return dp[0]
