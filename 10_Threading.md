# What is Multi Threading
	= Parellization

# threading function
	```
    import threading
    threading.active_count() #get actived thread,  output is an int
    threading.enumerate() # check thread information, output is a string (_MainThread + other Thread )
    threading.current_thread() # check current thread (_MainThread ..)
    threading.Thread(target=user_function, name='xxx', args=(arguments)) # add thread
    threading.start()  #let thread begin to work
    threading.join()  #all command after joinm this thread will be add into main thread, and run main thread after finish this thread,
	```

# get return value
   The results in the different thread should be input into the queue, then we can get them in the main thread.

```
import threading
from queue import Queue

def user_function(l,q)
   for i in range(len(l)):
       do something for l
   q.put(l)     # put results into queue

if __name__=='__main__':
    q = Queue();
    arguments = [["xxx"].["yyy"]]
    for i in range (2):
      t= Threading.Thread(target="user_function()", name='xxx', args=(arguments,q))
      t.start()
      threads.append(t)
    for j in threads: # join every thread into main thread
      j.join()
    for i in range (2):
      results.append(q.get())  # get results from the queue

```		

# GIL (Global Interpreter Lock) 
   Multi threading only has effects when dealing with different tasks for different threads.
   Because these threadings run one by one. 


