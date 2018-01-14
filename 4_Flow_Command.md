# Flow_Command

## while
while a < 10:
	print(a)
    a = a +1

## for
for a in list/range

e.g.
```
list = [1,3,5,2,4]
for i in list:
	print("in the for loop ", i)
print("out of the for loop")
```

```
for i in range(1,5,2):
	print(i)

output: 1,3
```
Note: this range will let i from 1  to all integer <5, and step 2


## if
```
if a<b:
	print("a<b",a)
elif a>b:
	print("a>b,b")
else:
	print("a=b,a,b")
```


python can recognize complicated condition command:
```
if a<b<c:
	print("a<b<c",a)
```
