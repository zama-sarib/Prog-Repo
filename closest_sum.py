import sys
def closest_sum(a,n,target):
  min_diff = sys.maxsize
  out = 0
  for i in range(n-2):
    l = i+1
    r = n-1
    while l<r:
      s = a[i] + a[l] + a[r]
      if s<target:
        l+=1
      elif s>target:
        r-=1
      else:
        print("The target and calculated sum of the triplets are {}".format(s))
        return None
      if min_diff > abs(s-target) and s>out:
        min_diff = abs(s-target)
        out = s
  print("The sum is {}".format(out))

a = list(map(int, input("Enter the elements to the array: ").split()))
n = len(a)
target = int(input("Enter the target sum "))
a.sort()
closest_sum(a,n,target)