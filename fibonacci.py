def fibonacci(n):
    if n<=1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
print("Enter the number of terms")
num=int(input())
print ("fibonacci series : ")
for i in range(num):
    print(fibonacci(i))
