import random

def three_random_num_divby_5():
    numbers = []
    for i in range(3):
        numbers.append(random.choice(range(100,1000,5)))
    
    return numbers
    
    
def lottery_pick():
    tickets = random.sample(range(1000,5000),100)
    winners = random.sample(tickets, 2)
    
    return winners
    
    
def generate_otp():
    return random.randint(100000,999999)
    
    
def random_character(string):
    return random.choice(string)
    
def random_string_len5():
    alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    return "".join(random.sample(alphabets,5))
    
def generate_password():
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    specials = '!@#$%&*()_-'
    
    password = ''
    
    
    password += "".join(random.sample(uppercase,2))
    password += "".join(random.sample(numbers,1))
    password += "".join(random.sample(specials,1))
    password += "".join(random.sample(lowercase,6))
    
    return password
    
    
def mul_random_floats():
    f1 = round(random.uniform(1,100),2)
    f2 = round(random.uniform(1,100),2)
    
    return f'multiplication of {f1} and {f2} is {round(f1*f2,2)}'
    
def roll_dice():
    return 6
    
def random_date(start,end):
    
    start_date = int(start.split('/')[0])
    end_date = int(end.split('/')[0])
    
    start_month = int(start.split('/')[1])
    end_month = int(end.split('/')[1])
    
    start_year = int(start.split('/')[2])
    end_year = int(end.split('/')[2])
    
    date = random.randint(min(start_date,end_date),max(start_date,end_date))
    month = random.randint(min(start_month,end_month),max(start_month,end_month))
    year = random.randint(min(start_year,end_year),max(start_year,end_year))
    
    return str(date)+'/'+str(month)+'/'+str(year)
