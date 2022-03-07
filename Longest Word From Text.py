# This program finds the longest word form an input text

txt_list = input("Type some text: ").split()    # stores each word from input as list elements

# stores each word from txt_list and their length as key: value pair in txt_dict
txt_dict = {}
for i in txt_list:
    txt_dict[i] = len(i)

# prints word (key) with maximum length (value) from txt_dict
print("{} is the longest word you typed :)".format(max(txt_dict, key=txt_dict.get)))
