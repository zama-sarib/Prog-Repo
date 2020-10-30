#Given a binary array A[] of size N. The task is to arrange the array in increasing order.

l = int(input("\nEnter the size of the array\n"))
print()
A = list(map(int, input("Enter the binary array: ").split()))

c_z=0;c_o=0
for i in range(l):
  if A[i]==0:
    c_z+=1

c_o = l-c_z

print("\n")
print("0 "*c_z+"1 "*c_o)

