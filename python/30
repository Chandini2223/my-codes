class Solution:
    MOD = 10**9 + 7

    def countPermutations(self, complexity):
        n = len(complexity)
        if n == 0:
            return 0

        # If complexity[0] is not strictly smaller than all others -> impossible
        first = complexity[0]
        # quick check: is first the strict global minimum?
        for x in complexity[1:]:
            if x <= first:
                return 0

        # else answer = (n-1)! % MOD
        ans = 1
        for i in range(2, n):    # multiply 2 * 3 * ... * (n-1)
            ans = (ans * i) % self.MOD
        return ans
