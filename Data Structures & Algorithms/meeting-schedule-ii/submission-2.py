import heapq

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:

    def check_free_rooms(self, current_meetings, start, end):
        # current_meetings is a min-heap of (end, start); the earliest end is always at index 0
        curr_end, curr_start = current_meetings[0]
        if start >= curr_end:
            heapq.heapreplace(current_meetings, (end, start))  # pop the earliest end, push the new meeting
            return current_meetings, True
        return current_meetings, False

    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        min_rooms = 0
        current_meetings = []
        intervals = sorted(intervals, key=lambda x: x.start)
        for meeting in intervals:
            start, end = meeting.start, meeting.end
            if current_meetings:
                current_meetings, is_available = self.check_free_rooms(current_meetings, start, end)
                if not is_available:
                    heapq.heappush(current_meetings, (end, start))
                    min_rooms += 1
            else:
                heapq.heappush(current_meetings, (end, start))
                min_rooms += 1
        return min_rooms