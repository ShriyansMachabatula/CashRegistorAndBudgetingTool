"""
The problem: 

The program below performs the same funciton as a digital cash register and a budgeting machine 
which helps people with controlling how much they spend along with not overspending while shopping. Sometimes people
go shopping and go over budget; with this program you will be asked your budget and how many items you would like to purchase and
the price of each item. Based on the total of your shopping cart and your budget the program will tell you if you can afford it or not.
There is also several coupons which provide the user with upto a 40% discount.  


"""


def cashRegister():  # define the function
    tax = 1.13  # define the tax
    coupon_list = ["CPS109", "Shriyans", "Machabatula",
                   "COMPSCI"]  # define the coupon list
    function = True  # define the function as true

    while function == True:  # while the function is true
        total = 0  # set the total to 0
        coupons = False  # set the coupons to false
        budgetCase = True  # set the budget case to true
        itemsInCartCase = True  # set the items in cart case to true
        pricesCase = True  # set the prices case to true
        couponsInputCase = True  # set the coupons input case to true
        reload = True  # set the reload to true
        restart = ""  # initialize the restart variable to an empty string
        lst = []  # initialize an empty list

        while budgetCase == True:  # while the budget case is true
            try:  # try the following code
                budget = float(
                    input("Please enter your budget for this shopping trip: $"))  # ask the user for their budget
            except ValueError:  # if the user enters a value error
                continue  # continue the loop
            else:  # if the user enters a value that is not a value error
                print(f'Your budget is: ${budget}')  # print the budget
            budgetCase = False  # set the budget case to false

        # The block of code above(lines 31-39) will avoid any invalid inputs that the user may enter and will ask the user to enter a valid input, This will continue to loop till the user enters a float value.

        while itemsInCartCase == True:
            try:
                itemsInCart = int(
                    input("Please enter how many item(s) you would like in your cart: "))
            except ValueError:
                continue
            else:
                print(f'The amount of item(s) in your cart is: {itemsInCart}')
            itemsInCartCase = False
            # The block of code above(lines 43-51) will avoid any invalid inputs that the user may enter and will ask the user to enter a valid input, This will continue to loop till the user enters a integer value.

        while pricesCase == True:
            try:
                for i in range(itemsInCart):
                    lst.append(
                        float(input("Please enter the prices of your item(s): $")))
                    total = sum(lst)
            except ValueError:
                continue
            else:
                pricesCase = False
            print("The total of your shopping cart is : $", round(total*tax, 2))
        # The block of code above(lines 54-64) will avoid any invalid inputs that the user may enter and will ask the user to enter a valid input, This will continue to loop till the user enters a float value.
        # This code also asks the user for the price of each item and adds it to the list and then sums the list to get the total of the shopping cart. The number of items on the list is dependent on the users previous input.

        while couponsInputCase == True:
            try:
                couponsInput = input(
                    "If you have a coupon code please enter it: ")
            except ValueError:
                continue
            couponsInputCase = False
        # The block of code above(lines 68-75) will avoid any invalid inputs that the user may enter and will ask the user to enter a valid input, This will continue to loop till the user enters a string value.
        # This string value will be used to check if the user has a coupon or not depending on the list called "coupon_list".
        # if the user enters the first coupon in the list
        if couponsInput == coupon_list[0]:
            coupons = True  # set the coupons to true
            if coupons == True:  # if the coupons are true
                # set the total to the total times 0.9 and then times the tax(this is a 10% discount)
                total = round(((total*0.9)*tax), 2)
                print("Fantastic! You have received 10% off of your entire shopping cart, Your total is now $", round(
                    total, 2))  # print the total
        # if the user enters the second coupon in the list
        if couponsInput == coupon_list[1]:
            coupons = True  # set the coupons to true
            if coupons == True:  # if the coupons are true
                # set the total to the total times 0.8 and then times the tax(this is a 20% discount)
                total = round(((total*0.8)*tax), 2)
                print("Fantastic! You have received 20% off of your entire shopping cart, Your total is now $", round(
                    total, 2))  # print the total
        # if the user enters the third coupon in the list
        if couponsInput == coupon_list[2]:
            coupons = True  # set the coupons to true
            if coupons == True:  # if the coupons are true
                # set the total to the total times 0.7 and then times the tax(this is a 30% discount)
                total = round(((total*0.7)*tax), 2)
                print("Fantastic! You have received 30% off of your entire shopping cart, Your total is now $", round(
                    total, 2))  # print the total
        # if the user enters the fourth coupon in the list
        if couponsInput == coupon_list[3]:
            coupons = True  # set the coupons to true
            if coupons == True:  # if the coupons are true
                # set the total to the total times 0.6 and then times the tax(this is a 40% discount)
                total = round(((total*0.6)*tax), 2)
                print("Fantastic! You have received 40% off of your entire shopping cart, Your total is now $", round(
                    total, 2))  # print the total
        elif coupons == False:  # if the coupons are false
            # Let the user know that the coupon is invalid
            print("Sorry, that is an invalid coupon!")

        # set the savings to the budget minus the total
        savings = round(budget-total, 2)

        # set the amount owed to the total minus the budget
        AmountOwed = round(total-budget, 2)

        if budget > total:
            # if the budget is greater than the total print that the user can afford all of their items and how much they have left over
            print("You can afford all of your items with $", savings, "to spare")
        elif total > budget:
            print('You are not able to afford all of these items. You would need another $',
                  AmountOwed, 'in order to complete your purchase')  # if the total is greater than the budget print that the user is not able to afford all of their items and how much they need to spend in order to complete their purchase

        while reload == True:  # while the reload is true
            restart = input(
                "Would you like to calculate your budget again? Answer 'yes' or 'no': ")  # ask the user if they would like to calculate their budget again
            # set the restart to lower case so that the user can enter yes or no in any case
            restart = restart.lower()
            if restart == "yes":  # if the restart is yes
                reload = False  # set the reload to false
            elif restart == 'no':  # if the restart is no
                function = False  # set the function to false, this will end the program
                reload = False  # set the reload to false


if __name__ == "__main__":
    cashRegister()  # call the function
