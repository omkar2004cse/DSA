# string formatting by three ways 
# 1- by using %
# 2- by using format
# 3- by using f string

age=21
name='omkar'
# 1
print('I am %s and %d years Old'%(name,age))

# 2 
print("I am {} and {} years old".format(name,age))

# 3
print(f'I am {name} and {age} year old')