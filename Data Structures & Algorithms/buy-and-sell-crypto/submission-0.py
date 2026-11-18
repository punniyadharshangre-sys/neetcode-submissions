class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length=len(prices)
        profit=0
        if length>1:
            i,j=0,1
            while j<length:
                temp=prices[j]-prices[i]
                if temp>0:
                    profit=max(profit,temp)
                else:
                    i=j
                j+=1
        return profit



        