#Visualization
TKinter moduler for generating window by python.
This is similar as other visualization tools --- add a toolbox and give the trigger.

load tkinter and initialize a default window and active the window
```
import tkinter as tk
window=tk.TK()
window.title('Hello World!')
window.geometry('500x500')

some operation to the window

window.mainloop() # this will refresh the window after doing any operation
```

## add text
```
text=tk.Label(window,
     text='test text is printed here!',
     bg  ='red',
     font=('Arial',12)
	 width=10,height=3
	)
test.pack()
```
Or you can also use a variable to instead the fixed text
```
textvar=tk.StringVar()
textvar.set('This is a changable string!')
text=tk.Label(window,
     textvariable=textvar,
     bg  ='red',
     font=('Arial',12)
	 width=10,height=3
	)
test.pack()
```
	
## add button

```
single_click_in_user_function=False

def user_function():
	global single_click_in_user_function
	if single_click_in_user_function == False:
		do something
	else:
		do other thing
	



button=tk.Button(window,
	text='There is a button!'
    bg  ='red',
    font=('Arial',12)
	width=10,height=3
	command=user_function # when single_click, this function will be run
	)
```
## add menubar 
## add entry 
## add listbox 
## add radiobutton 
## add messagebox 

## change the button position 
