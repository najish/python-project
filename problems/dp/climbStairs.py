def climbStairs(n):
    if n <= 2:
        return n
    return climbStairs(n - 1) + climbStairs(n - 2)


def fun(n, memo = {}):

    if n in memo:
        return memo[n]
    
    if n <= 2:
        memo[n] = n
        return memo[n]
    
    memo[n] = fun(n - 1, memo) + fun(n - 2, memo)
    return memo[n]
    

if __name__ == "__main__":
    input = [5, 10, 15, 20, 40, 50, 100]

    for item in input:
        print(fun(item))
    
    