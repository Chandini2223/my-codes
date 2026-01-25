class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        # Start with the bottom row as our DP base
        dp = triangle[-1][:]
        
        # Iterate from the second-to-last row up to the top
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # The min path for the current node is its value + 
                # the minimum of the two paths below it
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
        
        return dp[0]