class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            # Per constraints, x is non-negative, but for safety
            raise ValueError("Input must be non-negative")
        
        if x == 0 or x == 1:
            return x

        # Initialize the search range
        left = 1
        right = x
        result = 0

        # Binary Search
        while left <= right:
            # Calculate mid point
            mid = left + (right - left) // 2
            
            # Since x is an int, mid * mid must be compared carefully
            # to avoid overflow if x was much larger (though python handles large ints,
            # we adhere to the spirit of the constraint which is based on 32-bit integer limits).
            # For this problem's constraint (2^31 - 1), direct multiplication is safe in Python,
            # but we can use a temporary variable for clarity.
            mid_squared = mid * mid

            if mid_squared == x:
                # Exact match found
                return mid
            
            elif mid_squared < x:
                # mid is a potential answer (k^2 <= x). Save it and search higher.
                result = mid
                left = mid + 1
            
            else:
                # mid is too large (mid^2 > x). Search lower.
                right = mid - 1
        
        # 'result' holds the largest integer k such that k*k <= x
        return result
        