'''set is immutable data type'''
'''set is mutable is itself'''
'''set is unordered'''
'''set() is empty set'''
'''set{} is dictionary'''


a={1,34,4.5,'ravi',(3,45,'hi')}
# print(a)
# print(a,type(a))  #{(3, 45, 'hi'), 1, 34, 4.5, 'ravi'} <class 'set'>

# print(dir(set))['add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

# a={1,34,4.5,'ravi',(3,45,'hi')}
# b=1,3,4
# (a.add(b))
# print(a)  # {1, 'ravi', 34, 4.5, (3, 45, 'hi'), (1, 3, 4)}


# a={1,34,4.5,'ravi',(3,45,'hi')}
# a.clear()
# print(a) # set()

# a={1,34,45,56}; b={34,54}; c={54,34,56} ; d={1,34}
# print(a.intersection(b))   #34
# print(b.intersection(c))   #34,54

# a={1,2,3}
# b={2,3,4}
# c={1,3,6}
# a.update(b)
# a.update(c)
# print(a)  #{1,2,3,4,6}


# a={56,57,58}
# b={45,56,76}
# print(a.difference(b))  #  {57, 58}
# print(b.difference(a))   # {76, 45}
# print(a-b)
# print(b-a)


# a={1,23,45,56}
# a.discard(45)
# print(a)  #{56,1,23}

# a={1,23,34}
# b={34,45,67}
# a.union(b)
# print(a) # {1, 34, 23}
# b.union(a)
# print(b)  # {34,67,45}

# a={1,23,45,67}
# b={23,45,67}
# c={2,5,4}
# print(a.isdisjoint(b))   #false
# print(b.isdisjoint(c))   #true


# a={1,2,3,4,5}
# b={2,3,4}
# print(a.issubset(b))  #false
# # print(b.issubset(a))  #true


# a={1,21,4,45}
# b=(a.pop(2))
# print(b)

'''set methods in python'''
# a={1,2,3,4}
# b={2,3,4,5}
# # a.difference_update(b)
# print(a)  #{1}
# b.difference_update(a)
# print(b)  #{5}


# a={1,2,3}
# b={2,3,4}
# a.intersection_update(b)
# print(a) #  {2,3}



# a={1,2,3,4}
# b={2,3,4}
# # c=  a.issuperset(b)
# # print(c)  #false
# # c=b.issuperset(a)
# # print(c)  #false
# c=a.issuperset(b)
# print(c)   #true

# a={2,3,4,5}
# a.remove(3)
# print(a)   #{2, 4, 5}


# a={1,2.6,3.6,True,False}
# b={2,3.6,4.7,False}
# c=a.difference(b)
# print(c)


# a={1,2,3,4}
# b={2,3,4}
# c=a.symmetric_difference(b)
# print(c) # {1}

a={1,2,3,4}
b={2,3,4,5}
a.symmetric_difference_update(b)
print(a)
