#Hashtag Generator for social media application

#Sample Input: code sleep eat repeat
#Sample Output: #codesleepeatrepeat

user_string = input(": ")


def hashtag_generator(x):
    x = x.replace(" ", "")
    return "#" + x


print(hashtag_generator(user_string))
