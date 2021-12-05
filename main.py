feb = 2
febDay = 18
userMonth = int(input())
userDay = int(input())

if userMonth==feb:
  if febDay>userDay:
    print("Before")
  elif febDay==userDay:
    print("Special")
  else:
    print("After")
  # Special Day Check
elif feb < userMonth:
  print("After")
else:
  print("Before")