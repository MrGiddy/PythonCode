#Four Digit Bank card PIN System
#Compares inputs from user, checks if they are four digits long to create PIN
try:
    user_pin = int(input("Create PIN: "))
    repeat_pin = int(input("Confirm PIN: "))
    if user_pin == repeat_pin:
        list_user_pin = [int(a) for a in str(user_pin)]  #Creates a list separating digits of the PIN
        if len(list_user_pin) != 4:
            print("PIN code should be four digits long.")
        else:
            print("PIN code successfully created.")
    else:
        print("PIN codes don't match.")

except ValueError:                            #catches if input has non-digit characters
    print("PIN code should be four digits long.")

finally:
    print("We value your commitment :)")
