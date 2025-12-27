import java.util.*;

class Solution {
    public int mostBooked(int n, int[][] meetings) {
        Arrays.sort(meetings, (a, b) -> a[0] - b[0]);

        // available rooms (min room number first)
        PriorityQueue<Integer> free = new PriorityQueue<>();
        for (int i = 0; i < n; i++) free.add(i);

        // busy rooms: [endTime, roomNumber]
        PriorityQueue<long[]> busy =
                new PriorityQueue<>((a, b) -> a[0] == b[0]
                        ? (int)(a[1] - b[1])
                        : (int)(a[0] - b[0]));

        int[] count = new int[n];

        for (int[] m : meetings) {
            long start = m[0], end = m[1];
            long duration = end - start;

            // free rooms that finished before current start
            while (!busy.isEmpty() && busy.peek()[0] <= start) {
                free.add((int) busy.poll()[1]);
            }

            if (!free.isEmpty()) {
                int room = free.poll();
                busy.add(new long[]{end, room});
                count[room]++;
            } else {
                long[] earliest = busy.poll();
                long newEnd = earliest[0] + duration;
                busy.add(new long[]{newEnd, earliest[1]});
                count[(int) earliest[1]]++;
            }
        }

        int ans = 0;
        for (int i = 1; i < n; i++) {
            if (count[i] > count[ans]) ans = i;
        }
        return ans;
    }
}
