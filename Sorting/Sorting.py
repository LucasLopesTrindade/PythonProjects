import random


def buble_sort(rand_list):
	v=0
	for i,value in enumerate(rand_list):
		print(i,'-',value)
		#print(value)
		if i == len(rand_list)-1:
			break
			print('oi')
	
		if value> rand_list[i+1]:
			rand_list[i] = rand_list[i+1]
			rand_list[i+1] = value
			v+=1
		

		
	return rand_list

if __name__ == '__main__':
	n = 100
	rand_list = [random.randint(1,100) for i in range(100)] 
	print(rand_list)
	sorted_list = buble_sort(rand_list)
	print(sorted_list)