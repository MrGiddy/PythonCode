# Inventory Management Program
# Uses a dictionary to track all of the store's inventory
# along with how many of each item the store has.

# Takes fruit as input and returns how many there are in the store.

store = {"Orange": 2, "Watermelon": 0, "Apple": 8, "Banana": 42}

user_input = input("Enter type of fruit: ").capitalize()
if user_input in store:
    print("There are", store[user_input], "of them.")
else:
    print("This fruit has not been catalogued.")
