def stock_availability(products, action, *args):
    if action == "delivery":
        products.extend(args)
    elif action == "sell":
        if not args:
            products.pop(0)
        elif isinstance(args[0], int):
            for _ in range(args[0]):
                if products:
                    products.pop(0)
        else:
            products = [item for item in products if item not in args]
    return products


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
