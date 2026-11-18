class MovingAverage:

    def __init__(self, size: int):
        self.size=size
        self.nums=[]
        self.rolling_sum=0
        

    def next(self, val: int) -> float:
        if len(self.nums)>=self.size:
            popped=self.nums.pop(0)
            self.rolling_sum-=popped
            self.nums.append(val)
            self.rolling_sum+=val
        else:
            self.nums.append(val)
            self.rolling_sum+=val
        return self.rolling_sum/len(self.nums)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
