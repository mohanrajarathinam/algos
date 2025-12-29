"""
Maximum Fruits Problem (Longest Subarray with At Most Two Distinct Elements)

Problem:
Write a function to calculate the maximum number of fruits you can collect from an
integer array 'fruits', where each element represents a type of fruit. You can start
collecting fruits from any position in the array, but you must stop once you encounter
a third distinct type of fruit. The goal is to find the longest subarray where at most
two different types of fruits are collected.

Example:
Input: fruits = [3, 3, 2, 1, 2, 1, 0]
Output: 4
Explanation: We can pick up 4 fruits from the subarray [2, 1, 2, 1]

Approach:
This is a sliding window problem where we need to maintain a window with at most
2 distinct fruit types.
- Use two pointers (left and right) to define the window
- Use a hash map to track the count of each fruit type in the current window
- Expand the window by moving right pointer
- When we have more than 2 distinct types, shrink from left until we have 2 types
- Track the maximum window size seen
"""


def max_fruits(fruits):
    """
    Find the maximum number of fruits that can be collected with at most 2 distinct types.

    Args:
        fruits: List[int] - Array where each element represents a fruit type

    Returns:
        int - Maximum number of fruits that can be collected
    """
    maximum_fruits, start, end = 0, 0, 0
    state = {}

    while end < len(fruits):
        # Add current fruit to the window
        if fruits[end] in state:
            state[fruits[end]] += 1
        else:
            state[fruits[end]] = 1

        # Shrink window from left if we have more than 2 fruit types
        while len(state) > 2:
            state[fruits[start]] -= 1
            if state[fruits[start]] == 0:
                state.pop(fruits[start])
            start += 1

        # Update maximum only after ensuring window is valid (at most 2 types)
        maximum_fruits = max(maximum_fruits, end - start + 1)
        end += 1

    return maximum_fruits

def run_tests():
    """Test cases for the max_fruits function"""

    test_cases = [
        {
            'input': [3, 3, 2, 1, 2, 1, 0],
            'expected': 4,
            'description': 'Example case: subarray [2, 1, 2, 1]'
        },
        {
            'input': [1, 2, 1],
            'expected': 3,
            'description': 'All fruits can be collected (only 2 types)'
        },
        {
            'input': [0, 1, 2, 2],
            'expected': 3,
            'description': 'Subarray [1, 2, 2] or [2, 2] (length 3)'
        },
        {
            'input': [1, 2, 3, 2, 2],
            'expected': 4,
            'description': 'Subarray [2, 3, 2, 2]'
        },
        {
            'input': [3],
            'expected': 1,
            'description': 'Single fruit'
        },
        {
            'input': [1, 1, 1, 1],
            'expected': 4,
            'description': 'All same fruit type'
        },
        {
            'input': [1, 2, 1, 2, 1, 2],
            'expected': 6,
            'description': 'Two alternating types - all can be collected'
        },
        {
            'input': [],
            'expected': 0,
            'description': 'Empty array'
        }
    ]

    print("Running test cases...\n")
    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        result = max_fruits(test['input'])
        status = "PASS" if result == test['expected'] else "FAIL"

        if status == "PASS":
            passed += 1
        else:
            failed += 1

        print(f"Test {i}: {status}")
        print(f"  Description: {test['description']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")
        print(f"  Got: {result}")
        print()

    print(f"Results: {passed} passed, {failed} failed out of {len(test_cases)} tests")


if __name__ == "__main__":
    run_tests()