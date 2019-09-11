#USING THE SIEVE OF ERASTOTHENES ALGORITHM:
# Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number. 
#The sieve of Eratosthenes is one of the most efficient ways to find all primes smaller than n when n is smaller than 10 million.
import math

def main():
    
    p = 2
    i = 1
    n = int(input('Insert the n value:\n'))    
    # creating a list of all integers below "n"
    list_n = [number for number in range(2,n+1)]
    limit = int(math.sqrt(n))

    while p<=limit:

        list_mark = [mark for mark in range(p,n+1,p) if mark != p]
        list_n = list(set(list_n) - set(list_mark))

        p=list_n[i]
        i+=1
    return list_n


if  __name__ == '__main__':

    primes =  main()
    print(primes)
    




