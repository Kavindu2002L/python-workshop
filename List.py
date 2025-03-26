num=[1,2,2,3,4,5,6,58,69,7,98,36]
#num.index(5)
print(max(num))
print(min(num))
print(len(num))

def filter_value(cost):
    if(cost>350):
        return True
    else:
        return False
price=[230,480,450,350,370]
filter_value=filter(filter_value,price)
print(list (filter_value))

samplelist=["12","name",54,10,29,245,789]
samplelist[2:5]=[25,45,55]
print(samplelist)