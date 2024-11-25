n=int(input("Enter a number"))
sum1=0

for i in range(1,n):
    sum1=sum1+i
print("sum of",n,"numer is",sum1)
    
total_sum=sum(range(1,n))
print("total_sum is",total_sum)