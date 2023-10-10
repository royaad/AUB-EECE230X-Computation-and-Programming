def moveDisks(n,start=1,destination=3,intermediate=2):
    """ Assumes n is an integer >=1 """
    if n>=2:  # first recursive call
        moveDisks(n-1, start,intermediate,destination) 
    print("Move disk from ", start, " to ", destination)
    # Base case: if n ==1, only this print  will be executed
    if n>=2:  # second recursive call
        moveDisks(n-1, intermediate,destination,start)

def moveDisks4(n,start_1=1, start_2=2, destination=4, intermediate_1=2, intermediate_2=3):
    if n >= 2:
        moveDisks(n-1, start_2, intermediate_2, destination)
    print("Move disk from ", start_2, " to ", destination)
    if n >= 2:
        moveDisks(n-1, start_1, intermediate_1, destination)
    print("Move disk from ", start_1, " to ", destination)
    if n>=2:
        # moveDisks4(n-1, intermediate_1, intermediate_2, destination, start_1, start_2)
        # and many other combinations of start and intermediate are valid
        moveDisks4(n-1, intermediate_1, intermediate_2, destination, intermediate_2, start_1)
print("moveDisks(4):")
moveDisks4(3)