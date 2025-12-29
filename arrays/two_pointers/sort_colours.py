"""
Sort Colors (Dutch National Flag Problem)

Problem:
Given an array nums with n objects colored red, white, or blue, sort them in-place
so that objects of the same color are adjacent, in the order red (0), white (1), and blue (2).

Constraints:
- Must sort in-place (modify the input array)
- Cannot use built-in sort functions
- Array contains only integers 0, 1, and 2

Example:
Input: nums = [2,1,2,0,1,0,1,0,1]

Output: [0,0,0,1,1,1,1,2,2]

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Input: nums = [2,0,1]
Output: [0,1,2]
"""


def sort_colors(nums):
    """
    Sort an array containing only 0s, 1s, and 2s in-place.

    Args:
        nums: List[int] - Array of integers (0, 1, or 2) representing colors

    Returns:
        None - Modifies nums in-place
    """
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            mid += 1
            low += 1
        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
        else:
            mid += 1
    return nums

def test_sort_colors():
    """Test cases for sort_colors function"""

    # Test case 1: Example from problem
    test1 = [2, 1, 2, 0, 1, 0, 1, 0, 1]
    sort_colors(test1)
    assert test1 == [0, 0, 0, 1, 1, 1, 1, 2, 2], f"Test 1 failed: {test1}"
    print("Test 1 passed: [2,1,2,0,1,0,1,0,1] -> [0,0,0,1,1,1,1,2,2]")

    # Test case 2: Mixed colors
    test2 = [2, 0, 2, 1, 1, 0]
    sort_colors(test2)
    assert test2 == [0, 0, 1, 1, 2, 2], f"Test 2 failed: {test2}"
    print("Test 2 passed: [2,0,2,1,1,0] -> [0,0,1,1,2,2]")

    # Test case 3: One of each
    test3 = [2, 0, 1]
    sort_colors(test3)
    assert test3 == [0, 1, 2], f"Test 3 failed: {test3}"
    print("Test 3 passed: [2,0,1] -> [0,1,2]")

    # Test case 4: Already sorted
    test4 = [0, 0, 1, 1, 2, 2]
    sort_colors(test4)
    assert test4 == [0, 0, 1, 1, 2, 2], f"Test 4 failed: {test4}"
    print("Test 4 passed: Already sorted array")

    # Test case 5: Reverse sorted
    test5 = [2, 2, 1, 1, 0, 0]
    sort_colors(test5)
    assert test5 == [0, 0, 1, 1, 2, 2], f"Test 5 failed: {test5}"
    print("Test 5 passed: Reverse sorted array")

    # Test case 6: All same color
    test6 = [1, 1, 1, 1]
    sort_colors(test6)
    assert test6 == [1, 1, 1, 1], f"Test 6 failed: {test6}"
    print("Test 6 passed: All same color")

    # Test case 7: Only two colors
    test7 = [2, 0, 2, 0, 2]
    sort_colors(test7)
    assert test7 == [0, 0, 2, 2, 2], f"Test 7 failed: {test7}"
    print("Test 7 passed: Only two colors")

    # Test case 8: Single element
    test8 = [0]
    sort_colors(test8)
    assert test8 == [0], f"Test 8 failed: {test8}"
    print("Test 8 passed: Single element")

    print("\nAll tests passed!")


if __name__ == "__main__":
    test_sort_colors()