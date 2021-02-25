list1 = [1, 2, 3, 4, 5]

#for elem in list1:
#    print(elem)

print()

# # does the same thing as the code above it
[print(elem) for elem in list1]            #list comphresion

print()

# for elem in list1:
#     for elem >= 5:
#         print(elem)

#same as the code above
[print(elem) for elem in list1 if elem >= 5]  #list comphrension

print()

(print(elem) for elem in list1 if elem <= 5) # generator

print()

def square(x):
    return x**2

print()

print(list(map(lambda x: x**2, list1))) 

new_list = []
for elem in list1:
    elem = elem**2
    new_list.append(elem)