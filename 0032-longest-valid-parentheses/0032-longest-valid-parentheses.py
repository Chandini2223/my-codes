class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]  # Initialize stack with -1 for base index
        max_len = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Push index of '('
            else:
                stack.pop()  # Pop matching '('
                if not stack:
                    stack.append(i)  # Reset base index
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len
