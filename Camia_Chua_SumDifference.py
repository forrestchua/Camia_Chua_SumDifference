n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

def calculate_sum():
    global sum
    sum = n1 + n2

def calculate_difference():
    global difference
    difference = n1 - n2

calculate_sum()
calculate_difference()

print(f"Sum: {sum}")
print(f"Difference: {difference}")
