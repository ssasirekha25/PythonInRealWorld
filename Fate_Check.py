#Author:sasirekha
#A mixed random draw of your choice let see your fate
from random import choice
from random import randint
r=randint(1,10)
i=0
print("I know you are confused enter your two choice lets see your fate")
input1=input("Enter your choice one:")
input2=input("Enter your choice two:")
fate=0
count1,count2=0,0
print(r)
while(i<=r):
    draw = choice([input1,input2, input1, input1, input2,input2])
    #print(draw)
    if(draw==input1):
        count1+=1
    else:
        count2+=1
    i=i+1
result=1 if count1 > count2 else 2 
fate = input1 if result==1 else result2
print("fate decides you to choose:"+fate)


