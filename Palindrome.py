#Python code to check if the no. is palindrome

print("Enter a Number below")
i=int(input())   #for taking input no. from user
sum=0            #Variable to store reversed no.            
t=0              #Reminder variable
p=i              #To store value of i in p for comparing (12)
while(p>0):
    t=p%10                   
    sum=int(sum*10+t)
    p=int(p/10)
if(i==sum):      #Final comparing b/w original no. & reversed no.
    print("Yes")
else:
    print("No")
