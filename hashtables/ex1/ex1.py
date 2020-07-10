def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    ht = {}
    for i in range(length):
        weight = weights[i]
        complement = limit - weight
        if complement in ht:
            return [i, ht[complement]]
        else:
            ht[weight] = i    


    return None

weights_1 = [12, 6, 5, 7, 15, 20, 13, 21, 48, 24, 0]
print(get_indices_of_item_weights(weights_1,11, 25 ))
