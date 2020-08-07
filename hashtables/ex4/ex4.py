def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Set up hash table
    data = {}
    # Set up result list
    result = []
    # Iterate through the nums
    for i in a:
        data[i] = i 
        if  i !=0 and -i in data:
            result.append(abs(i))

    return result

    

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
