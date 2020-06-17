height = float(input("身長を入力してください（cm） > "))
weight = float(input("体重を入力して下さい（kg） > "))

height = height/100

def bmi(height, weight):
  bmi = weight / height**2
  print(bmi)

bmi(height, weight)