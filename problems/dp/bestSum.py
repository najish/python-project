def bestSum(nums, target):
    if target < 0:
        return False
    if target == 0:
        return True

    for item in nums:
        bestSum(nums, target - item)
    
    return False




if __name__ == "__main__":
    pass 