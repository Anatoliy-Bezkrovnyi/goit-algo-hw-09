coins = [50, 25, 10, 5, 2, 1]


def greedy_change(amount): 
    change = {}
    for coin in coins:
        count = amount // coin
        if count > 0: 
            change[coin] = count
        amount = amount - coin * count
    return change
 

def dynamic_change(amount): 
    min_coins_required = [0] + [float("inf")] * amount # Мінімальна кількість монет
    last_coin_used = [0] * (amount + 1) # Остання використана монета

    for s in range(1, amount + 1):
        for coin in coins: 
            if s >= coin and min_coins_required[s - coin] + 1 < min_coins_required[s]:
                min_coins_required[s] = min_coins_required[s - coin] + 1
                last_coin_used[s] = coin

    change = {}
    current_sum = amount
    while current_sum > 0: 
        coin = last_coin_used[current_sum]
        change[coin] = change.get(coin, 0) + 1
        current_sum = current_sum - coin

    return change


if __name__ == "__main__":
    result_greedy = greedy_change(113)
    print(result_greedy)
    result_dynamic = dynamic_change(113)
    print(result_dynamic)