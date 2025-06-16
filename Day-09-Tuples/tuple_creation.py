t1 = (1, 2, 3)
t2 = tuple([4, 5, 6])
t3 = 7, 8, 9  # Implicit tuple
print(t1, t2, t3)

#indexing
t = ('a', 'b', 'c', 'd', 'e')
print(t[0])     
print(t[-1])     
print(t[1:4])    

#singleton_tuple
t1 = (42,)
t2 = (42)
print(type(t1))     
print(type(t2)) 