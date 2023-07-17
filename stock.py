# make a function with 2 parameters, first parameter is list of tuple, second is also list of tuple
# the function will add the new tuple to the list of tuple
# return the list of tuple sort ASC
# the data of list of tuple will be like this:
# [('25', 'HTC'), ('50', 'Nokia')]

# the data of new tuple will be like this:
# [('100', 'Samsung'), ['200','Xiaomi']]

def addStock(list_of_stock:list, list_of_new_stock:list):
    for new_stock in list_of_new_stock:
        already_in_stock = False
        for index,stock in enumerate(list_of_stock):
            if stock[1] == new_stock[1]:
                # convert list_of stock with that index into a list
                new_stock = list(list_of_stock[index])
                new_stock[0] += new_stock[0]
                # convert new_stock into tuple
                new_stock = tuple(new_stock)
                # replace list_of_stock with new_stock
                list_of_stock[index] = new_stock
                already_in_stock = True
        if not already_in_stock:
            list_of_stock.append(new_stock)
    # sort list_of_stock by second data of tuple
    list_of_stock.sort(key=lambda x:x[1])
    return list_of_stock

stocks = [(25, 'HTC'), (1000, 'Nokia'), (50, 'Samsung'), (33, 'Sony'), (10, 'Apple')]
new_stock = [(5, 'LG'), (10, 'Sony'), (4, 'Samsung'), (5, 'Apple')]

print(addStock(stocks,new_stock))