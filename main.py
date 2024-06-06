import time

print("Welcome to deliver-roar")
time.sleep(0.5)
print("Where would you like to order from?")

restaurants = ["Burger King", "McDonalds", "KFC"]

# list all restaurant options
rIndex = 1
for r in restaurants: 
  time.sleep(0.25)
  print(f'[{rIndex}] {r}')
  rIndex = rIndex + 1

restaurantOption = int(input("Where would you like to order from: "))

# function to list all menu items and allow user to input their choice
# This loops untill they exit (by entering the number of menu items + 1)
def menuOptions(name, menu, prices):
  loop = 'Y'
  secondaryOrder = False
  incorrectOrder = False
  userOrder = []
  userCosts = []

  while loop == 'Y':
    if secondaryOrder and incorrectOrder == False:
        print(f'Alright, what else would you like from {name}? Heres our menu: ')
    elif secondaryOrder == False and incorrectOrder == False:
        print(f'Welcome to {name}! Heres our menu: ')
    elif incorrectOrder == True: 
        print("Please enter a correct option! Heres our menu: ")
        
    secondaryOrder = True
    menuIndex = 0
    for item in menu:
      time.sleep(0.15)
      menuIndex = menuIndex + 1
      print(f'[{menuIndex}] {item}')
    print(f'[{menuIndex + 1}] Exit')
    
    # Set the exitNumber as the index + 1
    exitNumber = menuIndex + 1

    # Ensure the number isnt greater than the number of items
    option = int(input("What would you like to order: "))
    if option > exitNumber:
        incorrectOrder = True
        print("Incorrect menu option")
        loop = 'Y'

    else:
        if option == exitNumber:
            print('Alright! Thanks for shopping!')
            print('Heres your shopping cart: ')
            previewOrderIndex = 0
            for order in userOrder:
                time.sleep(0.15)
                print(f'1x {order} - ${userCosts[previewOrderIndex]}')
                previewOrderIndex = previewOrderIndex + 1
            print("Heres your total cost: ")  
            totalCosts = 0
            for orderCost in userCosts:
                totalCosts = totalCosts + orderCost
            print(f'${totalCosts}')
            loop = 'N'
        else:
            userOrder.append(menu[option - 1])
            userCosts.append(prices[option - 1])
            # Subtracting 1 cus the array starts at 0. But the user inputs start at 0
      

if restaurantOption == 1:
  menuOptions(restaurants[0], ["Whopper","Burger", "Fries", "Nuggets"], [5, 6, 1, 3])

elif restaurantOption == 2:
    menuOptions(restaurants[1], ["Big Mac", "McChicken", "McFlurry", "Mc Nuggets", "Ice Cream"], [7, 5, 2, 4, 3])

elif restaurantOption == 3:
    menuOptions(restaurants[2], ["Tenders", "Zinger Chicken", "Fries"], [4, 10, 5])
    
else:
    print("Not a valid option! Please try again.")