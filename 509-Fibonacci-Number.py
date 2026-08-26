class Solution:
    def fib(self, n: int) -> int:
        memo = [-1] * (n + 1)  # Initialize cache
        
        def helper(i):
            if i <= 1:
                return i
            
            # 1. Check if subproblem was ALREADY solved
            if memo[i] != -1:
                return memo[i]
            
            # 2. Recurse, store result in memo, and RETURN
            memo[i] = helper(i - 1) + helper(i - 2)
            return memo[i]
            
        return helper(n)