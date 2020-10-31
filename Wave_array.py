# Wave Array

def warr(a,n):
  a.sort()
  for i in range(0,n-1,2):
    temp = a[i]
    a[i] = a[i+1]
    a[i+1] = temp

  return a

a = list(map(int, input("Enter the elements to the array: ").split()))
n = len(a)
print("Entered array: {}".format(a))
print()
print("*"*50)
print()
print("The array after manipulation: {}".format(warr(a,n))) 


