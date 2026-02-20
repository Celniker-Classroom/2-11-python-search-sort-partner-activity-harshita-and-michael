from random import randint #This line imports the randint function from the random module. The randint function generates a random integer between two specified values


numbers = [] #name your list and make sure it is empty!

# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
for number in range(10): #for loop appends 5 numbers to your list, but make sure you name your variable
    numbers.append(randint(1,50)) #this adds a random number between 1-50 to the list

print(f"Generated list: {numbers}")

random_number_to_search = randint(1, 20)
print(f"Searching for number: {random_number_to_search}")

if random_number_to_search in numbers:
    print("Number", random_number_to_search, "found in the list!")
else:
     print("Number", random_number_to_search, "not found in the list.")
