def sort(l):

	for i in range(1,len(l)):
		key = l[i]
		j = i-1

		while (j>=0 and l[j]>key):
			l[j], l[i] = l[i],l[j]
			j = j-1


l = list(map(int, input().split()))
print(l)
print()
sort(l)
print(l)