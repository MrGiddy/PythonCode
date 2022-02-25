#Print integers 1 to N,
#but print “Fizz” if an integer is divisible by 3,
#“Buzz” if an integer is divisible by 5,
#and “FizzBuzz” if an integer is divisible by both 3 and 5.
#Make the program skip even integers
N = int(input(":"))
count = 1

for i in range(count, N):
    if i % 2 == 0:
        count += 1
        continue
    elif i % 3 == 0 and i % 5 == 0:
        print("Fizz" + "Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
