# concatation is done with the string,list,tuple
# for concatation requried the same data types
name='omkar'
surname='jadhav'
full_name=name+surname
print(full_name)

l=['i','am','a','boy']
print(" ".join(l))

l1=['i','am','python','developer']
l2=['i','learn','python']

print("Concatation of string is:-",l1+l2)

t1=(1,2,3,'om')
t2=(12,33.34,'jadhav')
print("Concatation of tuple is:-",t1+t2)
