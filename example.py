def find_fixed_point(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    result = -1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == mid:
            result = mid
            high = mid - 1  # Continue searching left for a smaller index
        elif arr[mid] > mid:
            high = mid - 1
        else:
            low = mid + 1

    return result

# Test the function
def main():
    # Test case from the example
    A = [-10, -5, 0, 3, 7]
    result = find_fixed_point(A)
    print(result)  # Should print 3

if __name__ == "__main__":
    main()
