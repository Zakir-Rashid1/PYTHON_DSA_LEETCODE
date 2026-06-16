

'''
Problem Statement: Maximum Product Subarray in an Array

Given an integer array nums. Find the subarray with the largest product,
and return the product of the elements present in that subarray.
A subarray is a contiguous non-empty sequence of elements within an array.


Example 1
Input: nums = [4, 5, 3, 7, 1, 2]
Output: 840

Explanation:
The largest product is given by the whole array itself



Example 2
Input: nums = [-5, 0, -2]
Output: 0

Explanation:
The largest product is achieved with the following subarrays [0], [-5, 0], [0, -2], [-5, 0, -2].

'''

#Approach 01: Using Bruteforce
#Time Complexity: O(n^2)
#Space Complexity: O(1)


def maximum_product_subarray_1(nums):
    max_product = float('-inf') #Global maximum product
    product = 1
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            product *= nums[j]

            #Find maximum among product and global maximum product
            max_product = max(max_product, product)

        #Rest product
        product = 1

    return max_product

nums = [-5, 0, -2]
print(f"Maximum product of max subarray is: {maximum_product_subarray_1(nums)}")



#Approach 02: Using Observation
#Time Complexity: O(n)
#Space Complexity: O(1)

# Approach 02: Using Prefix & Suffix Observation
# Time Complexity: O(n)
# Space Complexity: O(1)

def maximum_product_subarray_2(nums):

    # Stores the maximum product seen so far
    maximum_product = float('-inf')

    # Product while traversing from left to right
    prefix_product = 1

    # Product while traversing from right to left
    suffix_product = 1

    for i in range(len(nums)):

        # If a zero was encountered previously,
        # start a new subarray from the next element.
        if prefix_product == 0:
            prefix_product = 1

        if suffix_product == 0:
            suffix_product = 1

        # Compute product from left to right
        prefix_product *= nums[i]

        # Compute product from right to left
        suffix_product *= nums[len(nums) - 1 - i]

        # The answer could come from either direction
        maximum_product = max(
            maximum_product,
            prefix_product,
            suffix_product
        )

    return maximum_product


nums = [2,3,-2,4]
print(f"Maximum product of max subarray is: {maximum_product_subarray_2(nums)}")




'''
NOTE: Why does the Prefix-Suffix Product approach work?

The sign of a product depends on the number of negative elements:

1. Even number of negative numbers
   -> Product of the entire subarray is positive.
   -> Keeping all elements gives the maximum product.

2. Odd number of negative numbers
   -> Product of the entire subarray is negative.
   -> To make it positive, we must remove either:
      - the prefix up to the first negative number, or
      - the suffix starting from the last negative number.

Therefore, the maximum product subarray must be obtainable by:
   - taking a prefix product (left-to-right traversal), or
   - taking a suffix product (right-to-left traversal).

---------------------------------------------------------

Why do we reset the product when it becomes 0?

A zero splits the array into independent segments.

Example:

    [2, 3, 0, -2, 4]

Any subarray crossing the zero will have product 0.

So after encountering a zero, we restart the product calculation
from the next element by resetting the running product to 1.

---------------------------------------------------------

Why are two traversals needed?

Consider:

    [-1, -2, -3]

Prefix products:

    -1
     2
    -6

Maximum = 2

But the correct answer is:

    (-2) * (-3) = 6

Now compute suffix products:

    -3
     6
    -6

Maximum = 6

Similarly, there are cases where only the prefix traversal finds
the optimal answer.

Therefore, we compute both:

    Prefix Products  -> Left to Right
    Suffix Products  -> Right to Left

and take the maximum among them.

---------------------------------------------------------

Key Observation:

For an odd number of negative elements, the optimal subarray is
obtained by excluding either:

    - everything before the first negative, OR
    - everything after the last negative.

A prefix scan captures one possibility.
A suffix scan captures the other.

Hence, checking both prefix and suffix products guarantees that
the maximum product subarray is found in O(n) time and O(1) space.

'''