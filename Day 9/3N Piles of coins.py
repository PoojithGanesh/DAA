def maxCoins(piles):
    piles.sort(reverse=True)
    max_coins = 0
    for i in range(1, len(piles), 2):
        max_coins += piles[i]
    return max_coins
