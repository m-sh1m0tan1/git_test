import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../source')))
from source.player import player_pon
from source.computer import computer_pon
from source.janken_judge import judge

# def main():
#    player_win = 0
#    computer_win = 0

#    """3回戦のじゃんけんゲームを行う関数"""
#    # hands = ['グー', 'チョキ', 'パー']

#    round = 1
#    while round <= 3:
#        print(f"-----ラウンド {round} -----")
#        computer_hand = computer.computer_pon()
#        player_hand = player.player_pon()
#        result = janken_judge.judge(computer_hand,player_hand)

#        print(f"あなたの手:{player_hand}")
#        print(f"コンピューターンの手:{player_hand}")

#        print("")  
#        if result == 'draw':
#          print("あいこです！ 再度対決！")    
#        else:
#          round += 1 
#          if result == 'player_win':
#              player_win +=1
#              print("あなたの勝ちです！")
#          else:
#              computer_win +=1
#              print("コンピューターの勝ちです！")            
#        print("")

#    print("【最終結果】")
#    print(f"あなた:{player_win}勝")
#    print(f"コンピュータ:{computer_win}勝")
#    if player_win >= computer_win:
#      print("あなたの総合勝利です！")
#    else:
#       print("コンピュータの総合勝利です！")
# 一つ目のメソッドはじゃんけんをするために作成、何ラウンド目かを引数としてうけとる、戻り値はじゃんけんの結果、ここでcomputer_pon()とplayer_pon()とjudge()を呼び出す
# 二つ目のメソッドは三回のじゃんけんが終わった後に総合勝利したのがどちらかを表示（戻り値）、引数は3つ目のメソッドでできた勝った回数
# 三つ目のメソッドは一つ目のメソッドで勝った方に増分＋１、あいこの場合増分はない
# 同時にラウンド数もプラス１、ここで一つ目のメソッドと二つ目のメソッド（勝った回数）を呼び出している


def first(round):
    # round = 1
#   while round <= 3:
    print(f"-----ラウンド {round} -----")
    computer_hand = computer_pon()
    player_hand = player_pon()
    result = judge(computer_hand,player_hand)
    print(f"あなたの手:{player_hand}")
    print(f"コンピューターンの手:{computer_hand}")
    print("")  
    if result == 'draw':
      print("あいこです！ 再度対決！")    
    else:
      round += 1 
      if result == 'player_win':
        # player_win +=1
        print("あなたの勝ちです！")
        return('player_win')
      else:
        # computer_win +=1
        print("コンピューターの勝ちです！")
        return('computer_win')          
    print("")

def second(player, computer):
    print(f"あなた:{player}勝")
    print(f"コンピュータ:{computer}勝")
    if player >= computer:
        return("あなたの総合勝利です！")
    else:
        return("コンピュータの総合勝利です！")

def third():
    round = 1
    player = 0
    computer = 0
    while round <= 3:
        result = first(round)
        if result == 'computer_win':
            computer += 1
            round += 1
        elif result == 'player_win':
            player += 1
            round += 1
    total = second(player, computer)
    return total
    

if __name__ == '__main__':
   third()