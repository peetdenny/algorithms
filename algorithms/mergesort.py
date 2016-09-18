import sys

def sort(set):
	if len(set)<2 :
		return set
	else:	
		pivot = (len(set)/2)-1
		list1=sort(set[0:pivot+1])
		list2=sort(set[pivot+1:len(set)])
		return merge(list1, list2)

def merge(list1, list2):
	merged=[]
	#Compare 1 from left with successive from right until L wins, then pop L and proceed with 2 from L
	l_idx=0
	r_idx=0
	while(l_idx<len(list1) and r_idx<len(list2)):
		l = list1[l_idx]
		r = list2[r_idx]
		if int(l) < int(r):
			merged.append(l)
			l_idx+=1
		else:
			merged.append(r)
			r_idx+=1

	#Exiting the above loop will have left one of the lists incompletely processed. 
	#We can just put the rest of the items from that list into merged
	
	if(l_idx < len(list1)):
		for i in list1[l_idx:]:
			merged.append(i)
	if(r_idx < len(list2)):
		for i in list2[r_idx:]:
			merged.append(i)
	return merged
						


if __name__ == '__main__':
	if len(sys.argv) <2:
		print 'please provide a name of a file which contains a list of random numbers'
		exit()
	lines=[]
	nums=[]
	with open(sys.argv[1]) as f:
		lines = f.readlines()
	for line in lines:
		nums.append(int(line))		
	print sort(nums)
