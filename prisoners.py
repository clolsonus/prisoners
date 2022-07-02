#!/usr/bin/env python3 

# From Veritasium
# The Riddle That Seems Impossible Even If You Know The Answer
# https://www.youtube.com/watch?v=iSNsgj1OCLA

# Please watch the video for the rules of the game so I don't have to retype
# them here. :-)

# Simulate riddle and validate results!

import random

# total number of prisoners
num = 100

# total number of simulation runs
runs = 1000

# count number of successes
wins_predicted = 0
wins_actual = 0

for run in range(runs):
    print("Run:", run)

    # create the boxes and shuffle them
    boxes = list(range(num))
    random.shuffle(boxes)
    #print(boxes)

    # find loops (not required to simulate the strategy, but interesting to see
    # the loops exist as explained in the video)
    loops = []
    box_used = [False] * num
    while True:
        loop = []

        # find first unallocated box
        i = 0
        while i < num and box_used[i] == True:
            i += 1
        #print("First box:", i)

        # test if no starting box found (finished)
        if i >= num:
            #print("Finished allocating loops")
            break

        # start traversing loop
        while not box_used[i]:
            # test if loop is completed
            if i in loop:
                #print("loop completed")
                break
            #print("Box:", i, "=", boxes[i])
            loop.append(i)
            box_used[i] = True  # mark as allocated to a loop
            i = boxes[i]  # advance to next box in the loop
        
        # add this completed loop to the list of loops
        loops.append(loop)
    #print(loops)

    # assertion that if all loops are length num/2 or less, all prisoners will
    # succeed in finding their numbers
    success = True
    for loop in loops:
        if len(loop) > num/2:
            success = False
        #print("loop len:", len(loop))
    print("predicted success:", success)
    if success:
        wins_predicted += 1

    # Run the simulation and check the theory
    success = True
    for prisoner in range(num):
        i = prisoner
        checks = 0
        while checks < num/2:
            if boxes[i] == prisoner:
                # woohoo, we found our number
                break
            i = boxes[i]  # advance to next box
            checks += 1
        if checks >= num/2:
            # oops, ran out of allowed boxes before finding our number!
            success = False
            # any failure means no need to continue
            break
    if success:
        wins_actual += 1
    print("Actual success:", success)

print("runs:", runs, "predicted wins:", wins_predicted, "actual wins:", wins_actual, "(%.2f)" % (100.0*wins_predicted/runs))