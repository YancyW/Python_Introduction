# tuple & list & dictionary
a = tuple(1,2,5,4,3)
a1= 1,2,5,4,3  
b = list[-1,-5,-3,-6]
b1 = [-1,-5,-3,-6]
d = {1:'a','c':'b'}

- tuple only can get value when definition.
- tuple can not be changed
- tuple must have a comma, even only have one element, e.g.: (item1,)



# get element
a[0],b[1], d[1], d['c']
NOTE: 
- the first element for tuple and list  is 0,  a[0]==1, b[0]==-1
     

## function of tuple or list
len(a), len(b)    --- length of tuple or list
b[0:3] (b[:3])    --- the first 0,1,2 element. the fourth element will not be included
b[-3:]            --- the last three  element
b.index(value)    --- the first position for element == value
b.count(value)    --- how many times for element == value

e.g.
```
for i in range(len(a)):
	print(i," ","a[i]")
for i in range(len(b)):
	print(i," ","b[i]")


def sum_times(x,y):
	return (x+y),(x*y) 
sum_times(1,2)   #--- (3,2)
```

## function of list only

len(a), len(b) --- length of tuple or list
b.append()        --- add element in the end of a list
b.insert(1,value) --- add value in the second position 
b.remove(value)   --- remove the first element when element==value in the list
b.sort(option)    --- defautlt from small to large, or "reverse=True" sort from large to small

del d['c'] 
d['b']='x'

## multi list
a = [[1,2,3],
	 [4,5,6],
	 [7,8,9]]



