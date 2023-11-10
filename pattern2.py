def pattern2(num):
    space=" "
    for i in range(1,num+1):
        for j in range(i):
            print(f"{j+1} ",end="")
        for k in range(num-i+1):
            print(" ",end="")
        print('\n')
            

num=int(input("Enter the number\n"))
pattern2(num)