class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Start with the first element of the row, which is always 1
        row = [1]
        
        for k in range(1, rowIndex + 1):
            # Calculate the next element based on the previous element
            # formula: previous * (n - k + 1) // k
            next_val = row[-1] * (rowIndex - k + 1) // k
            row.append(next_val)
            
        return row