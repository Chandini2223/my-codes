class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Convert strings to integers
        a = int(num1)
        b = int(num2)
        # Multiply and convert back to string
        return str(a * b)

# Example usage:
sol = Solution()
param_1 = "2"
param_2 = "3"
ret = sol.multiply(param_1, param_2)
print(ret)  # Output: "6"
