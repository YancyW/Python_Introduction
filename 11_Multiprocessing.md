# Multiprocessing
	= Parellization

# functions
They are almost the same with Threading:



# get return value
use queue (also same with threading)


```
import multiprocessing as mp
from queue import Queue


def user_function(l,q)
   for i in range(len(l)):
       do something for l
   q.put(l)     # put results into queue



if __name__=='__main__':
    q = Queue();
    arguments = [["xxx"].["yyy"]]
    for i in range (2):
		p=mp.Process(target="user_function()", name='xxx', args=(arguments,q))
        p.start()
		process.append(p)
    for j in process: # join every thread into main thread
		j.join()
    for i in range (2):
		results.append(q.get())  # get results from the queue

```


# processing pool
The following codes are same, so pool.map can store many things together and choose to parellelly compute automatically.
```
def multicore()
	pool = mp.Pool()
	result = pool.map(user_function,range(10))
	print(result)
```


```
def multicore()
	pool = mp.Pool()
	result = pool.apply_async(job,(2,2,3,4))
	multi_result = [pool.apply_async(job,(i,)) for i in range(10)]
	print(result.get() for result in range(multi_result))
```
	

# shared memory
In order to transfer data to different CPU cores, we need shared memory. Only the data in this shared memory can be used by other CPU.

```
value = mp.Value('d',1)   # this is a double type, the value is 1, and it already be defined in shared memory
array = mp.Array('i',[1,2,3]) # this is a 1-D list, and int type.
```


# process lock
When using shared memory to pass the value, all the processes will try to access the value. It is randomly that which process can really get this value, and this sometimes will cause problems.
The process lock is for only let one process using shared memory. Only after this process finished, other processes can access the shared memory again.

In order to add lock, at the beginning of the user_function, use multiprocessing.acquire()
At the end of user_function, user multiprocess.release()

For example:


```
def job(v,argument,l)
	l.acquire()
	v.value=v.value+argument
	l.release()
	

if __name__=='__main__':
	lock = mp.Lock()
    v= mp.Value('i',1)
	argument = 10
	p1=mp.Process(target="user_function()", name='xxx', args=(v,argument,l))
    p1.start()
	process.append(p1)

	argument = 20
	p2=mp.Process(target="user_function()", name='xxx', args=(v,argument,l))
    p1.start()
	process.append(p2)

    for j in process: # join every thread into main thread
		j.join()

    for i in range (2):
		results.append(q.get())  # get results from the queue
	

``` 



