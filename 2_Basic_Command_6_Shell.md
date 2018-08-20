# Use Shell Command in Python
## os.system module
```
os.system("command with args")
```


## Subprocess module can realize this.
with subprocess, you can get stdout, stderr or other error message.
The official documentation recommends the subprocess over the alternative os.system(). 

```
from subprocess import call
from subprocess import run 
call(["ls","-l"]) 
run(["ls","-l"]) 
```

