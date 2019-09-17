#####################################第二章#################################

##i,j=3,4
##i,j=2*j,i
##s=i+j
##print('s=',s)

##print(1,2,3,sep='-',end='\t')
##print('数量:{0},单价{1}'.format(100,45.8))
##print('数量:{0:4d},单价{1:3.3f}'.format(100,45.8))

##x,y,z=eval(input('Please:'))
##print(x,y,z,sep=',')
##print('{},{},{}'.format(x,y,z))

##from decimal import  Decimal
##x=eval(input('输入一个实数：'))
##y=int(x)
##z=Decimal(str(x))-Decimal(str(y))
####z=round(x%1,1)
##print(x,y,z,sep=',')

##import math
##x,y,z=eval(input('three float:'))
##average=(x+y+z)/3
##print(average)
##print(round(average,1))

##from random import *
##x=randrange(100,1000)
##print('orignal:',x)
##ge=x%10
##shi=x%100//10
##bai=x//100
##y=ge+bai*100
##print('transform:',y)

#####################################第三章#################################

#####################################第四章#################################

####2.5
##import math
##a=0
##b=0
##i=1
##sum4=0
##pai=0
####for i in range(1,1001):
####    a=1/(4*i-3)-1/(4*i-1)
####    sum4+=a
####pai=4*sum4
####print(pai,a)
##
##while i:
##    a,b=1/(4*i-3)-1/(4*i-1),-1/(4*i-1)
##    sum4+=a
##    i+=1
##    if math.fabs(b)<1e-6:break
##pai=sum4*4
##print(pai,b)

####2.6
##a,b=1,2
##sum=0
##for i in range(1,21):
##    c=b/a
##    print(c)
##    sum+=c
##    a,b=b,a+b
##print(sum)

####2.7
##for i in range(100,1000):
##    a=i%10
##    b=i//10%10
##    c=i//100
##    d=i/9
##    if int(d)==a**2+b**2+c**2:
##        print(i)

####2.8
##sum=0
##for N in range(1,1001):
##    for i in range(1,N):
##        if N%i==0:
##            sum+=i
##    if N==sum:
##        print(N)
##    sum=0

#####################################第五章#################################

##c='123'+'456'+'789'
##c+=c[-3:]*2
##print(c)

##s=input('sentence:')
##if s=='for':
##    print('It\'s for')
##elif s=='while':
##          print('It\'s while')
##else:
##          print('NO')

##import string
##s=input('test:')
##n=m=k=o=0
##for i in s:
##    if i in string.ascii_letters:
##        n+=1
##    elif i in string.digits:
##        m+=1
##    elif i==' ':
##        k+=1
##    else:
##        o+=1
##print(n,m,k,o)

##import string
##s=input('test:')
##A=s
##s1=''
##n=0
##for i in A:
##    if i in string.ascii_lowercase:
##        j=ord(i)-32
##        s1=s[:n]+chr(j)+s[n+1:len(s)]
##        s=s1
##    n+=1
##print(s)

##import string
##s=input('test:')
##sum=0
##for i in s:
##    if i in string.ascii_uppercase:
##        sum+=ord(i)-64
##    if i in string.ascii_lowercase:
##        sum+=ord(i)-96
##print(sum)

#####################################第六章#################################
##p=()
##t=()
##for i in range(10):
##    x=int(input())
##    t=(x,)
##    p+=t
##print(p)
    
##s=list(eval(input('列表s：')))
##index=0
##for i in s:
##    if i%2==0:
##       s[index]=i**2
##    index+=1
##print(s)

##import random
##t=()
##count=[]
##for i in range(10,100):
##    x=random.randrange(10,100)
##    t+=(x,)
##for i in t:
##    count+=[i,t.count(i)]
####count=[(x,t.count(x)) for x in t if t.count(x)>1]
##print(t,count,sep='\n')

##import random
##s=()
##for i in range(20):
##    x=random.randrange(0,500)
##    s+=(x,)
##print(s)
##s_former=sorted(s[0:9],reverse=True)
##s_latter=sorted(s[10:],reverse=False)
##s_transform=s_former+s_latter
##print(s_transform)

#####################################第七章#################################
##d={'Jack':'jack@mail.com','Tom':'Tom@mail.com'}
##d['Jim']='Jim@mail.com'
##del d['Tom']
##s=list(d.keys())
##s=sorted(s)
##print(s)

##numbers={}
##numbers[(1,2,3)]=1
##numbers[(2,1)]=2
##numbers[(1,2)]=3
##sum=0
##for k in numbers:
##    sum+=numbers[k]
##print(len(numbers),sum,numbers)

##a=set('ababcdabca')
##x={x for x in a if x not in 'ab'}
##print(a)
##print(x)
##print(a-x)
##print(a|x)
##print(a^x)
##print(a&x)

##dic={'星期一':'Monday','星期二':'Tuesday','星期三':'Wensday'}
##list1=dic.keys()
##list2=dic.values()
##list3=dic.items()
##print(list1,list2,list3,sep='\n')

dic={}
while 1:
    s=eval(input('key,values:'))
    print(s)
    if 'over' in s:break
    dic[s[0]]=s[1]
print(dic)

