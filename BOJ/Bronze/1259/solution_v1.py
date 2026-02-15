while(True) :
  num = input()
  if num == '0' : break
  temp = num[::-1]
  print("yes") if temp == num else print("no")
