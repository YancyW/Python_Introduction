# Number

python is not sensitive to variable type, it can identify the type automatically. 
For example, a=42 is int, a=42.0 is float, a="42" is string.
use keyword "type" can tell you the variable type
```
var_type = type(233)
print(var_type)    --- <class 'int'>
```

type can be forced to change to another one with the command 
str(), int(), float(), e.g.:
```
float(1)
```


 
## some operation function

- square
```
2**2
```

- get integer
```
9//2 = 4
```
- get reminder
```
9//2 = 1
```

- Boolean type --- True/False
	- <, >, <=, >=, ==, !=
    - other type can be change to Boolean automatically: 0 = False, 0.0 = False. empty set/list/dict/tuple = False
