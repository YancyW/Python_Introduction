# tuple & list
a = tuple(1,2,5,4,3)
a1= 1,2,5,4,3  
b = list[-1,-5,-3,-6]

NOTE: the first element is 0,  a[0]==1, b[0]==-1

## function of tuple or list
len(a), len(b) --- length of tuple or list

e.g.
```
for i in range(len(a)):
	print(i," ","a[i]")
for i in range(len(b)):
	print(i," ","b[i]")
```

b.append --- add element in the end of a list
b.insert(1,value) --- add value in the second position 
b.remove(value) --- remove the first element when element==value in the list
b[0:3] (b[:3]) --- the first 0,1,2 element. the fourth element will not be included
b[-3:] --- the last three  element
b.index(value) --- the first position for element == value
b.count(value) --- how many times for element == value
b.sort(option) --- defautlt from small to large, or "reverse=True" sort from large to small

## multi list



