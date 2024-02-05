def square_footage():
    length = input("What is the length of your house? ")
    width = input("What is the width of your house? ")
    return int(length) * int(width)




from math import pi

def circumference_of_circle():
    radius = input("What is the radius of your circle? ")
    return (2 * int(radius) * pi)




from IPython.display import clear_output

def shopping_cart():

    my_shopping_cart = {}

    while True:
        item = input("Hello, would you like to ADD or REMOVE an item from your shopping cart today? ").lower()
        if item == "add":
            added_items = input("What would you like to add?").lower()
            quantity = input("How many? ").lower()
            my_shopping_cart[added_items] = quantity
        elif item == "remove":
            removed_item = input("What would you like to remove? ").lower()
            if removed_item in my_shopping_cart:
                quantity = input("How many? ").lower()
                my_shopping_cart[removed_item] -= quantity
            else:
                print("That item is not in your shopping cart")
        elif item == "show":
            print(f"You have {my_shopping_cart} in your shopping cart")
        elif item == "quit":
            print(f"Ok, you are quiting with {my_shopping_cart} in your shopping cart. Have a great day!")
            break
        else:
            print("I'm sorry that is an invalid command")


