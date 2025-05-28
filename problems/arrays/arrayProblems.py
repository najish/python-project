def minElement(arr):
    """
    Function to find the minimum element in an array.
    :param arr: List of integers
        :return: Minimum element in the array
    """
    if not arr:
        return None
    min_value = arr[0]
    for num in arr:
        if num < min_value:
            min_value = num
    return min_value

