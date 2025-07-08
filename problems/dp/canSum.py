def canSum(nums, target, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]

    if target < 0:
        return False
    if target == 0:
        return True

    for num in nums:
        result = canSum(nums, target - num, memo)
        memo[target] = result
        if result:
            return True
    memo[target] = False
    return False



def howSum(nums, target, memo = {})
    if target in memo:
        return [memo[target]]
    
    if target < 0:
        return None

    if target == 0: 
        return []
    
    for num in nums: 
        return [] + howSum(nums, target - num)
    

def bestSum(nums, target):
    pass 


if __name__ == "__main__":
    print(canSum([7,14], 300))

    