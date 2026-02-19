from part1 import numbers

numbers.sort()
print(f"min: {min(numbers)}, max: {max(numbers)}, sorted list: {numbers}")

sum = 0
for number in numbers: sum += number
print("the sum is", sum)

print("\nfun things to do with lists\n")
numbers.reverse()
print(f"reversed list: {numbers}")
t = (1, 2, 3, 4)
numbers.extend(t)
print(f"there's this tuple: {t}. we can add it's elements to the list: {numbers}")
numbers.insert(4, 100)
print(f"we can also change the element at index 4 to 1000: {numbers}")