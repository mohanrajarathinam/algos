"""
This file provides a comprehensive playground for understanding lists in Python.
In Python, arrays are most commonly represented as lists. Lists are ordered,
mutable (changeable), and can contain items of different data types.
"""

# --- 1. Creating Lists ---
print("--- 1. Creating Lists ---")

# An empty list
empty_list = []
print(f"An empty list: {empty_list}")

# A list of integers
numbers = [1, 2, 3, 4, 5]
print(f"A list of numbers: {numbers}")

# A list with mixed data types
mixed_list = [1, "hello", 3.14, True]
print(f"A list with mixed data types: {mixed_list}")

# Using the list() constructor
from_string = list("world")
print(f"A list created from a string 'world': {from_string}")
print("-" * 20 + "\n")


# --- 2. Accessing Elements (Indexing) ---
print("--- 2. Accessing Elements (Indexing) ---")
# Lists are zero-indexed, meaning the first element is at index 0.
print(f"Original list: {numbers}")
print(f"Element at index 0: {numbers[0]}")  # First element
print(f"Element at index 2: {numbers[2]}")  # Third element

# Negative indexing allows you to access elements from the end.
print(f"Last element (using -1): {numbers[-1]}")
print(f"Second to last element (using -2): {numbers[-2]}")

# Accessing an index that doesn't exist will raise an IndexError.
# For example, numbers[5] would cause an error.
print("-" * 20 + "\n")


# --- 3. Slicing Lists ---
# Slicing extracts a portion of the list. It creates a new list.
# Syntax: list[start:stop:step]
# start: The index to start from (inclusive).
# stop: The index to end at (exclusive).
# step: The interval between elements.
print("--- 3. Slicing Lists ---")
print(f"Original list: {numbers}")

# Get elements from index 1 up to (but not including) index 4
sub_list = numbers[1:4]
print(f"Slice from index 1 to 4: {sub_list}")

# Slice from the beginning to index 3 (exclusive)
from_beginning = numbers[:3]
print(f"Slice from beginning to index 3: {from_beginning}")

# Slice from index 2 to the end
to_the_end = numbers[2:]
print(f"Slice from index 2 to the end: {to_the_end}")

# Slicing with a step
every_other = numbers[0:5:2]
print(f"Every other element: {every_other}")

# Reverse a list with slicing
reversed_list = numbers[::-1]
print(f"Reversed list using slicing: {reversed_list}")
print("-" * 20 + "\n")


# --- 4. Modifying Lists ---
print("--- 4. Modifying Lists ---")
print(f"Original list: {numbers}")

# Change an element at a specific index
numbers[0] = 100
print(f"After changing element at index 0: {numbers}")

# Change a range of elements
numbers[1:3] = [200, 300]
print(f"After changing elements from index 1 to 3: {numbers}")
print("-" * 20 + "\n")


# --- 5. List Methods ---
print("--- 5. List Methods ---")
fruits = ["apple", "banana", "cherry"]
print(f"Initial fruits list: {fruits}")

# append(): Adds an item to the end of the list.
fruits.append("orange")
print(f"After appending 'orange': {fruits}")

# extend(): Adds all items from an iterable (like another list) to the end.
fruits.extend(["grape", "mango"])
print(f"After extending with ['grape', 'mango']: {fruits}")

# insert(): Inserts an item at a given position.
fruits.insert(1, "blueberry")
print(f"After inserting 'blueberry' at index 1: {fruits}")

# remove(): Removes the first occurrence of a value.
fruits.remove("cherry")
print(f"After removing 'cherry': {fruits}")

# pop(): Removes and returns the item at a given index. If no index is specified, it removes and returns the last item.
popped_item = fruits.pop(2)
print(f"Popped item at index 2: {popped_item}")
print(f"List after pop: {fruits}")
last_item = fruits.pop()
print(f"Popped last item: {last_item}")
print(f"List after popping last item: {fruits}")

# index(): Returns the index of the first occurrence of a value.
# It raises a ValueError if the value is not found.
try:
    apple_index = fruits.index("apple")
    print(f"Index of 'apple': {apple_index}")
except ValueError:
    print("'apple' not found in the list.")


# count(): Returns the number of times a value appears in the list.
fruits.append("apple")
print(f"New fruits list: {fruits}")
print(f"Count of 'apple': {fruits.count('apple')}")

# sort(): Sorts the list in place (modifies the original list).
fruits.sort()
print(f"Sorted list (in-place): {fruits}")

# reverse(): Reverses the order of the list in place.
fruits.reverse()
print(f"Reversed list (in-place): {fruits}")

# copy(): Returns a shallow copy of the list.
fruits_copy = fruits.copy()
fruits_copy.append("I am a copy")
print(f"Original fruits list: {fruits}")
print(f"Copied and modified list: {fruits_copy}")


# clear(): Removes all items from the list.
fruits_copy.clear()
print(f"Cleared copy of the list: {fruits_copy}")
print("-" * 20 + "\n")


# --- 6. List Operations ---
print("--- 6. List Operations ---")
list_a = [1, 2, 3]
list_b = [4, 5, 6]

# Concatenation (+)
concatenated_list = list_a + list_b
print(f"{list_a} + {list_b} = {concatenated_list}")

# Repetition (*)
repeated_list = list_a * 3
print(f"{list_a} * 3 = {repeated_list}")
print("-" * 20 + "\n")

# --- 7. List Comprehensions ---
# A concise and readable way to create lists.
print("--- 7. List Comprehensions ---")

# Create a list of squares from 0 to 9
squares = [x**2 for x in range(10)]
print(f"List of squares from 0 to 9: {squares}")

# Create a list of even numbers from 0 to 19
evens = [x for x in range(20) if x % 2 == 0]
print(f"Even numbers from 0 to 19: {evens}")
print("-" * 20 + "\n")


# --- 8. Nested Lists ---
# Lists can contain other lists. This is useful for creating matrices or grids.
print("--- 8. Nested Lists ---")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"A 3x3 matrix:\n{matrix[0]}\n{matrix[1]}\n{matrix[2]}")

# Accessing elements in a nested list
# To get the element '5', we access the list at index 1, and then the element at index 1 within that list.
element_5 = matrix[1][1]
print(f"Element at matrix[1][1]: {element_5}")
print("-" * 20 + "\n")


# --- 9. Useful Built-in Functions with Lists ---
print("--- 9. Useful Built-in Functions with Lists ---")
data = [9, 1, 8, 2, 7, 3, 6, 4, 5]
print(f"Data list: {data}")

# len(): Get the number of items in a list.
print(f"Length of the list: {len(data)}")

# min(), max(), sum(): Get the minimum, maximum, and sum of a list of numbers.
print(f"Minimum value: {min(data)}")
print(f"Maximum value: {max(data)}")
print(f"Sum of values: {sum(data)}")

# sorted(): Returns a new sorted list, without modifying the original.
sorted_data = sorted(data)
print(f"Original data: {data}")
print(f"New sorted list: {sorted_data}")

# enumerate(): Iterate over a list and get both the index and the value.
print("Enumerating the fruits list:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
print("-" * 20 + "\n")
