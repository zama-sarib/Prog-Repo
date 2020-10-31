#Juggling Algorithm to Rotate an array 

def rotate(a,n,k):
  d = -1;temp = a[0]
  for i in range(math.gcd(n,k)):
    j=i
    temp = a[i]
    while 1:
      d = (j+k)%n 
      if d == i:
        break
      a[j] = a[d]
      j = d
      print(a)
      print()
    a[j] = temp

  return a


a = list(map(int, input("Enter the elements to the array: ").split()))
n = len(a)
k = int(input("Enter the number of rotation: "))
print("Entered array: {}".format(a))
print()
print("*"*50)
print()
print("The rotated array: {}".format(rotate(a,n,k)))