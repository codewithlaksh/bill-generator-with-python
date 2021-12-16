from datetime import datetime
import random
import os

sum = 0
currency = input("Enter the currency of your country in short form (like INR for Indian Rupees, USD for US Dollar): \n")
while(True):
    userInput = input(f"Enter the price ({currency}) or press q to quit: \n")
    if (userInput!='q'):
        sum = sum + int(userInput)
        print(f"Order total so far: {sum} {currency}")
    else:
        billNo = random.randint(1000, 9999)
        print(f"Your bill total is {sum} {currency}. Thanks for shopping!")
        name = input("Enter the name of your customer you want to save: \n")
        shop_name = input("Enter the name of your shop: \n")
        if not os.path.exists(f'{os.getcwd()}\\mybills'):
            os.mkdir(f'{os.getcwd()}\\mybills') # Generates a folder mybills in the current working directory
            save_path = f'{os.getcwd()}\\mybills'
            filename = f'{name}-bill-{str(datetime.now().date())}-{str(billNo)}.txt'
            complete_path = os.path.join(save_path, filename)
            f = open(complete_path, "x")
        else:
            save_path = f'{os.getcwd()}\\mybills'
            filename = f'{name}-bill-{str(datetime.now().date())}-{str(billNo)}.txt'
            complete_path = os.path.join(save_path, filename)
            f = open(complete_path, "x")

        f.write(f'''{shop_name}
----------
Bill Details :
Customer Id: {str(random.randint(8888, 15000))}
Bill No : {str(billNo)}
Customer Name: {name}
Total bill: {sum} {currency}.
Bill Created on: {str(datetime.now().date())}
Visted on: {str(datetime.now())}
----------
Thank you for visiting our store
----------
Copyright © Lakshyaraj Dash {int(datetime.today().year)} - {int(datetime.today().year) + 1}''')
        break