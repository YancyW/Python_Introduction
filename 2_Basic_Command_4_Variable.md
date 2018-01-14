# Variable

- python is case sensitive
	- a != A
- a,b,c = 1,2,3


## global variable
- define a variable outside any function, conventionally we use CAPITAL name for a global variable
- use key word "global" in a function to change the global variable
```
a = None
def fun():
	global a
	a = 2
	return a+1

print("a is :", a)
print("fun(a) is :", fun(a))

a is : 2
fun(a) is : 3
```
