# Question1: Cubed numbers to 1000

my_list = []

# defining variables
num = 0
cubed = 0

while cubed < 1000:           # If cubed number is over 1000, break the loop
    num += 1                  # number to be cubed

    cubed = num**3            # cubed number
    my_list.append(cubed)     # Adding cubed value to my_list

print(my_list)


# Could also be done using range but doesn't technically "break"
# cubed_list = []
# for number in range(1,11):
#     cube = number**3
#     cubed_list.append(cube)

# print(cubed_list)


#Question2: Prime numbers to 100

prime_list = []

# Creating range 1-100 and grabbing looping through values within the range
for Number in range (1, 101):

    # Count to keep track - resets each loop
    count = 0

    # checking divisibility from 2 to number value (ie. checking to see if 5 is divisible by any number between 2 and 4)
    for i in range(2, Number):

        # Iterates through each value in range
        if(Number % i == 0):         # If there are no remainders, the value is not prime. Adds to count and ends loop.
            count = count + 1        # If there are remainders, loops through count until reaching Number.
            break

            #Does not append to list in next loop since count !=0

    # Is a prime number
    if (count == 0 and Number != 1):
        prime_list.append(Number)

print(prime_list)

#Question3: User age
def age(user_age):
    if user_age < 18:          # Kid
        print("Kid")
    elif user_age >= 65:       # Senior
        print("Senior")
    else:                      # Adult
        print("Adult")

age(17)
age(18)
age(65)
