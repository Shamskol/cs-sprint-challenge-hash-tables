def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    #Set up the hash table for tracking counts
      # whereby key: number, value: count
    ht = {} 

    # Set up intersections list
    result = [] 

    # Iterate through the arrays of arrays
    for arr in arrays:
        for num in arr:
            if num not in ht:
                ht[num] = 1
            else:
                ht[num] += 1 
                if ht[num] == len(arrays):
                    result.append(num)    

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
