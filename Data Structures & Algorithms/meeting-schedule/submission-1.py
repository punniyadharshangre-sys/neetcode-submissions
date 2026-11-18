"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals)>=1:
            intervals=sorted(intervals,key=lambda x:x.start)
            curr=intervals[0]
            for meeting in intervals[1:]:
                if meeting.start<curr.end:
                    return False
                curr=meeting
            return True
        else:
            return True
        