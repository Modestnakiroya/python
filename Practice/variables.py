num = 5 
id(num) # returns the memory address of the variable num
print(id(num))
type(num) # returns the type of the variable num
print(type(num))
b=num # b is a reference to the same object as num
print(id(b)) # returns the memory address of the variable b which is the same as num

#data types 
m=6+5j # complex number
print(type(m)) 
print(m.real) 
print(m.imag) 
x= 5.6
y= int(x) # converts float to int
z= float(y) # converts int to float
print(y)
print(z)
names =('modest','karen','lynn') # tuple
cars =['toyota','nissan','honda'] # list
brands = {'nike', 'adidas', 'puma'} # set
str = 'arthur' # string
range(10)
list(range(10)) # converts range to list
print(list(range(10))) 