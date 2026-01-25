class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # 1. Convert to set for O(1) lookups
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # 2. Check if 'num' is the start of a sequence
            # (i.e., the number before it doesn't exist)
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # 3. Count how long this sequence lasts
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # Update the global maximum
                longest_streak = max(longest_streak, current_streak)

        return longest_streak