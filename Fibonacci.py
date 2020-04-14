import time
from multiprocessing import Pool

#Recursivo
def fibR(n): 
    if n<=1: 
        return n
    else: 
        return fibR(n-1)+fibR(n-2)

#Iterativo
def fibI(n):
    if n == 0 or n == 1:
        return n
    ant2 = 0
    ant1 = 1
    for i in range(2, n+1):
        fib=ant1+ant2
        ant2=ant1
        ant1=fib
    return fib

#Con la funcion Pool
def fibP(n):
   if n <= 1:
       return n
   else:
       return(fibP(n-1) + fibP(n-2))

if __name__ == '__main__':
    n=20

    inicioP=time.time()
    try:
        p = Pool()
        print (p.map(fibP, [5,16,20]))
    finally:
        p.close()
    finP=time.time()

    inicioR=time.time()
    print(fibR(n))
    finR=time.time()
    
    inicioI=time.time()
    print(fibI(n))
    finI=time.time()
        
    print('\nIterativo tarda: ', finI-inicioI, ' , recursivo: ', finR-inicioR, 'y con la funcion pool: ',finP-inicioP)