import sys

			
def count_inversions(nums):
	:q

	return len(nums)			


if __name__ == '__main__':
	if len(sys.argv) <2:
		print 'please provide a name of a file which contains a list of random numbers seperated by newline'
		exit()
	lines=[]
	nums=[]
	with open(sys.argv[1]) as f:
		lines = f.readlines()
	for line in lines:
		nums.append(int(line))		
	print count_inversions(nums)
