def discount_decider(price,quantity):
    if quantity>10:
        price = price*quantity
        discounted_price = price-(price*(10/100))
        return discounted_price
    else:
        return -1
 

price = float(input('enter price per item:'))
quantity = int(input('enter quantity:'))

bill = discount_decider(price,quantity)
if bill==-1:
    print('No discount applied :(. \nFinal Bill:',price*quantity)
else:
    print('10% discount applied :). \nFinal Bill:',bill)


'''
test case 1: 
enter price per item:15
enter quantity:5
No discount applied :(. 
Final Bill: 75.0
'''
'''
test case 2:
enter price per item:20
enter quantity:15
10% discount applied :). 
Final Bill: 270.0
'''
