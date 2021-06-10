#!/usr/bin/env python3

import sys
import random

n = int(sys.argv[1])

#Create a list of random ip addresses
def random_IP_list(n):
	IP_list = []
	for num in range(n):
		w=random.randrange(256)
		x=random.randrange(256)
		y=random.randrange(256)
		z=random.randrange(256)
		IP = str(w) + '.' + str(x) + '.'+ str(y) + '.' + str(z)			
		IP_list.append(IP)

	lis = IP_list
	return lis

# Save them to a file, new line delimited
def save_file(lis):
	with open("temp_IPs.txt", "w") as file:
		file.writelines('%s\n' % IP for IP in lis)
	return file
	

# load all functions into memory
def main():	
	lis = random_IP_list(n)
	file = save_file(lis)

# run
if __name__ == "__main__":
	main()
