class Solution {
    public int countCoveredBuildings(int n, int[][] buildings) {
        int[] minRow = new int[n+1];
        int[] maxRow = new int[n+1];
        int[] minCol = new int[n+1];
        int[] maxCol = new int[n+1];

        Arrays.fill(minRow, Integer.MAX_VALUE);
        Arrays.fill(minCol, Integer.MAX_VALUE);
        Arrays.fill(maxRow, -1);
        Arrays.fill(maxCol, -1);

        // Step 1: store min/max values for rows and columns
        for (int[] b : buildings) {
            int x = b[0], y = b[1];

            minRow[y] = Math.min(minRow[y], x);
            maxRow[y] = Math.max(maxRow[y], x);

            minCol[x] = Math.min(minCol[x], y);
            maxCol[x] = Math.max(maxCol[x], y);
        }

        // Step 2: Check coverage
        int count = 0;
        for (int[] b : buildings) {
            int x = b[0], y = b[1];

            if (minRow[y] < x && x < maxRow[y] &&
                minCol[x] < y && y < maxCol[x]) {
                count++;
            }
        }

        return count;
    }
}
