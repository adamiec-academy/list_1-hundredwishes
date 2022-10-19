def cross(n):
    for i in range(n*3):
        if (i<n) or ((2*n)<=i):    
            print(' '*(n-1),'*'*n,' '*n)
        else:
            print('*'*n*3)
