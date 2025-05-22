names =['modest','karen','lynn']
nums=[35,89,56,23]
values=(names, nums)
print(values)
x=min(nums)
print(x)
y="me"
#dictioary
data={1:'modest',2:'karen',3:'nakiroya'}
print(data[1])
print(data.get(3,'not found'))
print(data)
print(data.get(5,'not found'))
keys=['modest', 'junior','lynn','nancy']
value=['java','python', 'JS','CSS']
dictionary= dict(zip(keys, value))
print(dictionary)
#deleting to the dictionary
del dictionary['nancy']
print(dictionary)
#adding to the dictionary
dictionary['mary']= 'html'
print(dictionary)
print (type(names))