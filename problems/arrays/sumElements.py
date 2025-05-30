def sumElements(arr):
    """
    arg: 
        arr: list of elements

    return: 
        result: sum of all elements
    -------------
    """

    if not arr:
        return None
    sum = 0
    for element in arr:
        sum += element
    return sum



def run():
    arr = [1,2,3,4,5]
    result = sumElements(arr)
    print(f"Sum : {result}")


if __name__ == "__main__":
    run()