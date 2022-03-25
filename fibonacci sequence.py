# Fibonacci sequence using while loop

# number of terms
no_of_terms = int(input("Enter no. of terms: "))

# defining starting variables
n1, n2 = 0, 1
# validating input
if no_of_terms <= 0:
    print("Enter a positive integer.")

# generating fibonacci sequence
else:
    k = 0
    while k < no_of_terms:
        print(n1)
        n = n1 + n2
        n1 = n2
        n2 = n
        k += 1


# Fibonacci sequence using recursion
num = int(input("No. of terms: "))


def fibonacci(n):
    if n == 0 or n == 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(num):
    print(fibonacci(i))
