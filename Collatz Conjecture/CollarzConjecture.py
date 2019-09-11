#The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows: 
# start with any positive integer n. Then each term is obtained from the previous term as follows: 
# if the previous term is even, the next term is one half the previous term. If the previous term is
#  odd, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value 
# of n, the sequence will always reach 1. https://en.wikipedia.org/wiki/Collatz_conjecture

def main(n):    
    print(n)

    if 1 == n:
        return
        
    if n % 2 == 0:
        main(n/2)

    else:
        main(3*n+1)

if __name__ == '__main__':
    n = int(input('Enter a number:'))
    main(n)

