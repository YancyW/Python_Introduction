# zip/lambda/map

## zip 

```
a = [1,2,3]
b = [4,5,6]
list(zip (a,b))   --- [(1,4),(2,5),(3,6)]
for i,j in zip(a,b):
	print(i/2,j*2)   

---
0.5 8
1.0 10
1.5 12

```


## lambda
define a simple function
```
	func = lambda x,y:x+y

```
this is equal to 
```
def func(x,y):
	return x+y
```

## map
relate function to argument
```
list(map(func,[1,3],[2,5]))
--- [3,8]
```
