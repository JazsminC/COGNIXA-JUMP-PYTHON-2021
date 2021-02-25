# Given an integer, n, perform the following condition actions
# if n is odd, print weird
# if n is even:
#           * and in the inclusive range of 2 to 5
#           * and in the inclusive range of 6 to 20
#           * and greater than 20
# Then print Not Werid


# def weird_or_Not(numbers):
#     for num in numbers:
#         if (num % 2) != 0: # if number is even
#             print("Weird")
#         else:
#             if num >= 2 and num <= 5:
#                 print("Not weird")
#             elif num >= 6 and num <=20:
#                 print("Weird")
#             elif num > 20:
#                 print("Not weird")

# list_of_num = [1, 2, 3, 4, 8, 11, 18, 20]

# weird_or_Not(list_of_num)

# 1.
# Write a function that takes an array of integers and places the zeroes in the
# center of the array. All non-zero integers should keep their relative position. 
# For the purpose of this question, center is defined as floor(length of array / 2).

#def array_of_int():

# print all fibonnaci numbers less than 1000
# Hint: when you don't know many times you do something, use a while loop
# Hint: use a temp variable

def fib_less_than_1000():
    first_fib_num = 0
    sec_fib_num = 1
    previous_fib = sec_fib_num
    current_fib = first_fib_num

    while current_fib < 1000:
        print(current_fib)
        temp = current_fib
        current_fib = current_fib + previous_fib
        previous_fib = temp

fib_less_than_1000()
    
    



# 3.(This is super hard)
# center_zeros([1, 1, 3, 0, 6, 0]) -> [1, 1, 0, 0, 3, 6]
# center_zeros([0, 3, 1]) == [3, 0, 1]
# center_zeros([1, 1, 3, 0]) == [1, 1, 0, 3]
# center_zeros([1, 1, 3, 0, 6, 0]) == [1, 1, 0, 0, 3, 6]
