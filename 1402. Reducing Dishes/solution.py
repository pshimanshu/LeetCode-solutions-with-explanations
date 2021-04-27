class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        def recur(i, t):
            if i >= len(satisfaction):
                return 0
            if mem[i][t]!=-1:
                return mem[i][t]
            no = recur(i+1,t)
            yes = satisfaction[i]*t + recur(i+1,t+1)
            mem[i][t] = max(no, yes)
            return mem[i][t]
        satisfaction.sort()
        n= len(satisfaction)
        mem = [[-1]*(n+1) for i in range(n+1)]
        return recur(0,1)
