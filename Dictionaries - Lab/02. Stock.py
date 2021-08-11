stock = input().split()
search = input().split()
stock_dict = {}

for el in range(0, len(stock), 2):
    item = stock[el]
    quantity = stock[int(el) + 1]
    stock_dict[item] = int(quantity)

for element in range(len(search)):
    needed_item = search[element]
    if needed_item in stock_dict:
        print(f"We have {stock_dict[needed_item]} of {needed_item} left")
    else:
        print(f"Sorry, we don't have {needed_item}")
