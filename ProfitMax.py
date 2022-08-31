def profitMax(a):
    all = []
    for x in range(len(a)):
        for y in range(x + 1, len(a)):
            profit_loss = a[y] - a[x]
            all.append(profit_loss)

    max_profit = max(all)
    return max_profit


print(profitMax([23171, 21011, 21123, 21366, 21013, 21367]))
