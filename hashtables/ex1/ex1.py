def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Set up a hashtable
    ht = {}
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
        if complement in ht and complement != weights[i]:
            return sorted((ht[complement], ht[weights[i]]), reverse=True)
              
    return None
weights_1 = [12, 6, 5, 7, 15, 20, 13, 21, 48, 24, 0]
print(get_indices_of_item_weights(weights_1,11, 25 ))