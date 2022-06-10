"""
I/P: n=5
O/P: 5 4 3 2 1
"""

def reverseCounting(n):
    if(n==0):
        return
    
    print(n,end=' ')
    reverseCounting(n-1)

if __name__=="__main__":
    n=int(input())
    reverseCounting(n)