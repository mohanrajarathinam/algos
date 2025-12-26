"""
Coding Problem: Container With Most Water

Problem Description:
You are given an integer array 'height' of length 'n'. There are 'n' vertical lines
drawn such that the two endpoints of the i-th line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the maximum amount of water a container can store.

Note: You may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The vertical lines are shown in the image. The maximum area of water
             (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4

Instructions/Tips for writing a solution:
1.  Understanding the Area: The area formed by two lines at indices `l` and `r`
    is `min(height[l], height[r]) * (r - l)`.

2.  Brute Force Approach (O(n^2)):
    You could iterate through all possible pairs of lines (i, j) where i < j,
    calculate the area for each pair, and keep track of the maximum.
    This approach will likely be too slow for the given constraints (n <= 10^5).

3.  Optimal Approach (Two-Pointer Technique - O(n)):
    *   Initialize two pointers, `left` at the beginning of the array and `right`
        at the end of the array.
    *   Initialize `max_area = 0`.
    *   While `left < right`:
        a. Calculate the current `height_ = min(height[left], height[right])`.
        b. Calculate the current `width_ = right - left`.
        c. Calculate the `current_area = height_ * width_`.
        d. Update `max_area = max(max_area, current_area)`.
        e. The key insight: To potentially find a larger area, you need to try to
           increase the `min(height[left], height[right])`.
           If `height[left] < height[right]`, moving `right` inwards will definitely
           decrease the `width` and won't necessarily increase the `height_` (it's still
           limited by `height[left]`, or a potentially shorter new `height[right-1]`).
           However, if you move `left` inwards, you *might* find a taller `height[left+1]`,
           which could increase the `height_` while `width` decreases.
           Therefore, move the pointer that points to the shorter line inward.
           If `height[left] < height[right]`, increment `left`.
           Else (if `height[right] <= height[left]`), decrement `right`.
    *   Return `max_area`.

Implement your solution in the `max_area` function below.
"""

def max_area(height: list[int]) -> int:
    """
    Calculates the maximum amount of water a container can store.
    """
    # Your code goes here
    left, right  = 0, len(height) - 1
    max_area_val = 0

    while left < right:
        container_height = min(height[left], height[right])
        container_width = right - left
        area = container_height*container_width
        max_area_val = max (area, max_area_val)

        if height[left] > height[right]:
            right = right -1
        else:
            left = left + 1
    return max_area_val


# --- Test Cases ---
if __name__ == "__main__":
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([2,3,4,5,18,17,6], 17),
        ([0, 0], 0), # Edge case with zeros
        ([0, 100], 0), # Edge case with one zero
        ([100, 0], 0), # Edge case with one zero
        ([0,1,0,2,0,1,0], 4) # Example to think about two-pointer with zeros
    ]

    for height_input, expected_output in test_cases:
        result = max_area(height_input)
        print(f"Input: {height_input}")
        print(f"Expected Output: {expected_output}")
        print(f"Actual Output: {result}")
        if result == expected_output:
            print("Test Passed!")
        else:
            print("Test Failed!")
        print("-" * 30)
