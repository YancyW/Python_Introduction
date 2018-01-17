# Function

## define a function
def func1(a,b):
	c = a + b
	print("c = ".c)

## invoke a function
x=1
y=2
fun1(x,y)

Or you can emphase which variable get which value
fun1(a=x,b=y)

## default arguments
def func1(a,b=1):
	c = a + b
	print("c = ".c)


## [List](./5_Function_1_List_Tuple.md)

## [Map](./5_Function_2_Map.md)

## [Dictionary](./5_Function_3_Dictionary.md)

## in
keyword "in" can be used not only in for/while loop, but also in list/map/dictionary to select a special element
```
list_a = [1,2,3,5,6,7]
exist_4 = 4 in list_a   #--- False
```
 
```
dic_a = {"a":1, "b:2", "c":3}
exist_b = "b" in dic_a  #--- True 
```
 
