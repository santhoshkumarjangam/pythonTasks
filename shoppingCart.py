Available_items = ['bread', 'cookies', 'butter', 'cheese', 'yoghurt']
Prices = [40,80,120,180,60]
Cart = []
while True:
    print('-----------------------------------------')
    print('What do you want to do ?')
    print('Enter 1 for viewing the items')
    print('Enter 2 for adding the items in cart')
    print('Enter 3 for updating the items in cart')
    print('Enter 4 for deleting the items in cart')
    print('Enter 5 for printing bill')
    print('Enter 6 for Exiting')
    print('-----------------------------------------')
    
    option = int(input('Enter Your Option: '))
    if option == 1:
        for item,price in zip(Available_items,Prices):
            print('name: ',item,'price: ',price)
            
    elif option == 2:
        item = input('Enter item: ')
        quantity = int(input('Enter Quantity: '))
        
        item_index = Available_items.index(item)
        Cart.append([item,quantity,Prices[item_index]*quantity])
        print("Your Cart :",Cart)
            
    elif option == 3:
        item = input('which item to be updated? :')
        quantity = int(input('Enter the quantity to be updated :'))
        item_index = Available_items.index(item)
        
        for l in Cart:
            if[l[0]==item]:
                l[1]=quantity
                price = Prices[item_index]
                l[2] = price*quantity
        else:
            print("Item not available in cart")
            
        print("Your Cart :",Cart)
        
    elif option == 4:
        item = input('which item to be deleted? :')
        for l in Cart:
            if[l[0]==item]:
                del_list = l 
                Cart.remove(del_list)
        else:
            print("Item not available in cart")
            
        print("Your Cart :",Cart)
        
    elif option == 5:
        bill = 0
        for l in Cart:
            bill+=l[2]
        print('Your Total Bill is :',bill)
        
    elif option == 6:
        print('Bye Bye')
        break
    
    else:
        print("Wrong Option")
