if __name__ == "__main__":
    pass



def mincoin(coins, targetSum):
   
    for coin in coins:
        mincoin(coins, targetSum - coin)
    