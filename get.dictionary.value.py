what = input("enter the product name: ")

product = {"dildo": 3.00, "underwear": 4.00, "gag-ball": 10.00, "cigar": 2.00, "gold chain": 1000}

# print(product)

if what in product: 
    # print(product[what])
    print(product.get(what))
else: 
    print(f'{what} not found')