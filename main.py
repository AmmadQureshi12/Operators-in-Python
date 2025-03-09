"Arithmetic Operator"
"Addition"
a=10
b=20
print(a+b)

"Subtraction"
a=10
b=20
print(b-a)
print(a-b)

"Multiplication"
a=10
b=20
print(a*b)

"Division"
a=5   
b=2
print(a/b) #Simple division operator give float value
print(a//b) #Floor division operator give integer value

"Modules Remainder"
a=10
b=3
print(a%b) #Modules operator give remainder

"Exponent"
a=2
b=3
print(a**b) #Exponent operator give power of number

"Assigment Operator"
y=10+20
print(y)

"Addition"
m=15
m=m+10
print(m)

"Subtraction"
m=15
m=m-10
print(m)

"Multiplication"
m=15
m=m*10
print(m)

"Divisiom"
m=15
m=m/10
print(m)

"Modules"
m=15
m=m%10
print(m)

"Exponent"
m=15
m=m**2
print(m)

"floor division"
m=15
m=m//10
print(m)

"comparision operator"
"== #Equal"
a=10
b=20
print(a==b)

#Not Equal 
a=10    
b=30    
print(a!=b)  #not equal operator give false if both values are same

#Greater than
a=20
b=30
print(a>b) #Greater than operator give false if first value is less than second value

#less than
a=20
b=30
print(a<b) #less than operator give false if first value is greater than second value

#greater than equal to
a=20
b=10
print(a>=b) #greater than equal to operator give true if first value is greater than second value and both values are equal so it give true.

#less than equal to
a=30
b=20
print(a<=b) #less than equal to operator give true if first value is less than second value and both values are equal so it give true.

"Logical operator"
#and operator
a=10
b=20
c=20
print(a<b and b==c) #and operator give true if both condition are true.

"or operator"
a=10
b=20
c=20
print(a>b or b==c) #or operator give true if any one condition is true.

#not operator
a=10
b=20
c=20
print(not a>b) #not operator give true if condition is false and give false is condition is true.


#Identity operator
#is operator
a=[10,20,30]
b=[10,20,30]
print(a is b) # list is mutable because both objects are assign differnt memory location so it give false.

a=[1,2,3]
b=[3,4,5]
print(a is b)

a=10
b=10
z=a
a=z
print(a is b) #True
print(a is z)  #true
print(b is z)  #true
print(a is a) #true
print(z is a)  #true
print(b is b) #true
print(z is z) #true
print(b is z) #true
print(a is b) #true
print(z is b) #true

x=300
y=300
print(x is y)
print(id(x))
print(id(y))

#is not operator
a=10
b=20
print(a is not b) 

a=[10,20,30]
b=[10,20,30]
print(a is not b) #list is mutable because both objects are assign differnt memory location so it give true.

a=[1,2,3]
b=[3,4,5]
print(a is not b)

a=10
b=10
z=a
a=z
print(a is not b) 
print(a is not z)  
print(b is not z)  
print(a is not a) 
print(z is not a)  
print(b is not b) 
print(z is not z) 
print(b is not z) 
print(a is not b) 
print(z is not b) 

x=300
y=300
print(x is not y)
print(id(x))
print(id(y))


x = "hello"
y = "hello"
print(x is not y)  # False (Python string interning ki wajah se)


m = "world!"
n = "world!"
print(m is not n)  # True (Strings mein special characters hone par interning nahi hoti)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 is not list2)  # True (Alag memory locations par hain)

list3 = list1
print(list1 is not list3)  # False (Same memory location ko refer karte hain)

a = None
b = None
print(a is not b)  # False (None ek singleton object hai, sabhi `None` variables same object ko refer karte hain)


class Car:
    pass

car1 = Car()
car2 = Car()
print(car1 is not car2)  # True (Dono alag instances hain)

car3 = car1
print(car1 is not car3)  # False (Dono same object ko refer karte hain)


tup1 = (1, 2, 3)
tup2 = (1, 2, 3)
print(tup1 is not tup2)  # True (Mostly alag memory locations honge)

tup3 = tup1
print(tup1 is not tup3)  # False (Same reference)

