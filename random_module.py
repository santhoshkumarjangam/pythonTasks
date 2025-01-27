import random 

lucky = int(input('enter lucky number (1-10):'))
i = 1
while True:
    random_number = random.randint(1,10)
    print('iteration:',i)
    if lucky == random_number:
        print('random number matched lucky number')
        print()
        break
    else:
        print('random number did not matched lucky number')
      
    print('random number:',random_number)
    print('lucky number:',lucky)
    print()
    i+=1
