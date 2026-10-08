cart = ["apple", "milk", "bread", "apple", "eggs", "milk"]

cart = list(set(cart))

cart.append("cheese")

if "bread" in cart:
    cart.remove("bread")

    cart.sort()

    print("Final Cart:", cart)
    print("Number of Different Items:", len(cart))

