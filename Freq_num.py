#Frequencies of Limited Range Array Elements

def freq(a,n):
  fre = {}
  for i in range(n):
    if a[i] not in fre:
      fre[a[i]] = 0
    fre[a[i]] += 1

  print("The frequency of each element is: ")
  for i in range(1,n+1):
    if i in fre:
      print("{}".format(fre[i]),end=" ")
    else:
      print("{}".format(0),end=" ")


a = list(map(int, input("Enter the elements to the array: ").split()))
n = len(a)
print("Entered array: {}".format(a))
print()
print("*"*50)
print()
print("The array after manipulation: {}".format(freq(a,n)))

