# 🧪 Performance Lab – Test, Analyze, Optimize
# Name: ___Kossi Koutoglo__________________
# Date: ___10/04/2025__________________

# 🔍 Problem 1: Find Most Frequent Element
# We need to find the number that shows up the most in a list.
# If there's a tie, just return any of the most frequent numbers.

def most_frequent(numbers):
    # I used a dictionary to count how many times each number appears
    freq = {}
    max_count = 0
    result = None

    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > max_count:
            max_count = freq[num]
            result = num
    return result


# Testing the function
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))  # Should print 3
print(most_frequent([4, 4, 5, 5, 6]))        # Could be 4 or 5


"""
Performance notes:
- Best-case: O(n) because we have to look at every number
- Worst-case: O(n)
- Average-case: O(n)
- Space: O(n) for storing counts of each number
- Why this works: The dictionary makes counting fast and simple
- Could it be faster? Not really for big lists, this is already efficient
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# I want to make a new list with no duplicates, but keep the original order

def remove_duplicates(nums):
    # Use a set to remember what we've seen and a new list to store results
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


# Testing
print(remove_duplicates([4, 5, 4, 6, 5, 7]))  # Should print [4, 5, 6, 7]
print(remove_duplicates([1, 2, 2, 3]))        # Should print [1, 2, 3]


"""
Performance notes:
- Best-case: O(n) because we check each number once
- Worst-case: O(n)
- Average-case: O(n)
- Space: O(n) for the set and the output list
- Why this works: Checking set membership is fast (O(1))
- Could it be faster? This is already linear, so it's fine
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Find all pairs of numbers that add up to a target
# Assume no duplicates in input

def find_pairs(nums, target):
    # Use a set to track numbers we've seen
    seen = set()
    pairs = []
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs


# Testing
print(find_pairs([1, 2, 3, 4], 5))  # Should print [(1, 4), (2, 3)]
print(find_pairs([0, 5, 3, 2], 5))  # Should print [(0, 5), (3, 2)]


"""
Performance notes:
- Best-case: O(n), we just loop once
- Worst-case: O(n)
- Average-case: O(n)
- Space: O(n) for the set
- Why this works: Using a set avoids nested loops
- Could it be faster? Linear is already the best for this problem
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Add n items to a list and "double" the list size when needed
# Print a message every time resizing happens

def add_n_items(n):
    # Start with capacity 1
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


# Testing
add_n_items(6)
# Expected output:
# Resizing from 1 to 2
# Resizing from 2 to 4
# Resizing from 4 to 8


"""
Performance notes:
- Resizes happen when list is full
- Worst-case for one append: O(n) when we have to copy everything
- Amortized time per append: O(1), because doubling reduces frequency of resizing
- Space: O(n) for the list
- Why doubling helps: fewer resizes overall, so average append is fast
"""


# 🔍 Problem 5: Compute Running Totals
# Return a list where each number is the sum of all numbers up to that index

def running_total(nums):
    total = 0
    result = []
    for num in nums:
        total += num
        result.append(total)
    return result


# Testing
print(running_total([1, 2, 3, 4]))  # Should print [1, 3, 6, 10]
print(running_total([5, 5, 5]))     # Should print [5, 10, 15]


"""
Performance notes:
- Best-case: O(n), we need to go through each element
- Worst-case: O(n)
- Average-case: O(n)
- Space: O(n) for the new list
- Why this works: Single loop keeps track of running sum
- Could it be faster? Already linear, so no
"""
