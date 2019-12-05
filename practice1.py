

        
l1= [(1,2),(4,5),(7,8)]
for x in l1:
    print(x[1])
    
for n in range(51):
    if n % 2 ==0:
        print(n)
        
        
c=[10,20,30,40,50,60]
print(10 in c)
print(20 in c)
print(80 in c)
print(50 in c)
print(90 not in c) 




exp=input('enter an expression:')
result = eval(exp)
print('the result is :',result)


 
        
a= int(input('enter the value:'))
b= int(input('enter the value:'))
if a<b:
    min=a
else:
    min=b
print('The min value is:',min)

a= int(input('enter the first value:'))
b= int(input('enter the second value:'))
print('both are equal' if a==b else 'second value is more' if b>a else 'first value is more')


a= int(input('enter the first value:'))
b= int(input('enter the second value:'))
c= int(input('enter the third value:'))
max= a if a>b and a>c else b if b>c else c
print('the max value is:',max)



# WAP to find sum and average of first n natural numbers

n=int(input('enter a num:'))
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print('the sum of first',n,' numbers is:',sum)
print('the average of first',n,'numbers is:',sum/n)


#Wap to find fatorial of any num

def fact(n):
    result = 1
    while n>1:
        result = result * n
        n=n-1
    return result
fact(5)



