# Use a for loop to print out the numbers 1 to 7

#for i in range(1, 8): 
#    print(i)

#****************************************************************

# Use a while to print out the numbers 1 to 7
#easy way to use while loop
#j = 1
#while j <= 7:
#    print(i)
#    j = j + 1

#******************************************************************
#Another way to use while loop

#i = 0
#while True:
#    print(i)
#    i = i + 1
#    if i == 8:
#        break

# Given the participants' score sheet for your University Sport day,
# you are required to find the runner-up score. You are given n scores.
# Store them them in a list and find the score of the runner up
#runner_up_score = [2, 3, 6, 6, 5]

def second_place(runner_up_score):
    # sort the list
    runner_up_score.sort(reverse=True)

    first_place_score = runner_up_score[0]

    for elem in runner_up_score:
        if elem < first_place_score:
            return_string = "Here is second place with a score of {}!".format(elem)
            return return_string


print(second_place(runner_up_score))