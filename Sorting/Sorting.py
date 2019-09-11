import random
import matplotlib.pyplot as plt 
import numpy as np


def bubble_sort(rand_list):
    not_done = True
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    
    while not_done:
        not_done = False
        index = np.arange(len(rand_list))
        v=0
        
        for i,value in enumerate(rand_list):
            if i == len(rand_list)-1:
                break                

            if value> rand_list[i+1]:
                not_done = True
                rand_list[i] = rand_list[i+1]
                rand_list[i+1] = value
                v+=1
        ax1.clear()
        ax1.bar(index, rand_list)
        plt.pause(0.01)
        plt.draw()
#        plt.show()

    return rand_list

if __name__ == '__main__':
    n = 100
    #rand_list = [random.randint(1,100) for i in range(100)]
    rand_list = [i for i in range(100)]
    rand_list = random.sample(rand_list,n)
    sorted_list = bubble_sort(rand_list)
    print(sorted_list)