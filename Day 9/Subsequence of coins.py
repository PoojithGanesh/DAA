def min_coins_to_add(coins, target):
    coins.sort()
    current_sum = 0  
    coins_needed = 0  
    index = 0  
    for x in range(1, target + 1):
        if x > current_sum + 1:
            current_sum += (current_sum + 1)
            coins_needed += 1
        elif index < len(coins) and x == coins[index]:
            current_sum += coins[index]
            index += 1  
    return coins_needed
# Example usage
coins1 = [1, 4, 10]
target1 = 19
print(min_coins_to_add(coins1, target1))  # Output: 2
coins2 = [1, 4, 10, 5, 7, 19]
target2 = 19
print(min_coins_to_add(coins2, target2))  # Output: 1
