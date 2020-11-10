divider = "*" * 38
count = 0
underline = "------"
welcome = '**   Welcome to the Snakes Cafe!    **\n**    Please see our menu below.    **\n**                                  **\n** To quit at any time, type "quit" **'
menuItems = "Wings", "Cookies", "Spring Rolls", "Salmon", "Steak", "Meat Tornado", "A Literal Garden", "Ice Cream", "Coke", "Pie", "Coffee", "Tea", "Unicorn Tears"

def welcomeMsg():
    print(divider)
    print(welcome)
    print(divider)

def theMenu():
    menu= """
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears
    """
    print(menu)

def askOrder():
    print(divider)
    print("**  What would you like to order?   **")
    print(divider)

def takeOrder():
    # Create a dictionary with the items in the list and have the starting values be at 0
    count = 0
    item = dict.fromkeys(menuItems, count)
    # Ask for the item to be ordered
    askOrder()
    # While 
    while True:
        # Assign user input to variable
        customerOrder = input()
        # Check if user types "quit"
        if customerOrder == "quit":
            break
        # if customerOrder == "done":
        #     print(item.values)
        #     break
        if customerOrder in item:
            item[customerOrder] += 1
            print()
            print(f"** {item[customerOrder]} order of {customerOrder} have been added to your meal")
        
        else:
            print("Sorry, we dont have that... Try again")    


welcomeMsg()
theMenu()
takeOrder()