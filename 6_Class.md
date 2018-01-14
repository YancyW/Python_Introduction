# Class
## define

```
class person:
	_birth_d = 0
	_birth_m = 0

	def set_birthday(self,x,y):
		_birth_d = x
		_birth_m = m
	def print_birthday(self):
		print("the birthday is ", self._birth_d, "-", self._birth_m)
```


## declare

## use
use a class
```
Me = person()
Me.set_birthday(7,11)
Me.print_birthday()
Me._birth_d
```

## init a class
	For a class, don't need to define the member at the beginning, you can use the member in the init function

	```
class person:
	def __init__(self,day,month, year=1999):
		self._birth_d = day
		self._birth_m = month 
		self._birth_y = year 
	def set_birthday(self,x,y,z):
		_birth_d = x
		_birth_m = m
		_birth_y = m
	def print_birthday(self):
		print("the birthday is ", self._birth_d, "-", self._birth_m,"-",self._birth_y)
	```

    Then in declaration, you have to input the arguments for a new class
	```
	Me = person(7,11)
	Me.print_birthday()
	```

    
		
