"""
I/P: n=5
O/P: 1 2 3 4 5
"""

def forwardCounting(n):
    if(n==0):
        return 
    
    forwardCounting(n-1)
    print(n,end=' ')

if __name__=="__main__":
    n=int(input())
    forwardCounting(n)