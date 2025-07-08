def howSum(nums, target):
    if target < 0:
        return None
    
    if target == 0:
        return []
    
    for item in nums:
        return [] + howSum(nums, target - item)
    return []


howSum([10,5,20],3)