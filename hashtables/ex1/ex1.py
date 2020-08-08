def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Set up a hashtable
    ht = {}
    # iterate through the weights
    for i in range(length):
        if weights[i] not in ht:
            # store the index
            ht[weights[i]] = i
        else:
            # check if weight plus itself equals the limit
            if limit - weights[i] == weights[i]:

                return (i, ht[weights[i]])

    # Calculate the complement    
        complement = limit - weights[i]
    # Check if the complement exists and is not equal to itself    
        if complement in ht and complement != weights[i]:
            # Return the indices of the weights, sorted in reverse order
            return sorted((ht[complement], ht[weights[i]]), reverse=True)
    # If otherwise there exists no pair that adds up to the limit, return None          
    return None
weights_1 = [12, 6, 5, 7, 15, 20, 13, 21, 48, 24, 0]
print(get_indices_of_item_weights(weights_1,11, 25 ))