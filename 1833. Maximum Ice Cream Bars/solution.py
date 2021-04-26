class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ic = 0
        while coins>0 and len(costs)!=0:
            c = costs.pop(0)
            if c<=coins:
                ic+=1
                coins-=c
            else:   
                break
        return ic
        
