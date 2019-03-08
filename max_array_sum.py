"""
Given an array of integers, find the subset of non-adjacent elements 
with the maximum sum. Calculate the sum of that subset.
Example:
>>> max_subset_sum([-2, 1, 3,-4,5])
8
>>> max_subset_sum([3, 7, 4, 6, 5]) 
13
>>> max_subset_sum([2,1,5,8,4])
11
>>> max_subset_sum([3, 5, -7, 8, 10])
15
"""


def max_subset_sum(arr):
    if arr:
        n = len(arr)
        results = [0] * n

        if n == 1:
            results[0] = arr[0]
        elif n == 2:
            results[1] = arr[1]
        else:
            results[0] = arr[0]
            results[1] = arr[1]
            max_result = 0
            for i in range(2, n):
                if max_result < results[i - 2]:
                    max_result = results[i - 2]
                # print(max_result)

                results[i] = max(results[i - 2], (max_result + arr[i]), arr[i])
        # print(results)
        return max(results)
    return


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("All tests have passed.")
