
##def var(*t):
##    print(t)
##var(1,2,3)
##def bar(**t):
##    print(t)
##bar(age=25,x=3)

##def DECO(num): 
##    def deco(f):
##        def newf(x,y):
##            print(num+'original',x,y)
##            return f(x,y)
##        return newf
##    return deco
##@DECO('参数')
##def sqrsum(x,y):
##    return x**2+y**2
##print(sqrsum(10,20))

##x=10
##def f():
##    #y=x
##    x=0
##    print(x)
##print(x)
##f()

##class CC:
##    __x=10
##    y=20
##    z=30
##    def show(self):
##        print(self.__x,self.y,self.z)
##b=CC()
##b.y=80
##b.show()
##CC.id='250'
##b.num='320'
##print(CC.y,CC.id)
##print(b.num)
##print(CC.num)

##class Car:
##    number=4
##    engine='electric'
##    def __init__(self,color,brand):
##        self.color=color
##        self.brand=brand
##    @classmethod
##    def switch(cls):
##        cls.engine='gas'
##        print(cls.engine)
##    def show(self,nickname):
##        print('{:s},{:s},{:s}'.format(self.color,self.brand,nickname))
##
##class Microcar(Car):
##    size='small'
##    powerlevel=2
##    def __init__(self,color,brand,seats):
##        Car.__init__(self,color,brand)
##        self.seats=seats
##    def show(self,nickname):
##        print(self.seats)
##        Car.show(self,nickname)
##auto=Microcar('Red','Benz',5)
##auto.show('Burning')

##class Point:
##    x=10
##    y=10
##    def __init__(self,x,y):
##        self.x=x
##        self.y=y
##pt=Point(20,20)
##print(pt.x,pt.y)
##print(Point.x,Point.y)

##class C():
##    f=10
##class C1(C):
##    pass
##print(C.f,C1.f)

##class A:
##    def __init__(self,id):
##        self.id=id
##        id=888
##acc=A(8)
##print(acc.id)

##class parent:
##    def __init__(self,param):
##        self.v1=param
##class children(parent):
##    def __init__(self,param):
##        parent.__init__(self,param)
##        self.v2=param
##obj=children(100)
##print(obj.v1,obj.v2)

class account:
    def __init__(self,id,balance):
        self.id=id
        self.balance=balance
    def d(self,am):
        self.balance+=am
    def w(self,am):
        self.balance-=am
acc1=account('1224',100)
acc1.d(300)
acc1.d(500)
acc1.w(200)
acc1.w(300)
print(acc1.balance)
