# GLOBAL VARIABLES

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

def calculate_sum():
    global sum
    # LOCAL VARIABLES
    sum = n1 + n2
    print(f"Sum: {sum}")
    
def calculate_difference():
    global difference
    # LOCAL VARIABLES
    difference = n1 - n2
    print(f"Difference: {difference}")
    
calculate_sum()
calculate_difference()
