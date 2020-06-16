import random

class Poker():

  cards = []

  def handout(self):
    num = random.randint(0, 13)
    return num

  def marks(self):
    kind = random.randint(0, 3)
    if kind == 0:
      return "のスペード"
    if kind == 1:
      return "のハート"
    if kind == 2:
      return "のクローバー"
    if kind == 3:
      return "のダイヤ"       
        

poker = Poker()

player_hand_1 = poker.handout()
player_hand_1_kind = poker.marks()
player_hand_2 = poker.handout()
player_hand_2_kind = poker.marks()

enemy_hand_1 = poker.handout()
enemy_hand_1_kind = poker.marks()
enemy_hand_2 = poker.handout()
enemy_hand_2_kind = poker.marks()

print("あなたの持っているカードは： {0}, {1} です".format(str(player_hand_1) + str(player_hand_1_kind), str(player_hand_2) + str(player_hand_2_kind)))

preflop = input("チェックしますか？フォールドしますか？ チェック=0, フォールド=1 : ")

if int(preflop) == 0:
  print("チェックしました")
elif int(preflop) == 1:
  print("フォールドしました")  
else:
  print('間違えた入力です。もう一度入力して下さい')
    