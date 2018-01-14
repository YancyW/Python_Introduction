# Read/Write File
- myfile = open('file_name','option')
	- option = 'w',  write 
	- option = 'r',  read  
	- option = 'a',  append
  
- my_file.write("string")
- my_file.close()
- all = my_file.read()
	- will read all content once 
- line= my_file.readline()
	- will read one line each time, and prepare to read next line in the next time
- lines= my_file.readlines()
	- will read all lines once, and will put in to a list. (lines will become a list) 

