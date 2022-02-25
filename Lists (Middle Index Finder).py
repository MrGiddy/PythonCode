#Prompts input, calculates the middle element's index in a list (with even or odd #elements).
user_input = input("Enter elements separated by spaces: ")
user_list = user_input.split()
n = len(user_list)

if len(user_list) == 0:
    print("empty list!")
elif len(user_list) % 2 != 0:
    mid_index = (((n + 1) / 2) - 1)
    print(user_list)
    print("The middle index is: ", int(mid_index))
else:
    print(user_list)
    print("The middle indices are: ", int((n / 2) - 1), ",", int(n / 2))
