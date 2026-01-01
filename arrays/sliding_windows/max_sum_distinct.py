"""
Maximum Sum of Distinct Subarray With Length K

Problem:
Given an integer array nums and an integer k, find the highest possible sum of a subarray
where:
- The subarray has length k
- All elements in the subarray are unique (distinct)

If no such subarray exists, return 0.

Example 1:
Input: nums = [3, 2, 2, 3, 4, 6, 7, 7, -1], k = 4
Output: 20
Explanation: The subarray [3, 4, 6, 7] has all distinct elements and sum = 20

Example 2:
Input: nums = [1, 1, 1, 1], k = 2
Output: 0
Explanation: No subarray of length 2 has all distinct elements

Approach:
- Use sliding window technique with a hash set/dict to track unique elements
- Maintain a window of size k
- Check if all elements in the window are distinct
- Track the maximum sum among valid windows
"""

from typing import List


def max_sum_distinct_subarray(nums: List[int], k: int) -> int:
    """
    Find the maximum sum of a subarray of length k with all distinct elements.

    Args:
        nums: List of integers
        k: Length of the subarray

    Returns:
        Maximum sum of valid subarray, or 0 if no valid subarray exists
    """
    start, curr_sum, max_sum = 0, 0, 0
    subset = set()
    for end in range(len(nums)):
        while nums[end] in subset:
            subset.remove(nums[start])
            curr_sum -= nums[start]
            start += 1

        subset.add(nums[end])
        curr_sum += nums[end]
        if end - start + 1 == k:
            max_sum = max(curr_sum, max_sum)
            subset.remove(nums[start])
            curr_sum -= nums[start]
            start += 1
    return max_sum


def run_tests():
    """Run test cases for the solution."""
    test_cases = [
        {
            "nums": [3, 2, 2, 3, 4, 6, 7, 7, -1],
            "k": 4,
            "expected": 20,
            "description": "Example 1 - subarray [3, 4, 6, 7]"
        },
        {
            "nums": [1, 1, 1, 1],
            "k": 2,
            "expected": 0,
            "description": "All elements are duplicates"
        },
        {
            "nums": [1, 2, 3, 4, 5],
            "k": 3,
            "expected": 12,
            "description": "All distinct - subarray [3, 4, 5]"
        },
        {
            "nums": [1, 5, 4, 2, 9, 9, 9],
            "k": 3,
            "expected": 15,
            "description": "Multiple valid windows - [5, 4, 2] and [4, 2, 9]"
        },
        {
            "nums": [4, 4, 4],
            "k": 3,
            "expected": 0,
            "description": "No valid window exists"
        },
        {
            "nums": [1],
            "k": 1,
            "expected": 1,
            "description": "Single element"
        },
        {
            "nums": [9, 9, 9, 1, 2, 3],
            "k": 3,
            "expected": 6,
            "description": "Valid window at the end [1, 2, 3]"
        },
        {
            "nums": [1, 2, 2],
            "k": 2,
            "expected": 3,
            "description": "Valid window [1, 2]"
        },
    ]

    passed = 0
    total = len(test_cases)

    print("Running tests...\n")

    for i, test in enumerate(test_cases, 1):
        nums = test["nums"]
        k = test["k"]
        expected = test["expected"]
        description = test["description"]

        try:
            result = max_sum_distinct_subarray(nums, k)
            status = "PASS" if result == expected else "FAIL"

            if result == expected:
                passed += 1
                print(f"Test {i}: {status}")
                print(f"  Description: {description}")
                print(f"  Input: nums={nums}, k={k}")
                print(f"  Expected: {expected}, Got: {result}\n")
            else:
                print(f"Test {i}: {status}")
                print(f"  Description: {description}")
                print(f"  Input: nums={nums}, k={k}")
                print(f"  Expected: {expected}, Got: {result}")
                print(f"  ERROR: Result mismatch!\n")

        except Exception as e:
            print(f"Test {i}: ERROR")
            print(f"  Description: {description}")
            print(f"  Input: nums={nums}, k={k}")
            print(f"  Expected: {expected}")
            print(f"  Exception: {str(e)}\n")

    print("=" * 50)
    print(f"Tests passed: {passed}/{total}")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()