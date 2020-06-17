height = float(input("身長を入力してください（cm） > "))
weight = float(input("体重を入力して下さい（kg） > "))
age = float(input("年齢を入力して下さい > "))
goal = float(input("目標の体重を入力してください > "))

energy = 13.397*weight+4.799*height-5.677*age+88.362
cal = (weight-goal)*7200
die = round(cal/energy)

print("-------------------------------------------")
print("基礎代謝量は"+str(round(energy))+"です")
print("目標の体重になるまでには"+str(cal)+"kcalのカロリーを減らす必要があります")
print("絶食生活を続けると"+str(die)+"日で目標の体重に到達します")