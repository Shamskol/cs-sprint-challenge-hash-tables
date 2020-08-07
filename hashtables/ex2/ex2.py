#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    
    # Set up tickets hash table
    loc = {}
    route = [None] * length

    # Iterate through the tickets
    for ticket in tickets:
        loc[ticket.source] = ticket.destination
    #Set up route list
    # Initialize with the first location
    next = loc["NONE"]
    
    for i in range(0, length):
        route[i] = next
        next = loc[next]

    return route
