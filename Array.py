num=["kavindu","chamath",12,34,67]
print(num[0])
print(num[1])
print(num[2])
print(num[3])
print(num[4])

print( )
print(num[-1])
print(num[-2])
print(num[-3])
print(num[-4])
print(num[-5])

for i in num:
    print (type (i))
    
num=[1,2,3,4,5,6,58,69,7,98,36]
num.sort()
print(num)
# num.sort(reverse=True)
print(num)
num.append(10)
print(num)
print()
num.extend ((5,6,45))
print(num)
