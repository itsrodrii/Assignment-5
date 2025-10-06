# 🧪 Performance Lab – Test, Analyze, Optimize
# Your name: _____________________
# Date: _____________________

# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    # 📝 Implementation
    freq = {}
    max_count = 0
    result = None

    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > max_count:
            max_count = freq[num]
            result = num
    return result


# 📝 Test cases
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))  # Expected 3
print(most_frequent([4, 4, 5, 5, 6]))        # Expected 4 or 5


"""
Time and Space Analysis for problem 1:
- Best-case: O(n) → must traverse all elements at least once
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) → dictionary stores counts for each unique element
- Why this approach? Simple hash map allows linear counting and easy max lookup
- Could it be optimized? Only if input size is very small; otherwise, this is efficient
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    # 📝 Implementation
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


# 📝 Test cases
print(remove_duplicates([4, 5, 4, 6, 5, 7]))  # Expected [4, 5, 6, 7]
print(remove_duplicates([1, 2, 2, 3]))        # Expected [1, 2, 3]


"""
Time and Space Analysis for problem 2:
- Best-case: O(n) → must check each element at least once
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) → set and result list
- Why this approach? Hash set allows O(1) membership check and preserves order
- Could it be optimized? Not significantly; this is already linear time
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    # 📝 Implementation
    seen = set()
    pairs = []
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs


# 📝 Test cases
print(find_pairs([1, 2, 3, 4], 5))  # Expected [(1, 4), (2, 3)]
print(find_pairs([0, 5, 3, 2], 5))  # Expected [(0, 5), (3, 2)]


"""
Time and Space Analysis for problem 3:
- Best-case: O(n) → traverse list once
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) → set stores seen elements
- Why this approach? Single pass, uses hash set to find complements
- Could it be optimized? Already linear; no nested loops needed
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    # 📝 Implementation
    capacity = 1
    lst = [None] * capacity
    size = 0

    for i in range(n):
        if size == capacity:
            print(f"Resizing from {capacity} to {capacity*2}")
            capacity *= 2
            new_lst = [None] * capacity
            for j in range(size):
                new_lst[j] = lst[j]
            lst = new_lst
        lst[size] = i
        size += 1


# 📝 Test case
add_n_items(6)
# Expected output:
# Resizing from 1 to 2
# Resizing from 2 to 4
# Resizing from 4 to 8


"""
Time and Space Analysis for problem 4:
- When do resizes happen? When size reaches capacity
- Worst-case for a single append: O(n) → copying all elements
- Amortized time per append: O(1) → doubling reduces frequent resizing
- Space complexity: O(n) → list stores all elements
- Why doubling reduces cost overall? Fewer resizes overall; average cost per append is constant
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    # 📝 Implementation
    total = 0
    result = []
    for num in nums:
        total += num
        result.append(total)
    return result


# 📝 Test cases
print(running_total([1, 2, 3, 4]))  # Expected [1, 3, 6, 10]
print(running_total([5, 5, 5]))     # Expected [5, 10, 15]


"""
Time and Space Analysis for problem 5:
- Best-case: O(n) → must iterate all elements
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) → new result list
- Why this approach? Simple single pass, accumulates running sum
- Could it be optimized? Already linear, no better asymptotic improvement
"""
