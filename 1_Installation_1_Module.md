# Module
- install pip, which is a tool for installing python modules
```
sudo apt install python3-pip   
```
- install module
```
pip3 install [module_name]
```
- update module
```
pip3 install -U [module_name]
```

## numpy
for math 

## tensorflow

	- tensorflow, for cpu
	- tensorflow-gpu, for gpu

## re
regular expression
	- sub(), need three arguments: rule,replace and target.
         - rule    ---  something need to be changed
         - replace ---  change "rule" to something 
         - target  ---  find the rule in this target
		 ```
			import re
			rule = "cat"
			replace = "dog"
			target = "I like a cat"
			print(re.sub(rule,replace,target))
		 ```
        


## codecs
encode/decode nature language, 
```
bfile = codecs.open("xxx.dat","r","big5")
```
if use default open, it will have wrong input.

## sqlite3
deal with SQLite library

## requests

## pycuda
package for cuda, which define some function for gpu cores.
```
import pycuda.autoinit
import pycuda.gpuarray as gpuarray
import pycuda.driver as cuda
```
Note: with nvidia bumblebee drive, one needs to use optirun command to compile python
```
optirun puthon python ***.py
```
