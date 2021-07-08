#1
# def countdown(num):
#     lst = []
#     for i in range(num, 0, -1):
#         lst.append(i)
#     return lst
# print(countdown(5))

#2
# def print_and_return(a,b):
#     print(a)
#     return b
# print(print_and_return(1,2))

# 3 
# def first_plus_length(lst):
#     return lst[0] + len(lst)
# print(first_plus_length([5, 4, 3, 2, 1]))
# print(first_plus_length([1, 2, 3, 4, 5]))

#4
# def values_greater_than_second(lst):
#     newLst = []
#     if len(lst) < 2:
#         return False
#     else:
#         for i in range(0, len(lst), 1):
#             if lst[i] > lst[1]:
#                 newLst.append(lst[i])
#     return newLst
# print(values_greater_than_second([11, 10, 4, 7, 19, 32, 21, 1]))

#5
# def length_and_value(a,b):
#     lst = []
#     for x in range(0, a, 1):
#         lst.append(b)
#     return lst
# print(length_and_value(5,7))
# print(length_and_value(3,1534))