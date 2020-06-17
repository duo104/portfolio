# 間違い探しです。隠れた「め」を見つけましょう。その後、result.txtが作成されます

import random

count = 0
positions = []
problem = ""

A = "め"
B = "ぬ"

for x in range(1,11):
  for y in range(1, 11):
    if y % 10 == 0:
      print(A)
      problem += A + "\n"
    elif random.random() < 0.1:
      print(B, end="")
      count += 1
      problem += B

      p = [x, y]
      positions.append(p)
    else:
      print(A, end="")
      problem += A

print("「め」の数は{}個".format(count))

for a in positions:
  print("「め」は{}行、{}列目".format(a[0], a[1]))

with open("result.txt", "w") as f:
  f.write("間違い探しクイズ\n")
  f.write(problem)
  f.write("「め」の数は{}個\n".format(count))

  for a in positions:
    f.write("「め」は{}行、{}列目\n".format(a[0], a[1]))

  
         