class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        length=len(intervals)
        if length>1:
            intervals=sorted(intervals,key=lambda x:x[0])
            purge=0
            
            i,j=0,1
            while j<length-purge and i<j:
                if intervals[i][1]>=intervals[j][0]:
                    
                    new_interval=[intervals[i][0],max(intervals[i][1],intervals[j][1])]
                    intervals[:]=intervals[:i]+[new_interval]+intervals[j+1:]
                    purge+=1
                else:
                    j+=1
                    i+=1


        return intervals