def pattern1(num):
    for i in range(1,num+1):
        for j in range(i):
            print(f"{i},",end=' ')

num=int(input("Enter the number\n"))
pattern1(num)