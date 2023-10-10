def moveDisks4(n,start_1=1, start_2=2, destination=4, intermediate=3):
    if n>=2:  # first recursive call
        moveDisks4(n-1, start_1, start_2, intermediate, destination) 
    print("Move disk ", n, " from ", start_2, " to ", destination)
    print("Move disk ", n, " from ", start_1, " to ", destination)
    if n>=2:  # second recursive call
        moveDisks4(n-1, intermediate, intermediate, destination, start_1)

print("moveDisks(4):")
moveDisks4(1)