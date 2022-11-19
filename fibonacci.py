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

    
    
 OUTPUT :-
Enter the number of terms
20
fibonacci series : 
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
> 
