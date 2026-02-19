from random import randint #This line imports the randint function from the random module. The randint function generates a random integer between two specified values

comparisons = 0  # Initialize the counter for comparisons
found = False  # Variable to track if the number was found
numbers = [] #name your list and make sure it is empty!

# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
for number in range(10): #for loop appends 5 numbers to your list, but make sure you name your variable
    numbers.append(randint(1,50)) #this adds a random number between 1-50 to the list
print(f"Generated list: {numbers}")

random_number_to_search = int(input("Search for a number: "))

for number in numbers:  # Name your variable in the for loop
    comparisons += 1  # Increment the counter for each comparison
    if number == random_number_to_search:
        found = True  # Set found to True if the number is in the list
        print(f"Number {random_number_to_search} found in the list after {comparisons} comparisons!")
        break  # Exit the loop early if the number is found

if found == False: print(f"Number {random_number_to_search} not found in the list after {comparisons} comparisons!")