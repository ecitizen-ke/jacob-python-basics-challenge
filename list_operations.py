'''
List Operations:
- Create a list called `numbers` containing five integer values.
- Print the list in its original order.
- Sort the list in ascending order and print it.
- Reverse the list and print it.
- Print the length of the list.
Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
Write a Python program to sum all the items in a list.
'''

numbers = [4, 5, 6, 7, 8]
print(numbers)

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

sum(numbers)
print(f"The sum of the numbers is {sum(numbers)}")

color_list = ["Red", "Green", "White", "Black"]
print(f"The first color is {color_list[0]} and the last color is {color_list[-1]}")
