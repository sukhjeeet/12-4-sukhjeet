#user input

x = 0
num = int(input("enter year: "))
while (x < num):
  y = 0
  z = 0
  total = 0
  while (y < 12):
    print("enter  month:", y + 1, "")
    z = int(input())
    total = total + z
    y += 1
  x = x + 1
#finalizing the total and average 

avg = total / 12
print("totally :", total, "")
print("Average monthly rainfall:",avg,"")

