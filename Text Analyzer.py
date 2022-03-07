# This program analyzes a sample file to find what percentage of the text each character occupies.
# It also returns the number of words in the file.

def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count


filename = input("Enter file name: ")  # i.e text_file.txt
with open(filename) as f:
    text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = (count_char(text, char) / len(text)) * 100
    print("{0} - {1}%".format(char, round(perc, 2)))

# prints number of words in the file
x = text.split()
print()
print("The file has {} words.".format(len(x)))
