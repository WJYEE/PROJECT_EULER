# Python - 1(내가 한 거)
def multiple_of_num(num, n):
  sum = 0
  n = (n-1)//num
  for i in range(1,n+1):
    sum += num*i
  return sum

print(multiple_of_num(3,1000)+multiple_of_num(5,1000)-multiple_of_num(3*5,1000))