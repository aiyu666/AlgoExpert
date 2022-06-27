def nonConstructibleChange(coins):
    coins.sort()
    min_change = 0 
    for coin in coins:
        if coin > min_change + 1:
            break
        min_change += coin
    return min_change + 1