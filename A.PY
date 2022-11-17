from time import sleep
import os
def pr(n,h,k):
    if n%2 == 0:
        n = n-1
    s = [2*n-h, 2*n-k]
    for i in range(1,n+1):
        print()
        for j in range(1,2*n+1):
            if i == n//2:
                if j in s:           
                    print('/', end='')
                elif j == n:
                    print('|', end="")
                else:
                    print('-', end='')
            else:
                if j in s:           
                    print('/', end='')
                elif j == n:
                    print('|', end="")
                else:
                    print(' ', end='')
        s = [i-1 for i in s]



for i in range(11,1,-1):
    if i == 2:
        pr(11,2,i)
    else:
        pr(11,2,i)
        sleep(0.05)
        os.system('cls')


    





# STEP 2
# from time import sleep
# def pr(n,h,k):
#     if n%2 == 0:
#         n = n-1
#     s = [2*n-h, 2*n-k]
#     for i in range(1,n+1):
#         print()
#         for j in range(1,2*n+1):
#             if i == n//2:
#                 if j in s:           
#                     print('/', end='')
#                     s[s.index(j)] = s[s.index(j)] - 1
#                 elif j == n:
#                     print('|', end="")
#                 else:
#                     print('-', end='')
#             else:
#                 if j in s:           
#                     print('/', end='')
#                     s[s.index(j)] = s[s.index(j)] - 1
#                 elif j == n:
#                     print('|', end="")
#                 else:
#                     print(' ', end='')

# STEP 1
# n = int(input())
# if n%2 == 0:
#     n = n-1
# for i in range(1,n+1):
#     if i-1 == n//2:
#         print(('-'*(n))+'|'+('-'*(n)))
#     else:
#         print((' '*(n))+'|'+(' '*(n)))