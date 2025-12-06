class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove trailing spaces
        s = s.rstrip()
        # Split by spaces and get last word
        words = s.split(' ')
        return len(words[-1])
