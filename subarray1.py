def calc(a,n,sum1):

	start = 0
	curr_sum = a[0]
	i=1

	while i<n:
		while curr_sum>sum1 and start <i-1:
			curr_sum = curr_sum - a[start]
			start+=1

		if curr_sum == sum1 :
			print("The required subarray found between {} and {} index".format(start+1,i))
			return None

		if i<n:
			curr_sum = curr_sum + a[i]
			i+=1

a = list(map(int, input("Enter the elements to the array ").split()))
n = len(a)
sum1 = int(input("Enter the sum of the subarray "))

calc(a,n,sum1)
