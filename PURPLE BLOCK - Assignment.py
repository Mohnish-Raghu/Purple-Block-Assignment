def maxProfit(l):
    buy_price = l[0]
    sell_price = l[0]
    for i in l:
        if buy_price > i:
            buy_price = i
        elif sell_price < i:
            sell_price = i
    return buy_price, sell_price

l = list(map(int,input("Enter a list of prices: ").split()))
buy_price, sell_price = maxProfit(l)
print(f"To get the maximum profit, below is the best buy price and sell price.\nBuy Price = {buy_price}\nSell Price = {sell_price}")