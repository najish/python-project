def maxElement(arr):
    if not arr:
        return None
    max_value = arr[0]
    for value in arr:
        if max_value < value:
            max_value = value
    return max_value



def run():
    arr = [1,2,3,5,66,7]
    result = maxElement(arr)
    print(f"maximum element in the array : {result}")


if __name__ == "__main__":
    run()